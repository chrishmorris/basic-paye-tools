# install this container, on debian/ubuntu

#sudo apt-get install singularity-container debian-archive-keyring debootstrap

# build singularity container  
singularity instance.stop paye || true
rm -rf sandbox || true 

# can build from recipe file only as root
if [ ! -f sandbox.simg ]; then
    sudo singularity build java.simg java.spec
fi 
if [ ! -f payetools.zip ]; then
    curl -Lo payetools.zip https://www.gov.uk/government/uploads/uploaded/hmrc/payetools-rti-19.1.19116.1393-linux.zip
fi

rm paye.simg || true
sudo singularity build --force paye.simg paye.spec

# now convert to a userspace sandbox
singularity build --sandbox sandbox paye.simg
# ignore warnings, we will not run this container as root.
# also ignore error message, it is inaccurate

bash start.sh

