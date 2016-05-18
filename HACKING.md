# Introduction
This documentation refers to the installation and configuration of a MySQL and an 
Apache WebServer in two different docker. Also, we configure a monitor server inside
the docker host which collects and send docker log files to Amazon S3.


# Premisses
* S3 Amazon proper configured;
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
It will deploy two docker with MySQL and Apache web server. Also, it make a basic installation
of the Icinga.

## MySQL Remote Connection

In order to be able to connect to MySQL you should run the following commands.

```
# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                              NAMES
5afda1dcfec3        mysql               "/sbin/my_init"     8 minutes ago       Up 8 minutes        0.0.0.0:3360->3360/tcp, 3306/tcp   mysql

# docker exec -i -t 5afda1dcfec3 /bin/bash

root@5afda1dcfec3:/# mysql -p
Enter password: \<type_password\>
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 7
Server version: 5.5.49-0ubuntu0.12.04.1 (Ubuntu)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> GRANT ALL ON *.* to root@'%' IDENTIFIED BY 'root';
Query OK, 0 rows affected (0.00 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.00 sec)

mysql> quit
Bye
root@5afda1dcfec3:/# exit
exit
#
``` 

After the sequence of these commands you should be able to connect to MySQL from the host.

```
# mysql -P 3360 -u root -p -h 172.17.42.1
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 6
Server version: 5.5.49-0ubuntu0.12.04.1 (Ubuntu)

Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```


