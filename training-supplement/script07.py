# SPDX-FileCopyrightText: 2022 Thomas Foerster <thomas.foerster@hzdr.de>
#
# SPDX-License-Identifier: MIT

#-- 3. Create links
#-- Links to the dataset Links to the group hard links soft links

from header import *

# Checking and reseting
if os.path.exists(filename7):
    os.remove(filename7)

#-- Example with Hard Links
with h5py.File(filename7,'w') as h5file:
    
    h5file.create_dataset(dataset1,data=d1)
    h5file.create_dataset(dataset2,data=d2)
    
    t1=np.array(h5file.get(dataset1))
    t2=np.array(h5file.get(dataset2))
    
    print(h5file.keys())
    
    h5file[dataset3] = 42
    
    t3=np.array(h5file.get(dataset3))
    
    #-- this is the hard link (like a pointer to the same instance)
    h5file[dataset4] = h5file.get(dataset3)
    
    t4 = h5file.get(dataset4)
    
    print(t4)
    
    t4=np.array(h5file.get(dataset4))
    
