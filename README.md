# basic-paye-tools
Installation of HMRC Basic Paye Tools in a singularity container

The HMRC's Basic PAYE Tools run on Windows or 32-bit Linux. 
Installing the dependencies in a 64 bit system does not always work. 
This project does the installation in a Singularity container, 
so avoiding breaking the host system.

To use it, check out, cd to the new directory, and
   ./build.sh
