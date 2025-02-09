#!/usr/bin/env bash
WORKER_NUM=$1
PROCESS_NUM=`expr $WORKER_NUM + 1`
echo $PROCESS_NUM
hostname > mpi_host_file
$(which mpirun) -np $PROCESS_NUM \
python torch_fedml_mpi_object_detection.py --cf config/fedml_object_detection.yaml