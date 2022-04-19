# SPDX-FileCopyrightText: 2022 Thomas Foerster <thomas.foerster@hzdr.de>
#
# SPDX-License-Identifier: MIT

#-- 6. Plotting and Visualization
from header import *

# Checking and reseting
if os.path.exists(filename9):
    os.remove(filename9)

with h5py.File(filename9, "w") as h5file:
    
    h5file['3D']     = d1
    h5file['2D']     = d2
    h5file['1D']     = d3
    h5file['Scalar'] = d4

    print("Keys of dataset",h5file.keys())
