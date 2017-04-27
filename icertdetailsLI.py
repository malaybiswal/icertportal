#import urllib2
# started with 800,000 ID
import datetime
from re import sub
import re
from decimal import Decimal
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
def find_word(text, search):

   result = re.findall('\\b'+search+'\\b', text, flags=re.IGNORECASE)
   print('RESULT',result,len(result))
   if len(result)>0:
      return True
      print('RETURNING TRUE','********************')
   else:
      return False
      print('RETURNING FALSE','********************')

company='';empAdd1='';empAdd2='';empcity='';empState='';empCountry='';empZip='';empph='';empEmail=''
attorneyLastName='';attorneyFirstName='';attorneyAdd1='';attorneyAdd2='';attorneyPhone='';attorneyCity='';attorneyState='';atorneyCountry='';attorneyZip='';attrorneyEmail=''
#print(len(board),len(board[0]))
OccupationTitle='';pwg=0;
print ('Number of arguments:', len(sys.argv), 'arguments.')

try:
	id=833838
except:
	id=1234
url1="https://lcr-pjr.doleta.gov/index.cfm?event=ehLCJRExternal.dspCert&doc_id=3&visa_class_id=6&id="

try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
url=url1+str(id)

context = ssl._create_unverified_context()
#page = urllib2.urlopen(url)
page=urlopen(url,context=context)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
all_div=soup.find('div')#, attrs={'class':'infoHolder freeTextItem'})
#print (all_div)
all_li=all_div.find_all(['li'])
#all_p=all_div.find_all('p')
print ('----------------------------------------')
for row in all_li:
	i+=1
	print (i,'...',str(row))
	

	if(i>=12 and i<=19):
		if(find_word(str(row),'alt="checked')):
			pwsource=str(row.get_text())
			print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&',str(row.get_text()))
			
	elif(i>=24 and i<=30):
		if(find_word(str(row),'alt="checked')):
			educationmin=str(row.get_text())
			print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&',str(row.get_text()))

	elif(i>=31 and i<=32):
		if(find_word(str(row),'alt="checked')):
			trainingreq=str(row.get_text())
			print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&',str(row.get_text()))

	elif(i>=37 and i<=38):
		if(find_word(str(row),'alt="checked')):
			altedu=str(row.get_text())
			print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&',str(row.get_text()))

	elif(i>=92 and i<=98):
		#if(row.find("alt=\"checked\"")!=-1):
		if(find_word(str(row),'alt="checked')):
			alienEducation=str(row.get_text())
			print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&',str(row.get_text()))