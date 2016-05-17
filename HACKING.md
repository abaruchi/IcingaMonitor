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
in all servers (when using Red Hat based distros).

# Installation Procedure

## Clone Git
First step is to clone our git repository into any directory. For instance, we 
are going to use centos home.

```
$ cd ~centos
$ git clone https://github.com/abaruchi/IcingaMonitor.git
```

## Ansible Ping Test
Before start with the installation procedure, please, run the following command to 
test ansible connection between hosts (amazon and localhost).

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

