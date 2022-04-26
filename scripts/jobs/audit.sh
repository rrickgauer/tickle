#!/bin/sh
cd /var/www/tickle/src/tickle/jobs
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
#python -m /var/www/tickle/scripts/jobs.py
python3.8 -m tickle.jobs.audit.main
