#!/bin/bash

BKP_PATH="/tmp"

# Remove OLD backups
rm -rf $BKP_PATH/icinga_backup.sql

# Make a New Backup
docker run --rm --link mydb:mydb -v $BKP_PATH:/backup mysql sh -c 'mysqldump -uroot -proot -P3306 -hmydb icinga > backup/icinga_backup.sql'