import glob

files = [f for f in glob.glob("/home/pi/Twilio_Cronjobs_Project/logs/*.txt", recursive=True)]
log_count = str(len(files)+1)

print(log_count)

