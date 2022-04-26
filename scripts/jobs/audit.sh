source .constants.sh


echo 'start'
echo $PATH_APPLICATION

cd $PATH_APPLICATION

python3.8 -m tickle.jobs.audit.main

echo 'end'
