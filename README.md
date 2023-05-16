# GROMACS_redeployment

To deploy GROMACS on the pawsey Setonix system I tried two approaches:
1) I built a Docker image with the implemented Gromacs code following the image provided [by Pawsey](https://quay.io/organization/pawsey)
2) I used Pawsey's [spack script](https://github.com/PawseySC/pawsey-spack-config) following the instructions on the user website.

In case 1 there appears to be a problem with the Pawsey's provided images, so the current version of the Docker deployment has been uploaded without specific optimization for Setonix.

In case 2 I used the attached package.py script in conjuction with Pawsey's spack standard procedure installation to deploy GROMACS as a module. 
