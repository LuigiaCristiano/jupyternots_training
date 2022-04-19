<!--
SPDX-FileCopyrightText: 2022 Thomas Foerster <thomas.foerster@hzdr.de>

SPDX-License-Identifier: CC-BY-4.0
-->

# RDM Trainings

# Background

...

# Use the material

## Getting The setup

***Installing the repo***

~~~
$ git clone https://gitlab.helmholtz-berlin.de/a2395/training_material1.git
$ cd training_material1
$ bash run.sh && exit
~~~

***Uninstalling the repo***

First command removes the kernel and `rm` removes the folder, incl. the build env.

~~~
$ jupyter kernelspec remove run-training
$ cd ..
$ rm -rf training_material1
~~~


# Project Files 

In terms of the training the following files need not to be tinkered with 

`pyproject.toml`
: poetry package configure

`poetry.toml`
: poetry additional settings

`poetry.lock`
: poetry internal config file

`*.license`
: license information

`LICENSES/`
: License folder


# Licensing
...


