# SPDX-FileCopyrightText: 2022 Thomas Foerster <thomas.foerster@hzdr.de>
#
# SPDX-License-Identifier: MIT

# Metadata

# Many groups can be defined and many arrays associated to the groups
# del command can be used to remove objects
from header import *

if os.path.exists(filename4):
    os.remove(filename4)

with h5py.File(filename4,'w') as h5file:
    
    g1  = h5file.create_group('group1')
    dg1 = g1.create_dataset('data1',data=d1)
    
    print(g1.items())
    
    g1.attrs['Date'] = time.time()
    g1.attrs['User'] = 'Me'
    
    for k in g1.attrs.keys():
        print(k, g1.attrs[k])

    for j in dg1.attrs.keys():
        print(j, dg1.attrs[j])

