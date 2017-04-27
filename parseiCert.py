#import urllib2
import ssl
import sys
A=[]
s1=''
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
all_tables=soup.find('table')
print (all_tables)


print ('----------------------------------------')
for row in all_tables.findAll('tr'):
	
	s1=''
	values = row.findAll('th')

	#name = row.findall('td')
	#print(values,"---",name,"***")
	for i in values:
		print(type(i),"$$$$$$$$$$$")
		if(i.find(text=True)>'A'):
			A.append(i.find(text=True))
		else:
			strng = str(i)
			if(len(strng)>0):
				print(i,"*****",len(strng))
				for s in strng:
					strng = s1+strng.replace('\n','')
				print("###",strng)
				l = strng.split()
				A.append(l.find(text=True))
	print(values,"---")
	
print ('----------------------------------------')
print(A)

#print (all_tables)

#print (soup.prettify())
#print (all_tables)
#print(page.read())



#for row in all_tables.find_all('th'):
#	print (row)