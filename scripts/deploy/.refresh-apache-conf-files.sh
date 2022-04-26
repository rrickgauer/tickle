#****************************************************************************
#
# Refresh the apache .conf files
#
#****************************************************************************

source .build-variables.sh

cd $DIRECTORY_APACHE_SITES_AVAILABLE

# remove the files from the enabled sites
a2dissite $CONF_API
a2dissite $CONF_GUI


# remove the symbolic links
rm $CONF_API
rm $CONF_GUI

# create new symbolic links
ln -s /var/www/tickle/apache/tickle.ryanrickgauer.com.conf
ln -s /var/www/tickle/apache/api.tickle.ryanrickgauer.com.conf

# add the files to enabled sites
a2ensite $CONF_API
a2ensite $CONF_GUI

# restart the apache
systemctl reload apache2