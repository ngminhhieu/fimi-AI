from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='curl localhost:8000/sensor/get_sensors/')
job.minute.every(5)
 
## The job takes place once every four hours
job.hour.every(4)
 
## The job takes place on the 4th, 5th, and 6th day of the week.
job.day.on(4, 5, 6)
cron.write("update_calibration.tab")