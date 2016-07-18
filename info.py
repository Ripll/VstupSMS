# -*- coding: cp1251 -*-
from grab import Grab
import time
g = Grab()
password = "***"
def TryGo(url):
   try:
      g.go(url)
   except:
      print "Error! " + url
      time.sleep(3)
      TryGo(url)

def setStartDate():
   global start_date
   TryGo("http://www.vstup.info/")
   start_date = g.doc.rex_text('<small>([^>]+)</small>')

   
def getDB():
   global phone, api_key
   TryGo("http://ripll.top/get.php?password=" + password + "&type=phone")
   phone = g.response.body.split()
   TryGo("http://ripll.top/get.php?password=" + password + "&type=api_key")
   api_key = g.response.body.split()
   
setStartDate()

while True:
   i = 0
   getDB()
   time.sleep(60)
   TryGo('http://www.vstup.info/')
   now = g.doc.rex_text('<small>([^>]+)</small>')
   print now.encode("utf-8")
   if now != start_date:     
      while i < len(phone):
           SendSmsUrl = "http://sms.ru/sms/send?api_id=" + api_key[i] + "&to=" + phone[i] + "&text=" + now
           TryGo(SendSmsUrl)
           print "Отправлено СМС на номер " + phone[i]
           i += 1
      setStartDate()
   

   
