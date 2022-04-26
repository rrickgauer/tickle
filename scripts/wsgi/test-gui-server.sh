mod_wsgi-express start-server \
--user www-data  \
--group www-data  \
--server-name tickle.ryanrickgauer.com  \
--port 5011   \
--access-log  \
--log-level info   \
--server-root /etc/tickle.ryanrickgauer.com \
--host 104.225.208.163 \
--log-to-terminal \
--python-path /var/www/tickle/src \
/var/www/tickle/src/tickle_gui.wsgi
