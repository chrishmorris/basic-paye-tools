singularity instance.start --cleanenv --contain --writable --bind shared:/shared sandbox/ paye
# maybe  --containall --no-home --no-privs --overlay= --userns  
singularity instance.list
echo 'to get a shell connection to the container: singularity shell instance://paye'
echo 'to stop it: singularity instance.stop janus'
