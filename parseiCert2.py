#import urllib2
import pymysql
import ssl
import sys
flag=0
i=0
s=''
str=''
cnt=0
temp=''
board = [[0]*5 for _ in range(3)]
board[0][0]='H-1B'
board[1][0]='H-2B'
board[2][0]='PERM'

#print(len(board),len(board[0]))

try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
	
url="https://icert.doleta.gov/"
context = ssl._create_unverified_context()
#page = urllib2.urlopen(url)
page=urlopen(url,context=context)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
all_tables=soup.find_all('table')
#print (all_tables)


#print ('----------------------------------------')
for row in all_tables:
	i+=1
	
	str=row.get_text()
	#print(">>>>",str,"<<<<<<<")
	if (str.find("Average Number of Days to Issue Wage Determinations") != -1):
		#print(i,">>>>",str,"<<<<<<<")
		
		l=str.split()
	else:
		#print("NOT FOUND")
		dummy=0

#print(l)

for s in l:
	if(flag==1):
		if(tmp=='H-1B'):
			cnt+=1
			board[0][cnt]=s
			if(cnt==4):
				cnt=0
				flag=0
		elif(tmp=='H-2B'):
			cnt+=1
			board[1][cnt]=s
			if(cnt==4):
				cnt=0
				flag=0
		elif(tmp=='PERM'):
			cnt+=1
			board[2][cnt]=s
			if(cnt==4):
				cnt=0
				flag=0
	else:
		if((s=='H-1B') or (s=='H-2B') or (s=='PERM')):
			flag=1
			#print(s,"INSIDE MATCHING H-1B or H-2B or PERM")
			tmp=s
		else:
			#print("INSIDE ELSE:",s)
			dummy=0
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='misc')
sql="""INSERT INTO icert(program,Month,Year,OESDAYS,NONOESDAYS) VALUES(%s, %s, %s, %s, %s)"""
cur = conn.cursor()

for x in range(0,3):
	for y in range(0,5):
		print('board[',x,'][',y,']',board[x][y])

for x in range(0,3):
		cur.execute(sql,(board[x][0],board[x][1],board[x][2],board[x][3],board[x][4]))


conn.commit()
cur.close()
conn.close()

	

#CREATE TABLE `icert` (`created_t` DATE NOT NULL ,`program` varchar(20) NOT NULL,`Month` varchar(20) NOT NULL,`Year` varchar(6) NOT NULL,`OESDAYS` int(4) NOT NULL,`NONOESDAYS` int(4) NOT NULL,UNIQUE KEY `ind1` (`created_t`,`program`));
#create trigger `role_date_created` before insert     on `icert`     for each row      set new.`created_t` = now();