# s3_backups
This project houses a script called by cron for backing up a few folders to an s3 bucket


To use, clone the git repository and copy the included crontab file into your crontab directory. Ensure that you edit the corntab file to reflect the folder you cloned into.

Next, edit the configuration file included in the repo

key= The access key recieved from AWS
secret= The secret access key recieved from AWS
folders= a comma separated list of folders that contain files you wish to have backed up
bucket=  the name of the s3 bucket you created.

Now you're done!
