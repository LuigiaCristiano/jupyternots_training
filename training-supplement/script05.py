# SPDX-FileCopyrightText: 2022 Thomas Foerster <thomas.foerster@hzdr.de>
#
# SPDX-License-Identifier: MIT

from header import *

if os.path.exists(filename5):
     os.remove(filename5)

metadata = {'Date': time.time(), 'User': 'Me', 'OS': os.name,}

with h5py.File(filename5,'w') as h5file:
    g1 = h5file.create_group('group1')
    d = g1.create_dataset('data_1', data=d1)
    m = g1.create_dataset('metadata', data=json.dumps(metadata))
    print(h5file['group1']['metadata'])
    print(g1.name)

