from bs4 import BeautifulSoup
import requests
import sys
import MySQLdb

url = "http://new.showrss.info/browse/{number}".format(number=sys.argv[1])
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data,'html.parser')

X=[]
Y=[]


for info in soup.find_all("a", class_="hd"): #picking only HD prints (LOL!)
	show_title = info.get('title')
	show_magnet = info.get('href')	
	X.append(show_title)
	Y.append(show_magnet)

#creating text file with some specific manner

file=open("{number}.txt".format(number=sys.argv[1]),"w")
for index in range(len(X)):
	file.write(str(X[index]) + "\t" + str(Y[index]) + "\n")
file.close()

#Creating table in some specific database

table_name = "a{number}".format(number=sys.argv[1])
db = MySQLdb.connect(host="localhost",user="projectuser",passwd="ankitldrpceb",db="newuserdata")
cursor = db.cursor()
sql = """CREATE TABLE IF NOT EXISTS %s (Name VARCHAR(255) NOT NULL, Magnet_link VARCHAR(255))""" %table_name
cursor.execute(sql)
db.close()

