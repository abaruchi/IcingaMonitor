#!/bin/bash

# Collects log files from Dockers
/root/copy_docker_files.sh
/root/make_backup.sh

# Send file to S3
/usr/bin/env python /root/log_file_upload.py AKIAJLT2AZFWDHCZYIUA vi7TCLbUTbXjy4rIao7NfdVcuIEMmEA4eYRNf09G
/usr/bin/env python /root/bkp_file_upload.py AKIAJLT2AZFWDHCZYIUA vi7TCLbUTbXjy4rIao7NfdVcuIEMmEA4eYRNf09G
