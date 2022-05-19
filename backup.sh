#!/bin/bash
now=$(date +"%Y%m%d")
year=$(date +"%Y")
month=$(date +"%m")
echo "Dumping postgres database..."
docker-compose exec db pg_dump postgres > /home/latona/deploy/dumps/${now}.dump
echo "Syncing with Google Drive"
rclone copy /home/latona/deploy/dumps/ gdrive:kintai_dumps/${year}/${month}/
rm /home/latona/deploy/dumps/*.dump
