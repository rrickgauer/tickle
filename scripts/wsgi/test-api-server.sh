mod_wsgi-express start-server \
--user www-data  \
--group www-data  \
--server-name api.tickle.ryanrickgauer.com  \
--port 5010   \
--access-log  \
--log-level info   \
--server-root /etc/api.tickle.ryanrickgauer.com \
--host 104.225.208.163 \
--log-to-terminal \
--document-root /var/www/tickle/src/tickle/api/static \
/var/www/tickle/src/tickle_api.wsgi