#import urllib2
import pymysql
import ssl
import sys
flag=0
i=0
s=''
strng=''
values=''
cnt=0
temp=''

company='';empAdd1='';empAdd2='';empcity='';empState='';empCountry='';empZip='';empph='';empEmail=''
attorneyLastName='';attorneyFirstName='';attorneyAdd1='';attorneyAdd2='';attorneyPhone='';attorneyCity='';attorneyState='';atorneyCountry='';attorneyZip='';attrorneyEmail=''
#print(len(board),len(board[0]))

try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
	
url="https://lcr-pjr.doleta.gov/index.cfm?event=ehLCJRExternal.dspCert&doc_id=3&visa_class_id=6&id=1009499"
context = ssl._create_unverified_context()
#page = urllib2.urlopen(url)
page=urlopen(url,context=context)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
all_div=soup.find('div')#, attrs={'class':'infoHolder freeTextItem'})
#print (all_div)
all_h5_p=all_div.find_all(['h5','p'])
#all_p=all_div.find_all('p')
print ('----------------------------------------')
for row in all_h5_p:
	i+=1
	values=values+str(row.get_text())
	values=values+'-----'
	#strng=row.get_text()
	#print(str)
#print(values)
i=0;j=0;k=0
valueslist = values.split("-----")	
print(len(valueslist))
print(valueslist)

for l in valueslist:
	cnt+=1;
	if(l=='1. Employer\'s name'):
		company = valueslist[cnt]
	elif(l=='2. Address 1'):
		i=i+1
		
		if(i==1):
			print(i,'*************INSIDE ADD1')
			empAdd1= valueslist[cnt].strip()
			#continue
		elif(i==3):
			print(i,'$$$$$$$$$$$INSIDE ADD1')
			attorneyAdd1= valueslist[cnt].strip()
		print('**',empAdd1,'--',i)
		#i=0
	elif(l=='Address 2'):
		j=j+1
		if(j==1):
			print(i,'*************INSIDE ADD2')
			empAdd2 = valueslist[cnt].strip()
		elif(j==3):
			print(i,'$$$$$$$$$$$INSIDE ADD2')
			print(i,'%%%%%%%%%%%%%%')
			attorneyAdd2 = valueslist[cnt].strip()

		print('>>',empAdd2,'--',i)
		#i=0
	elif(l=='3. City'):
		empCity= valueslist[cnt].strip()
	elif(l=='State/Province'):
		empState= valueslist[cnt].strip()
	elif(l=='Country'):
		empCountry= valueslist[cnt].strip()
	elif(l=='Postal Code'):
		empZip= valueslist[cnt].strip()
	elif(l=='4. Phone Number'):
		k=k+1
		if(k==1):
			#print(i,'*************')
			empph= valueslist[cnt].strip()
			#i=0
			#continue
			print('>>>',empph)
print('COMPANY:',company,'ADD1:',empAdd1,'ADD2:',empAdd2,'CITY:',empCity,'STATE:',empState,'COUNTRY:',empCountry,'ZIP:',empZip,'PH:',empph)
print('ATTORNEYADD1:',attorneyAdd1,'ATTORNEYADD2:',attorneyAdd2)


		



	
