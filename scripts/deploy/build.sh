
#****************************************************************************
#
# Pull down any changes from GitHub and deploy the application
#
#****************************************************************************

source .build-variables.sh

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


# Restart the servers
echo '\nRestart the servers...'
cd $DIRECTORY_HOME/wsgi
./restart-servers.sh
