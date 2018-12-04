#!/usr/bin/env python
#name of the processor
from mpi4py import MPI
comm = MPI.COMM_WORLD
name = MPI.Get_processor_name()
shared = (comm.rank+1)*5

# send the data to the other node. dest = size -rank
if comm.rank ==0: 
    data = shared 
    comm.send(data,dest=  1)# destination, send it to dest 1, give me error as
    print("from rank %s we senr %s"%(comm.rank, data))
    # I have only 0 rank. 
elif comm.rank == 1: 
    data = comm.recv(source =0)# recieve the data from rank 0 which is source.
    print("on node%s we recieved %s"%(comm.rank, data))