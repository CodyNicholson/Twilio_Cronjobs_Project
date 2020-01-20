# Scheduling Cronjobs

Cronjobs are scheduled commands that your unix-based system will run at the specified cron time. For example:

```
* * * * * /path/to/script.sh
```

If your crontab file had this written inside it then every minute your computer would try to run "script.sh" found in the "/path/to/" driectory. The five "*"'s at the beginning indicate the time to run the script. To learn more about how that time format works see: https://crontab.guru/

To get to your crontab file where you can schedule your cronjobs, use this command in your terminal to open your crontab file in nano:

```
crontab -e
```

Another useful command is:

```
crontab -l
```

This will list all of your scheduled cronjobs without you needing to open the crontab file.
