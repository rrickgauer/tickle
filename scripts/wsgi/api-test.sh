mod_wsgi-express start-server \
--user www-data  \
--group www-data  \
--server-name api.tickle.ryanrickgauer.com  \
--port 5010   \
--access-log  \
--log-level info   \
--log-to-terminal \
--python-path /var/www/tickle/src \
--host 104.225.208.163 \
--server-root /etc/api.tickle.ryanrickgauer.com \
/var/www/tickle/src/tickle_api.wsgi
