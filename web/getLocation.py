from random import choice
import csv
import pandas
from collections import deque
from datetime import datetime

crimes = deque(maxlen=20)
schools = deque(maxlen=20)
#lsoas = deque(maxlen=20)
lsoas = []
end_vals = []

latlongs = [
	[52.4863520771, 1.7524139512],
	[52.4820583105, 1.7403722789],
    [53.7155898244, -1.6676645531],
    [53.3694336227, -2.7122767367],
    [52.5262270486, -1.9966547854],
    [55.7574785674, -2.0019467746],
    [54.1932611002,  -3.0791961468],
    [56.1224543752, -3.1427113521],
    [56.4633781494, -3.1701595478],
    [57.814049437, -4.0593344221],
    [51.7998522079, -4.3887263761]
]


def getLocation(crime = 0, education = 0):
	start = datetime.now()
	valid_lat_longs = []
	line = 0
	crime = 10 - crime
	education = 10 - education
	with open('../data/merge.csv', 'rb') as table:
		reader = csv.reader(table)
		for row in reader:
			line += 1
			if line > 1:
				lsoa = str(row[0])
				cpr = float(row[3])
				sr = float(row[1])
				education_row = ((1 + 0.1 * education) * sr)
				print "education", education_row
				crime_row = ((1 + 0.1 * crime) * cpr)
				print "crime", crime_row
				end_val = education_row + crime_row
				end_vals.append([lsoa, end_val])
		sorted_vals = sorted(end_vals, key=lambda tup: tup[1], reverse=True)
		times = 0
		wanted_vals = [sorted_vals[0],sorted_vals[1],sorted_vals[2],sorted_vals[3],sorted_vals[4]]
		for i in wanted_vals:
			print("i: ", i)
			lsoas.append(i[0])
	with open("../data/lsoas.csv", "rb") as lsoa_reference:
		reader = csv.reader(lsoa_reference)
		for row in reader:
			if row[0] in lsoas:
				print "got match for: ", row
				valid_lat_longs.append([row[1], row[2]])
	time_taken = datetime.now() - start
	print time_taken
	print "Valid lat/longs: ", len(valid_lat_longs)
#	for lat_long in valid_lat_longs:
#		print lat_long
	return valid_lat_longs

print(getLocation(crime = 5, education = 7))

def getLocationRand(crime = 0, education = 0):
	random_latlong_1 = choice(latlongs)
	random_latlong_2 = choice(latlongs)
	random_latlong_3 = choice(latlongs)
	random_latlong_4 = choice(latlongs)
	random_latlong_5 = choice(latlongs)
	return [random_latlong_1, random_latlong_2, random_latlong_3, random_latlong_4, random_latlong_5]