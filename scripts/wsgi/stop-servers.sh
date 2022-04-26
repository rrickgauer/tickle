# This script stops both list servers that are running in the background.

echo 'Stopping api...'
/etc/api.tickle.ryanrickgauer.com/apachectl stop

echo 'Stopping gui...'
/etc/tickle.ryanrickgauer.com/apachectl stop