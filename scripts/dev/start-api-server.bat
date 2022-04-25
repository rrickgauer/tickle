:: --------------------------------------------
:: Start up the api development flask server
:: --------------------------------------------

cd C:\xampp\htdocs\files\tickle\src\tickle\api

set FLASK_ENV=development
:: set FLASK_APP=tickle.api

flask run --with-threads --host 0.0.0.0 --port 5010
