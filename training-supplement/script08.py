# SPDX-FileCopyrightText: 2022 Thomas Foerster <thomas.foerster@hzdr.de>
#
# SPDX-License-Identifier: MIT

#-- 4. Specify data type and Insert compression

from header import *

# Checking and reseting
if os.path.exists(filename8):
    os.remove(filename8)

# Generating a dataset
with h5py.File(filename8,'w') as h5file:
    
    dset_int1    = h5file.create_dataset('integers' , (10,), dtype='i1')
    dset_int8    = h5file.create_dataset('integers8', (10,), dtype='i8')
    dset_complex = h5file.create_dataset('complex'  , (10,), dtype='c16')
    
    dset_int1[0]    = 2200
    dset_int8[0]    = 2200.1
    dset_complex[0] = 3+4j    
    
    print("Files content of array 'integers'", h5file['integers'][:])
    print("Files content of array 'integers8'", h5file['integers8'][:])
    
    # Adding compression
    h5file.create_dataset( dataset1, (100000,), dtype='i1' , compression="gzip", compression_opts=9)
    h5file.create_dataset( dataset2, (100000,), dtype='i8' , compression="gzip", compression_opts=9)
    h5file.create_dataset( dataset3, (100000,), dtype='f16', compression="gzip", compression_opts=9)

    #-- Resizing
    # Generating dataset
    d = h5file.create_dataset(dataset4, (100, ),  maxshape=(500, ))
    
    # Manipulating the dataset
    d[:100] = np.random.randn(100)
    d.resize((200,))
    d[100:200] = np.random.randn(100)

# Get data from dataset
with h5py.File(filename8,'r') as h5file:
    dset = h5file[dataset4]
    print(dset[99])
    print(dset[199])

# Generating Chunks
with h5py.File(filename8,'a') as h5file:
    h5file.create_dataset("chunked", (1000, 1000), chunks=(100, 100))
    h5file.create_dataset("autochunk", (1000, 1000), chunks=True)

    print("Keys of dataset",h5file.keys())

