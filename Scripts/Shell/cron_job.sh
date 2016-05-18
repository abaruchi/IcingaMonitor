#!/bin/bash

# Collects log files from Dockers
./copy_docker_files.sh
././make_backup.sh

# Send file to S3
/usr/bin/env python log_file_upload.py AKIAJLT2AZFWDHCZYIUA vi7TCLbUTbXjy4rIao7NfdVcuIEMmEA4eYRNf09G
/usr/bin/env python bkp_file_upload.py AKIAJLT2AZFWDHCZYIUA vi7TCLbUTbXjy4rIao7NfdVcuIEMmEA4eYRNf09G
