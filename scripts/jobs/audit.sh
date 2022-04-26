#!/bin/sh
cd /var/www/tickle/src
/usr/local/bin/python3.8 -m tickle.jobs.audit.main
