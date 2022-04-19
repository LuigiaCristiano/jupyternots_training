# SPDX-FileCopyrightText: 2022 Thomas Foerster <thomas.foerster@hzdr.de>
#
# SPDX-License-Identifier: MIT

from header import *

# with dictionary call and direct keys definition

# remove the file filename2
if os.path.exists(filename2):
    os.remove(filename2)

with h5py.File(filename2,'w') as h5file:
    h5file['one'] = d1
    h5file['two'] = d2

# Show that the file filename2 is closed, but was writen 
print(h5file)


