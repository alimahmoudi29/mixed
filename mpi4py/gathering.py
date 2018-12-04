#!/usr/bin/env python

#gatter: gather all the objects
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

newData= comm.gather(data, root =0)# senf to node 0

if rank==0: 
    print("master collected:%s"%newData)

# reduce: 
# scan: 



