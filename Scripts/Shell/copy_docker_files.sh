#!/bin/bash

MYSQL_LOG_DIR="/var/log/mysql"
HTTPD_LOG_DIR="/var/log/httpd"
LOCAL_DIR="/var/tmp/docker_logs"

# MySQL Docker ID
mysql_id=`docker ps | grep mysql | awk '{print $1}'`

# HTTPD Docker ID
httpd_id=`docker ps | grep httpd | awk '{print $1}'`

# Remove Old Structures
rm -rf $LOCAL_DIR/

# Creates http LogDir
mkdir -p $LOCAL_DIR/httpd/

# Creates mysql LogDir
mkdir -p $LOCAL_DIR/mysql/

# Copy mysql files from docker to host
docker cp $mysql_id:$MYSQL_LOG_DIR $LOCAL_DIR/mysql/

# Copy http files from docker to host
docker cp $httpd_id:$HTTPD_LOG_DIR  $LOCAL_DIR/httpd/

# Compress LogFiles to send to S3
tar czvf /tmp/docker_logfiles.tar.gz $LOCAL_DIR

