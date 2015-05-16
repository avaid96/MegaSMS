
import csv
# linking to csv
num=open('Numbers.csv')
csvnum=csv.reader(num)
for row in csvnum:
	print row
num.close()