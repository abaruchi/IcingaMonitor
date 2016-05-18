#!/bin/bash

MYSQL_LOG_DIR="/var/log/mysql"
LOCAL_DIR="/var/tmp/docker_logs"

# Remove Old Structures
rm -rf $LOCAL_DIR/

# Creates http LogDir
mkdir -p $LOCAL_DIR/httpd/

# Creates mysql LogDir
mkdir -p $LOCAL_DIR/mysql/

# Copy mysql files from docker to host
docker cp mysql:$MYSQL_LOG_DIR $LOCAL_DIR/mysql/


# Compress LogFiles to send to S3
tar czvf /tmp/docker_logfiles.tar.gz $LOCAL_DIR

