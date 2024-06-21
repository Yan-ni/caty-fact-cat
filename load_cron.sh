#! /bin/bash

# Variables
DIR_PATH=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SCRIPT_FILE="$DIR_PATH/main.sh"
TEMP_CRON="/tmp/crontab_temp"

# Script
crontab -l > "$TEMP_CRON"
echo "# caty fact cat script"
echo "0 */6 * * * $SCRIPT_FILE" >> "$TEMP_CRON" # Every six hours
echo "0 15 * * * $SCRIPT_FILE" >> "$TEMP_CRON" # Every day at 15:00
echo "0 21 * * * $SCRIPT_FILE" >> "$TEMP_CRON" # Every day at 21:00

crontab "$TEMP_CRON"

rm "$TEMP_CRON"

service cron reload
