#coding=utf-8
import time

class Time:
	def __init__(self, t):
		self.unixTime=int(t)
		self.startTime=1679353200
		self.unixCurTime=self.unixTime-self.startTime
		self.greg=[]

	def calculateGreg(self):
		modulatedtime=self.unixCurTime
		print(modulatedtime)
		seconds = modulatedtime%60
		modulatedtime=(modulatedtime-seconds)/60
		print(modulatedtime)
		minutes = modulatedtime%60
		modulatedtime=(modulatedtime-minutes)/60
		print(modulatedtime)
		hour = modulatedtime%24
		modulatedtime=(modulatedtime-hour)/24
		print(modulatedtime)
		days = modulatedtime%365.25
		modulatedtime=(modulatedtime-days)/365.25
		years=modulatedtime
		self.greg=[years, days, hour, minutes, seconds]

	def calculateRel(self):
		# [int_years, str_month, int_days, int_hour, str_moment, int_min, str_quadrant, int_sec]
		int_years=self.greg[0]
		int_month=0
		int_days=round(self.greg[1])
		if int_days>45:
			int_month+=1
			int_days-=45
		if int_days>45:
			int_month+=1
			int_days-=45
		if int_days>45:
			int_month+=1
			int_days-=45
		if int_days>45:
			int_month+=1
			int_days-=45
		if int_days>45:
			int_month+=1
			int_days-=45
		if int_days>44:
			int_month+=1
			int_days-=44
		if int_days>46:
			int_month+=1
			int_days-=46

		if int_month==0:
			str_month="Eau"
		elif int_month==1:
			str_month="Terre"
		elif int_month==2:
			str_month="Soleil"
		elif int_month==3:
			str_month="Feu"
		elif int_month==4:
			str_month="Air"
		elif int_month==5:
			str_month="Temps"
		elif int_month==6:
			str_month="Lune"
		else:
			str_month="Vide"

		if self.greg[2]>=6 and self.greg[2]<12:
			str_moment = "Matin"
			int_hours = self.greg[2]-6
		elif self.greg[2]>=12 and self.greg[2]<18:
			str_moment = "Apres-midi"
			int_hours = self.greg[2]-12
		elif self.greg[2]>=18 and self.greg[2]<24:
			str_moment = "Soir"
			int_hours = self.greg[2]-18
		else:
			str_moment = "Nuit"
			int_hours = self.greg[2]

		if self.greg[3]>=0 and self.greg[3]<15:
			str_quadrant="apres l'heure"
			int_min=self.greg[3]
		elif self.greg[3]>=15 and self.greg[3]<30:
			str_quadrant="apres le quart"
			int_min=self.greg[3]-15
		elif self.greg[3]>=30 and self.greg[3]<45:
			str_quadrant="apres la demi"
			int_min=self.greg[3]-30
		else:
			str_quadrant="apres le trois quart"
			int_min=self.greg[3]-45

		int_sec=self.greg[4]

		self.rel=[int_years, int_days, str_month, int_hours, str_moment, str_quadrant, int_min, int_sec]


now=Time(time.time())
now.calculateGreg()
print(now.greg)
now.calculateRel()
print(now.rel)