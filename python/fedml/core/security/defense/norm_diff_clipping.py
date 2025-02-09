import torch
from .defense_base import BaseDefenseMethod
from ...security import utils

"""
defense @ client, added by Shanshan, 06/28/2022
"Can You Really Backdoor Federated Learning?" 
https://arxiv.org/pdf/1911.07963.pdf 
"""


class NormDiffClipping(BaseDefenseMethod):
    def __init__(self, norm_bound):
        self.norm_bound = norm_bound  # for norm diff clipping and weak DP defenses

    def defend(self, local_w, global_w, refs=None):
        vec_local_weight = utils.vectorize_weight(local_w)
        vec_global_weight = utils.vectorize_weight(global_w)
        clipped_weight_diff = self._get_clipped_norm_diff(
            vec_local_weight, vec_global_weight
        )
        clipped_w = self._get_clipped_weights(local_w, global_w, clipped_weight_diff)
        return clipped_w

    def _get_clipped_norm_diff(self, vec_local_w, vec_global_w):
        vec_diff = vec_local_w - vec_global_w
        weight_diff_norm = torch.norm(vec_diff).item()
        clipped_weight_diff = vec_diff / max(1, weight_diff_norm / self.norm_bound)
        return clipped_weight_diff

    @staticmethod
    def _get_clipped_weights(local_w, global_w, weight_diff):
        # rule: global_w + clipped(local_w - global_w)
        recons_local_w = {}
        index_bias = 0
        for item_index, (k, v) in enumerate(local_w.items()):
            if utils.is_weight_param(k):
                recons_local_w[k] = (
                    weight_diff[index_bias : index_bias + v.numel()].view(v.size())
                    + global_w[k]
                )
                index_bias += v.numel()
            else:
                recons_local_w[k] = v
        return recons_local_w
