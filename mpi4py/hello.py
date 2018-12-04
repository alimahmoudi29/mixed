#!/usr/bin/env python
from mpi4py import MPI
comm = MPI.COMM_WORLD
print("hell the rank is %s"%comm.rank)




