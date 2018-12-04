#!/usr/bin/env python
# scatter : take the list(object) and send to each of the nodes

from mpi4py import MPI 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank ==0: 
    data = [(x+1)**x for x in range(size)]
    print("we will be scaterrung %s"% data)
else: 
    data = None
data = comm.scatter(data, root=0)
print("rank %s has data %s"%(rank, data))



