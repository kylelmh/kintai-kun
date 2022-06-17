#!/bin/bash
cd /home/latona/deploy/kintai-kun
rm /home/latona/deploy/dumps/*.dump
now=$(date +"%Y%m%d")
year=$(date +"%Y")
month=$(date +"%m")
echo "Dumping postgres database..."
docker-compose exec db pg_dump postgres -F c > /home/latona/deploy/dumps/${now}.dump
echo "Syncing with Google Drive"
rclone copy /home/latona/deploy/dumps/ gdrive:kintai_dumps/${year}/${month}/
