# SPDX-FileCopyrightText: 2022 Thomas Foerster <thomas.foerster@hzdr.de>
#
# SPDX-License-Identifier: MIT

from header import *

#=== Session 1.1 ===#
# Checking and reseting
if os.path.exists(filename1):
    os.remove(filename1)

#=== Session 1.2 ===#
# There are several ways to enrich the hdf5 file with content. 
# One methode is with create_dataset!

# Open a h5py._hl.files.File type
# Be aware that you need to close the file as well!
# see: https://stackoverflow.com/questions/25070854/why-should-i-close-files-in-python

h5file = h5py.File(filename1,'w')
h5file.create_dataset(dataset1,data=d1)
h5file.create_dataset(dataset2,data=d2)

# How to extract data from an h5 file
# --A-- 
# via the 'get' methode --> h5 dataset
nA1 = h5file.get(dataset1)
nA2 = np.array(h5file[dataset1])

# --B--
# via h5 array syntax
nB1 = h5file[dataset1]
nB2 = h5file[dataset1][()] 

# Check if nA2 equals nB2
equal_array1 = (nA2 == nB2).all()
print(f"Are methode A and B are equal?: {equal_array1}")

# Display the key overview of the file content
print(f"h5 file keys:{h5file.keys()}")

h5file.close()

#Let's parse the array elements
with h5py.File(filename1,'r') as h5file:

    # Get the h5py dataset
    # t1 and t2 are not available after 'with' is finished
    t1=h5file[dataset1]
    t2=h5file[dataset2]

    data = t1[t1[()]>0.001]


