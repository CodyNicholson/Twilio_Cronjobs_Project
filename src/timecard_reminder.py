import datetime
import glob
from twilio.rest import Client
from sensitive import auth_token, account_sid, cn_num, tw_num

client = Client(account_sid, auth_token)

files = [f for f in glob.glob("/home/pi/Twilio_Cronjobs_Project/logs/*.txt", recursive=True)]
log_count = str(len(files)+1)
print(f"Log: {log_count}")

now = datetime.datetime.now()
timestamp = str(now.strftime("%Y-%m-%d-%H-%M-%S"))
print(f"timestamp is: {timestamp}")

with open(f"Twilio_Cronjobs_Project/logs/log{log_count}-{timestamp}.txt","w+") as file:
	file.write("SUBMIT YOUR TIMECARD!!!\n")
	file.write(f"timestamp: {timestamp}\n")
	file.write(f"datetime: {str(now)}\n")
	file.write(f"logs: {log_count}\n")
	file.write("End Log\n\n")
	file.close()

msg_body = f"SUBMIT YOUR TIMECARD!\nLOG: {log_count}\nTIME: {timestamp}\nEND LOG."
message = client.messages.create(to=cn_num, from_=tw_num, body=msg_body)

print("DONE")
