# SPDX-FileCopyrightText: 2022 Thomas Foerster <thomas.foerster@hzdr.de>
#
# SPDX-License-Identifier: MIT

import numpy as np
import h5py 
import os
#import json
import time
from jupyterlab_h5web import H5Web

#Global variables
filename1 = "simple1.h5"
filename2 = "simple2.h5"
filename3 = "simple3.h5"
filename4 = "simple4.h5"
filename5 = "simple5.h5"
filename6 = "simple6.h5"
filename7 = "simple7.h5"
filename8 = "simple8.h5"
filename9 = "simple9.h5"
dataset1  = "dataset1"
dataset2  = "dataset2"
dataset3  = "dataset3"
dataset4  = "dataset4"

X     = np.arange(-5, 5, 0.25)
Y     = np.arange(-5, 5, 0.25)
Xg,Yg = np.meshgrid(X, Y)

# Definition of new arrays of data
# via a list comprehension (advanced)
d1 = [np.sin(2*np.pi*f*np.sqrt(Xg**2 + Yg**2)) for f in np.arange(0.1, 1.1, 0.1)]
d2 = np.sin(np.sqrt(Xg**2 + Yg**2))
d3 = X
d4 = 42


