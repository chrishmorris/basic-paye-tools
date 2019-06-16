Bootstrap: debootstrap
OSVersion: stable
MirrorURL: http://ftp.us.debian.org/debian
# Note that for singularity 3.0 this becomes Bootstrap: library
# see https://www.sylabs.io/2018/09/new-containers-apache-mariadb-blender/
 

%help
    Container with MariaDB for Debian 9.x (Stretch).

%setup
    # none needed

# copy a config file into the container
%files 
mariadb.cnf /tmp/mariadb.cnf

%post
    #mkdir /shared
    apt-get -y --allow-unauthenticated install gnupg software-properties-common
    # build-essential wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libiconv-hook1 #git
    echo '---------- getting MariaDB ---------------------'
    apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xF1656F24C74CD1D8
    add-apt-repository 'deb [arch=amd64] http://www.ftp.saix.net/DB/mariadb/repo/10.1/debian stretch main'
    apt-get update
    # could apt-get -y upgrade
    apt-get -y install mariadb-server

    rm -rf /var/lib/apt/lists/*

    apt-get clean
    mv /tmp/mariadb.cnf /etc/mysql/conf.d/mariadb.cnf
    /usr/bin/mysql_install_db --verbose --skip-name-resolve --user=`whoami` --datadir='/var/lib/mysql'
   #--basedir=/opt/mysql/mysql 
   # see https://mariadb.com/kb/en/library/mysql_install_db/ 
   # in case of trouble read /var/lib/mysql/error_log


%labels
  Maintainer_Email chris.morris@biorelate.com
  MariaDB_Version 2018.12
  
%environment
#  export ANACONDA_VERSION=2018.12
#  export PATH=/usr/local/anaconda/bin:$PATH

%apprun python
  exec python "${@}"

%apprun secure
  exec /usr/bin/mysql_secure_installation

%apprun admin
   exec /usr/bin/mysqladmin -u root -h 127.0.0.1 #--password "$@"

%apprun root
  /usr/bin/mysqld --datadir='/var/lib/mysql'   #--password

%apprun csv
  exec mysql --user=root --batch --column-names --default-character-set=utf8 -h 127.0.0.1 #--password

%apprun xml
  exec mysql --user=root --xml --default-character-set=utf8 #--password

%runscript
  exec "mysqld" "$@"
  
%startscript
  /usr/bin/mysqld --datadir='/var/lib/mysql' 
  # --flush-caches --skip-syslog  

%help


%test
