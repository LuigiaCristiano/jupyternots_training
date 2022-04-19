# SPDX-FileCopyrightText: 2022 Thomas Foerster <thomas.foerster@hzdr.de>
#
# SPDX-License-Identifier: MIT

#----------------------------------------------------------------------
# Chapter 2. Introducing the hierarchical structure
#    Using group function
#    Group can be seen as container to organize the data in the HDF5.
#    They are characterized by 
#       - keys (names), 
#       - vakues (container elements)
#----------------------------------------------------------------------
from header import *

# remove the file filename3 if exits
if os.path.exists(filename3):
    os.remove(filename3)

# Open file h5file
h5file = h5py.File(filename3,'w')

g1  = h5file.create_group('group1')
dg1 = g1.create_dataset('data1',data=d1)

print(g1.items())
print(g1.name)

print("----------------------")

# You can notice that the name of the group is specified by a slash "/"
# 
# Every group is created with an hard link and is possible to explore the content using the
# keys function
# 
# items,values,keys are calls to explore the groups The names of the objects are all strings

subgroup = g1.create_group("/group1/subgroup1")
print(subgroup.name)

out=h5file['group1']['subgroup1']
print(out)
print(g1.values())

# Close file h5file
h5file.close()

print("----------------------")

