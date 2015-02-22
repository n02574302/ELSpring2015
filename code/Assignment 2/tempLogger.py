#Temperature reading portion by Dr. Chirakkal Easwaran
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as mydb
import sys
import os
import time

def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-000006964288/w1_slave")
	tempfile_text = tempfile.read()
	currentTime = time.strftime('%x %X %Z')
	tempfile.close()
	tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	
	tempF = tempC*9.0/5.0+32.0
	con = mydb.connect('temperature.db')

	with con:
    
    		cur = con.cursor()    
   		cur.execute("INSERT INTO TempData VALUES(?, ?, ?)", (currentTime, tempC, tempF))
		con.commit();

	return tempC
print "The current temperature is", readTemp(), "degrees Celsius."
print "The current temperature has been logged."