:: --------------------------------------------
:: Start up the api development flask server
:: --------------------------------------------

cd C:\xampp\htdocs\files\tickle\src

set flask_program=C:\xampp\htdocs\files\tickle\venv\Scripts\flask
set FLASK_ENV=development
set FLASK_APP=tickle.api

%flask_program% run --with-threads --host 0.0.0.0 --port 5010
