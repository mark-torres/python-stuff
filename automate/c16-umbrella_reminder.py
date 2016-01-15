#!/usr/bin/env python3

import json, requests, urllib, smtplib
from email.mime.text import MIMEText

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='Morelia, Mexico')"
yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
result = requests.get(yql_url)
data = json.loads(result.text)

subject = data['query']['results']['channel']['description']
link = data['query']['results']['channel']['link']
sunrise = data['query']['results']['channel']['astronomy']['sunrise']
sunset = data['query']['results']['channel']['astronomy']['sunset']
condition = data['query']['results']['channel']['item']['condition']['text']
temp = float(data['query']['results']['channel']['item']['condition']['temp'])
temp = (temp - 32) / 1.8
temp = round(temp, 2)

forecast = data['query']['results']['channel']['item']['forecast']
texts = []
for i,day in enumerate(forecast):
	maxTemp = (float(day['high']) - 32) / 1.8
	minTemp = (float(day['low']) - 32) / 1.8
	text = "%s %s: %s (Max %s, Min %s)" % (day['day'], day['date'], day['text'], round(maxTemp, 2), round(minTemp, 2))
	texts.append(text)

lines = []
lines.append("CURRENT CONDITIONS")
lines.append("")
lines.append("Weather: %s" % condition)
lines.append("Temp: %s" % temp)
lines.append("Sunrise: %s" % sunrise)
lines.append("Sunset: %s" % sunset)
lines.append("")
lines.append("FORECAST")
lines.append("")
lines += texts

text = "\n".join(lines)

smtpServer = "smtp.mail.yahoo.com"
smtpPort = 587
smtpUser = "some@yahoo.com"
smtpPass = ""

yahoo = smtplib.SMTP(smtpServer, smtpPort)
yahoo.ehlo()
yahoo.starttls()
yahoo.login(smtpUser, smtpPass)

msg = MIMEText(text)
msg['Subject'] = subject
msg['From'] = "Mark Torres <%s>" % smtpUser
msg['To'] = "some@gmail.com"
yahoo.send_message(msg)
yahoo.quit()
