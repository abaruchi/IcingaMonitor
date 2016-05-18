# Introduction
This documentation refers to the installation and configuration of a MySQL and an 
Apache WebServer in two different docker. Also, we configure a monitor server inside
the docker host which collects and send docker log files to a VM installed at Amazon.


# Premisses
* VM installed at Amazon AWS with a [Elastic-IP](http://docs.aws.amazon.com/AmazonVPC/latest/GettingStartedGuide/getting-started-assign-eip.html);
* VMs are communicating and ssh pub key authentication are [configured](https://macnugget.org/projects/publickeys/);
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
test ansible connection between hosts (amazon and localhost).
Please, remember to update the file `Ansible/hosts` with the proper IP or Hostnames.

```
# pwd
/root/IcingaMonitor/Ansible

# ansible all -m ping

localhost | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
ec2-52-203-154-4.compute-1.amazonaws.com | SUCCESS => {
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
of the Icinga 



