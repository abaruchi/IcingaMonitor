# Table of Contents

1. [Introduction](#introduction)
2. [Premisses](#premisses)
3. [Installation Procedure](#installation-procedure)
  1. [Clone Git](#clone-git)
  2. [Ansible Ping Test](#ansible-ping-test)
  3. [Running Ansible](#running-ansible)
  4. [MySQL Remote Connection](#mysql-remote-connection)
  5. [Icinga Database](#icinga-database)
  6. [Icinga Plugins](#icinga-plugins) 
  7. [Starting Icinga Daemon](#starting-icinga-daemon)

# Introduction
This documentation refers to the installation and configuration of a MySQL and an 
Apache WebServer in two different docker. Also, we configure a monitor server inside
the docker host which collects and send docker log files to Amazon S3.


# Premisses
* S3 Amazon proper configured (with a valid Access Key);
* Ansible is already [installed](http://docs.ansible.com/ansible/intro_installation.html) in all VMs and the user centos (with sudo privilegies) are
configured;
* EPEL repository [installed](https://support.rackspace.com/how-to/install-epel-and-additional-repositories-on-centos-and-red-hat/) 
in all servers (when using Red Hat based distros);
* RPMForge repository [installed](https://wiki.centos.org/AdditionalResources/Repositories/RPMForge) in all servers (when using Red Hat based distros);

# Installation Procedure

## Clone Git
First step is to clone our git repository into any directory. For instance, we 
are going to use root home directory.

```
$ cd ~root/
$ git clone https://github.com/abaruchi/IcingaMonitor.git
```

## Ansible Ping Test
Before start with the installation procedure, please, run the following command to 
test ansible connection.

```
# pwd
/root/IcingaMonitor/Ansible

# ansible all -m ping

localhost | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

## Running Ansible

Once you clone the git repository and all hosts are reachable, run the playbook as following:

```
# ansible-playbook -v configure_playbook.yml
```
This ansible script performs the following tasks:

* Run some local configurations:
  * User creation with root privilegies;
  * SSH Configuration;
  * DNS and Timezone Configuration;
  * Packages and Libs Installation;
  * Clone this GIT repository.
* Install two dockers (one running httpd and the other one running MySQL);
* Prepare Icinga daemon;
* Install cron entries.

## MySQL Remote Connection

In order to be able to connect to MySQL you should run the following commands.

```
# docker exec -i -t mydb /bin/bash

root@5afda1dcfec3:/# mysql -p

Enter password: <type_password>
mysql> GRANT ALL ON *.* to root@'%' IDENTIFIED BY 'root';
mysql> FLUSH PRIVILEGES;
mysql> quit
root@5afda1dcfec3:/# exit
exit
#
``` 

After the sequence of these commands you should be able to connect to MySQL from the host.

```
# mysql -P 3360 -u root -p -h 172.17.42.1
Enter password:

mysql>
```

## Icinga Database

Following commands will create the icinga database and all tables necessary to it. 

```
# docker exec -i -t mydb /bin/bash

# cd /etc/mysql
# mysql -proot -uroot < icinga.sql
# mysql -Dicinga -proot -uroot < icinga_schema.sql
```

## Icinga Plugins

Our ansible playbook downloads the tar package of plugins inside /tmp. To install it run 
the following commands:

```
# cd /tmp/
# tar xzvf monitoring-plugins-2.1.2.tar.gz ; cd monitoring-plugins-2.1.2/
# ./configure --prefix=/tmp/ && make && make install 
# cd /tmp/libexec
# find . -print | cpio -dumpv /usr/lib64/nagios/plugins
```

## Starting Icinga Daemon

Our ansible playbook creates two configuration files and put it inside `/etc/icinga/objects`. These
files are configured to provide basic monitoring for the apache and mysql (use `check_http` and 
`check_mysql` plugins).

```
# icinga -d /etc/icinga/icinga.cfg
```

To test the Daemon run the following command:

```
# icinga --show-scheduling /etc/icinga/icinga.cfg
```



