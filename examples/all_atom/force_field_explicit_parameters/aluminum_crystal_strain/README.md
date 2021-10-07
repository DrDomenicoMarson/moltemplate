Aluminum crystal under strain
=============================
A simulation of a small alluminum crystal under high pressure.

### Images

<img src="images/AlCell_LR.jpg" width=110> <img src="images/rightarrow.svg" height=80> <img src="images/AlCrystal10x10x10_t=0steps_LR.jpg" height=140> <img src="images/rightarrow.svg" height=80> <img src="images/AlCrystal10x10x10_t=20000steps_LR.jpg" height=140>


## Details

NOTE: This example requires the "Al99.eam.alloy" file.
(It was not included in this directory because if its large size.)
As of 2012-11, I was able to obtain it here:
http://www.ctcms.nist.gov/~cbecker/Download/Al-YM/Al99.eam.alloy
Copy it to the directory containing this README file.

This example shows an alternative way to setup the
aluminum crystal loading simulation described here:
https://icme.hpc.msstate.edu/mediawiki/index.php/Uniaxial_Compression.html
by Mark Tschopp and Nathan R. Rhodes
For additional backgroumd information, please consult that web page.

In this example, I use moltemplate to build a "DATA" file for this system.
(I can't think of a compelling reason to do this for simple simulations like
this. But this approach might be useful if you want to artificially create
unusual structures out of aluminum crystals, or mix them with other molecules.
I created this example in response to a user request.)

### Instructions

More detailed instructions on how to build LAMMPS input files and
run a short simulation are provided in other README files.

1) To build the files which LAMMPS needs, follow the instructions in:
[README_setup.sh](README_setup.sh)

2) To run LAMMPS with these files, follow these instructions:
[README_run.sh](README_run.sh)

This will create an ordinary LAMMPS dump file (traj.lammpstrj) that you can visualize with Ovito, VMD, or AtomEye.  (See README_visualize.txt)

It will also create a number of other files, such as:
dump.comp_0.cfg
dump.comp_500.cfg
dump.comp_20000.cfg
Al_comp_100.def1.txt

The dump.comp_*.cfg files can be visualized using
AtomEye if you have AtomEye and ImageJ installed.
The procedure for doing this is explained in the original tutorial at:
http://icme.hpc.msstate.edu/mediawiki/index.php/Uniaxial_Compression

The "Al_comp_100.def1.txt" file is a four-column text file containing:
column 1:     v_strain = (lx - v_L0)/v_L0
column 2:     -pxx/10000  (diagonal components of the stress tensor)
column 3:     -pyy/10000
column 4:     -pzz/10000
