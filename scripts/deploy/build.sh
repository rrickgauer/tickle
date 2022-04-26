
# DIRECTORY_HOME='/var/www/tickle'
# DIRECTORY_GUI_STATIC='/var/www/tickle/src/tickle/gui/static'
# DIRECTORY_APACHE_SITES_AVAILABLE='/etc/apache2/sites-available'

# CONF_API='api.tickle.ryanrickgauer.com.conf'
# CONF_GUI='tickle.ryanrickgauer.com.conf'

# Pull down any changes from git
echo 'Fetching new source code from GitHub...'
./.get-latest.sh

# Pull down any changes from git
echo 'Setting the bash file permissions...'
./.set-permissions.sh


# Build the static js and css files
echo 'Building the static files...'
./.build-static-files.sh


# Refresh the apache .conf files
echo 'Refreshing the apache configuration files...'
./.refresh-apache-conf-files.sh



