# Overall Objective

You are required to setup a monitoring solution using Icinga. Icinga should monitor the Apache Web Server and the Mysql Database server and send logs to Amazon S3 dynamically using Bash Scripting.

Functional Requirements

An organization runs Linux servers and requests you to setup/configure the following infrastructure:

* Download, install and configure Icinga solution on the server.

* Troubleshoot any system issues to ensure availability of services

* Install Apache web server and a Mysql Database on different Docker containers

* Ensure that all logs that are generated by the Apache Web Server and Mysql Database are collected dynamically through a Bash Script

* Those logs should be automatically sent to Amazon s3 at 7 pm daily

* Ensure proper backups are optimally taken and sent to Amazon S3 bucket as well

* Write a Chef Recipe (Puppet Manifest or Ansible Playbook) to automate this process.

# Other Technical and Non-functional Requirements

The following list of technical specifications should be adhered to

* Assume missing/unclear requirements to fill the gaps in the specifications.

* Demonstrate your Administration and scripting skills by choosing a good design.

* Plan to setup servers, install services, configure them so as to create the system from scratch.

* Choose a mix of services to use for hands-on, shell scripting, NodeJS, Python that you need to create as part of the system for an efficient design.

* The web-pages should be protected with login.

* So there are two major parts to deliver

  * A deployment manual with detailed step by step process of creating the whole system. It can include other references.

  * Scripts and code for automating the infrastructure and centralized logging
