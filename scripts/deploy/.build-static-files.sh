#****************************************************************************
#
# Build the static js and css files
#
#****************************************************************************

source .build-variables.sh

# css
cd $DIRECTORY_GUI_STATIC/css
sass style.scss style.css

# JavaScript
cd $DIRECTORY_GUI_STATIC/js
rollup -c rollup.config.js