source .constants.sh


echo 'whats up bitch audit'

cd $PATH_APPLICATION

python3.8 -m tickle.jobs.audit.main
