import collections
import torch

# This function is for attack / defense at clients;
# for attack / defense at the server, please use create_fake_model_list*()
def create_fake_global_w_local_w_MNIST():
    local_w = dict()
    local_w["linear.weight"] = torch.FloatTensor(
        [
            [-0.0003, 0.0192, -0.0294, 0.0219, 0.0037, 0.0021],
            [-0.0198, -0.0150, -0.0104, -0.0203, -0.0060, -0.0299],
            [-0.0201, 0.0149, -0.0333, -0.0203, 0.0012, 0.0080],
            [0.0237, 0.0103, -0.0219, 0.0088, -0.0009, 0.0009],
            [0.0144, -0.0336, -0.0346, -0.0222, -0.0025, -0.0138],
            [-0.0196, -0.0118, 0.0230, -0.0202, 0.0172, 0.0355],
        ]
    )
    local_w["linear.bias"] = torch.FloatTensor(
        [-0.0753, -0.0589, -0.0907, -0.0672, 0.1159, 0.0290]
    )
    global_w = dict()
    global_w["linear.weight"] = torch.FloatTensor(
        [
            [-0.0003, 0.0192, -0.0294, 0.0219, 0.0037, 0.0021],
            [-0.0198, -0.0150, -0.0104, -0.0203, -0.0060, -0.0299],
            [-0.0201, 0.0149, -0.0333, -0.0203, 0.0012, 0.0080],
            [0.0237, 0.0103, -0.0219, 0.0088, -0.0009, 0.0009],
            [0.0144, -0.0336, -0.0346, -0.0222, -0.0025, -0.0138],
            [-0.0196, -0.0118, 0.0230, -0.0202, 0.0172, 0.0355],
        ]
    )
    global_w["linear.bias"] = torch.FloatTensor(
        [-0.0745, -0.0578, -0.0899, -0.0662, 0.1122, 0.0295]
    )
    return local_w, global_w


# This function is for attack / defense at clients;
# for attack / defense at the server, please use create_fake_model_list*()
def create_fake_vectors():
    return torch.FloatTensor([[0, 0, 0], [0, 0, 0], [1, 1, 1]]), torch.FloatTensor(
        [[3, 1, 1], [5, 5, 5], [2, 2, 2]]
    )


# This function is for attack / defense at clients;
# for attack / defense at the server, please use create_fake_model_list*()
def create_fake_global_w_local_w():
    local_w = dict()
    local_w["linear.weight"] = torch.FloatTensor(
        [[0, 0, 0], [0.2, 0.2, 0.2], [0.1, 0.1, 0.1]]
    )
    local_w["linear.bias"] = torch.FloatTensor([0, 0, 0.1])
    global_w = collections.OrderedDict()
    global_w["linear.weight"] = torch.FloatTensor(
        [[0.3, 0.1, 0.1], [0.5, 0.5, 0.5], [0.2, 0.2, 0.2]]
    )
    global_w["linear.bias"] = torch.FloatTensor([0.1, 0.1, 0.1])

    return local_w, global_w


def create_fake_model_list(active_worker_num):  # local_w for defenses at server
    a_local_w = dict()
    a_local_w["linear.weight"] = torch.FloatTensor(
        [[0, 0, 0], [0.2, 0.2, 0.2], [0.1, 0.1, 0.1]]
    )
    a_local_w["linear.bias"] = torch.FloatTensor([0, 0, 0.1])
    model_list = []
    for i in range(active_worker_num):
        model_list.append((i + 20, a_local_w))  # add a random sample num
    # print(model_list[0])
    # print("------")
    # print(model_list)
    return model_list


#
if __name__ == "__main__":
    print(create_fake_model_list(10))
