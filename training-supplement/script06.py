# SPDX-FileCopyrightText: 2022 Thomas Foerster <thomas.foerster@hzdr.de>
#
# SPDX-License-Identifier: MIT

from header import *

if os.path.exists(filename6):
    os.remove(filename6)

with h5py.File(filename6,'w') as h5file:
    
    g1  = h5file.create_group('group1')
    dg1 = g1.create_dataset('data1',data=d1)
    
    print(h5file['group1'].keys())

