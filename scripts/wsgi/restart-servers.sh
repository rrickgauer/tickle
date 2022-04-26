#!/bin/bash

IP_ADDRESS='104.225.208.163'
PORT_API='5010'
PORT_GUI='5011'
APPLICATION_SOURCE_DIRECTORY='/var/www/tickle/src'

#---------------------------------------
# Start up the API
#---------------------------------------
echo 'Starting up API server...'

cd $APPLICATION_SOURCE_DIRECTORY

mod_wsgi-express setup-server \
--user www-data  \
--group www-data  \
--server-name api.tickle.ryanrickgauer.com  \
--port $PORT_API   \
--access-log  \
--log-level info   \
--server-root /etc/api.tickle.ryanrickgauer.com \
--host $IP_ADDRESS \
--setup-only \
--python-path $APPLICATION_SOURCE_DIRECTORY \
tickle_api.wsgi

# restart the server
/etc/api.tickle.ryanrickgauer.com/apachectl restart


echo ''


#---------------------------------------
# Start up the gui
#---------------------------------------

echo 'Starting up front-end server...'

mod_wsgi-express setup-server \
--user www-data  \
--group www-data  \
--server-name tickle.ryanrickgauer.com  \
--port $PORT_GUI \
--access-log  \
--log-level info   \
--server-root /etc/tickle.ryanrickgauer.com \
--host $IP_ADDRESS \
--setup-only \
--document-root /var/www/tickle/src/tickle/gui/static \
--python-path $APPLICATION_SOURCE_DIRECTORY \
tickle_gui.wsgi

# restart the server
/etc/tickle.ryanrickgauer.com/apachectl restart


