import smtplib
import pandas as pd

#load the xlsx file and sheet number
df=pd.read_excel("Book1.xlsx", "Sheet1",index_col=None)


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
#enter senders id and app password
server.login('enter your email','enter your app password')
#appropriate subject
subject='your subject'
#body of the mail
body='your body'
msg = f"Subject: {subject}\n\n{body}"
for i in df["mail Ids"]:
	server.sendmail('sender's email id, i ,msg)
	print(f" mail to {i} successfull")
server.quit()
	