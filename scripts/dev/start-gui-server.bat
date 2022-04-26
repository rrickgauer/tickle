:: --------------------------------------------
:: Start up the gui development flask server
:: --------------------------------------------

cd C:\xampp\htdocs\files\tickle\src

set FLASK_ENV=development
set FLASK_APP=tickle.gui

flask run --with-threads --host 0.0.0.0 --port 5011
