Bootstrap: localimage
From: java.simg  

%help
    Container with HMRC Basic PAYE Tools

%setup
    # none needed

# copy a config file into the container
%files 
payetools.zip /payetools.zip

%post
    echo 'installing'
    apt-get -y install gnupg software-properties-common unzip
    dpkg --add-architecture i386
    apt-get update
    apt-get install -y libcomerr2:i386 libfontconfig1:i386 libfreetype6:i386 \
       libgl1-mesa-glx:i386 libgssapi-krb5-2:i386 libk5crypto3:i386 libkrb5-3:i386 \
       libreadline5:i386 libsqlite3-0:i386 libstdc++6:i386 libx11-6:i386 \
       libxext6:i386 libxrender1:i386 zlib1g:i386 libxslt1.1:i386 libxml2:i386

    rm -rf /var/lib/apt/lists/*
        rm -rf /var/lib/apt/lists/*
    unzip /payetools.zip 

%labels
  Maintainer_Email chris.morris@acm.org
  
%environment
export QT_X11_NO_MITSHM=1

%apprun install
   exec /payetools/payetools-rti-19.0.19063.1355-linux –mode text

%runscript
  exec /payetools/payetools-rti-19.0.19063.1355-linux
  
%startscript
  exec /opt/HMRC/payetools-rti/rti.linux

%test
