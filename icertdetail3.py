#import urllib2
import datetime
from re import sub
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

company='';empAdd1='';empAdd2='';empcity='';empState='';empCountry='';empZip='';empph='';empEmail=''
attorneyLastName='';attorneyFirstName='';attorneyAdd1='';attorneyAdd2='';attorneyPhone='';attorneyCity='';attorneyState='';atorneyCountry='';attorneyZip='';attrorneyEmail=''
#print(len(board),len(board[0]))
OccupationTitle='';pwg=0;

id=1;
url1="https://lcr-pjr.doleta.gov/index.cfm?event=ehLCJRExternal.dspCert&doc_id=3&visa_class_id=6&id="
for x in range(800000,2000000):
	try:
		from urllib.request import urlopen
	except ImportError:
		from urllib2 import urlopen
	url=url1+str(x)

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
#print(len(valueslist))
#print(valueslist)

	for l in valueslist:
		cnt+=1
		print(cnt,'--',l)
	print(url)
	company=valueslist[11]
	empAdd1=valueslist[13]
	empAdd2=valueslist[15]
	empcity=valueslist[17]
	empState=valueslist[19]
	empCountry=valueslist[21]
	empZip=valueslist[23]
	employerph=valueslist[25]
	empEmail=valueslist[27]
	try:
		numEmployees=int(valueslist[29])
		empYr=int(valueslist[31])
	except:
		numEmployees=0
		empYr=0
	#empYr=int(valueslist[31])
	print('----COMPANY-----',company,empAdd1,empAdd2,empcity,empState,empCountry,empZip,employerph,empEmail,numEmployees,empYr)

	empLastName=valueslist[39]
	empFirstName=valueslist[41]
	empPhone=valueslist[57]
	empEmail=valueslist[59]
	print('----ADV-----',empLastName,empFirstName,empPhone,empEmail)

	attorneyLastName=valueslist[61]
	attorneyFirstName=valueslist[63]
	attorneyPhone=valueslist[71]
	attorneyAdd1=valueslist[75]
	attorneyAdd2=valueslist[77]
	attorneyCity=valueslist[79]
	attorneyState=valueslist[81]
	attorneyCountry=valueslist[83]
	attorneyZip=valueslist[85]
	attorneyEmail=valueslist[87]

	print('----ATTORNEY-----',attorneyLastName,attorneyFirstName,attorneyPhone,attorneyAdd1,attorneyAdd2,attorneyCity,attorneyState,attorneyCountry,attorneyZip,attorneyEmail)

	pwgtracking=valueslist[89]
	OccupationTitle=valueslist[93]
	skillLevel=valueslist[95]
	pwg=valueslist[97]
	pwgvalue = Decimal(sub(r'[^\d.]', '', pwg))
	pwgDeterminationDt=valueslist[105].strip()
	try:
		pwgDeterminationDate = datetime.datetime.strptime(pwgDeterminationDt, '%m/%d/%Y')
	except:
		pwgDeterminationDate='1900-01-01 00:00:00'
	pwgExpirationDt=valueslist[105].strip()
	try:
		pwgExpirationDate=datetime.datetime.strptime(pwgExpirationDt, '%m/%d/%Y')
	except:
		pwgExpirationDate='1900-01-01 00:00:00'
	ow=valueslist[109]
	offeredWage=ow.split()
	print(offeredWage)
	owFrom=offeredWage[1]+offeredWage[2];owTo=offeredWage[4]+offeredWage[5]
	owFromValue = Decimal(sub(r'[^\d.]', '', owFrom))
	try:
		owToValue = Decimal(sub(r'[^\d.]', '', owTo))
	except:
		owToValue= 0.0
	print('-----PWG----',pwgtracking,OccupationTitle,skillLevel,pwgvalue,pwgDeterminationDate,pwgExpirationDate,owFromValue,owToValue)

	workAdd1=valueslist[113]
	workAdd2=valueslist[115]	
	workCity=valueslist[117]
	workState=valueslist[119]
	workZip=valueslist[121]
	jobTitle=valueslist[123]
	majorField=valueslist[129]
	try:
		numyrexp=int(valueslist[151])
	except:
		numyrexp=0
	print('-----WORK----',workAdd1,workAdd2,workCity,workState,workZip,jobTitle,majorField,numyrexp)

	jobDuties=valueslist[161]
	jobDuties=jobDuties.replace('%','percentage')
	specificSkill=valueslist[167]
	specificSkill=specificSkill.replace('%','percentage')
	print(jobDuties,'------------------------',specificSkill)

	swaStartdt=valueslist[193].strip()
	try:
		swaStartDt=datetime.datetime.strptime(swaStartdt, '%m/%d/%Y')
	except:
		swaStartDt='1900-01-01 00:00:00'
	swaEnddt=valueslist[195].strip()
	try:
		swaEndDt=datetime.datetime.strptime(swaEnddt, '%m/%d/%Y')
	except:
		swaEndDt='1900-01-01 00:00:00'
	newspaper=valueslist[199]
	print('%%%%%%%%%%%%%%%%%%',valueslist[201].strip(),valueslist[206].strip())
	try:
		advDateFirst=datetime.datetime.strptime(valueslist[201].strip(), '%m/%d/%Y') 
	except:
		advDateFirst='1900-01-01 00:00:00'
	try:
		advDateSecond=datetime.datetime.strptime(valueslist[206].strip(), '%m/%d/%Y')  
	except:
		advDateSecond='1900-01-01 00:00:00'
	ewdtfrom=valueslist[212]
	empWebSitePostDate=ewdtfrom.split()
	print('DEBUG::::',empWebSitePostDate[1].strip(),empWebSitePostDate[3].strip())
	try:
		empWebSitePostDateFrom=datetime.datetime.strptime(empWebSitePostDate[1].strip(), '%m/%d/%Y') 
	except:
		empWebSitePostDateFrom='1900-01-01 00:00:00'
	try:
		empWebSitePostDateTo=datetime.datetime.strptime(empWebSitePostDate[3].strip(), '%m/%d/%Y') 
	except:
		empWebSitePostDateTo='1900-01-01 00:00:00'
	jobsearch=valueslist[216]
	jobsearchwebsite=jobsearch.split()
	try:
		jobSearchWebSiteFrom=datetime.datetime.strptime(jobsearchwebsite[1].strip(), '%m/%d/%Y')
	except:
		 jobSearchWebSiteFrom='1900-01-01 00:00:00'
	try:
		jobSearchWebSiteTo=datetime.datetime.strptime(jobsearchwebsite[3].strip(), '%m/%d/%Y') 
	except:
		jobSearchWebSiteTo='1900-01-01 00:00:00'

	localnews=valueslist[224]
	localnewspaperdate=localnews.split()
	try:
		localNewsPaperDateFrom=datetime.datetime.strptime(localnewspaperdate[1].strip(), '%m/%d/%Y') 
	except:
		localNewsPaperDateFrom='1900-01-01 00:00:00'
	try:
		localNewsPaperDateTo=datetime.datetime.strptime(localnewspaperdate[3].strip(), '%m/%d/%Y') 
	except:
		localNewsPaperDateTo='1900-01-01 00:00:00'
	print('---------SWA----------',swaStartDt,swaEndDt,newspaper,jobSearchWebSiteFrom,jobSearchWebSiteTo,advDateFirst,advDateSecond,empWebSitePostDateFrom,empWebSitePostDateTo,localNewsPaperDateFrom,localNewsPaperDateTo)



	alienCity=valueslist[250]
	alienState=valueslist[252]
	alienCountry=valueslist[254]
	alienZip=valueslist[256]
	aliencitizenshipcountry=valueslist[260]
	aliencountryofbirth=valueslist[262]
	alienclassofadmission=valueslist[266]
#alieneducation=
	alienmajor=valueslist[276]
	print('------ALIEN--------',alienCity,alienState,alienCountry,alienZip,aliencitizenshipcountry,aliencountryofbirth,alienclassofadmission,alienmajor)
	print('^^^^^^^^^^^^^^^^^^^',alienmajor,'-',valueslist[277],'-',valueslist[278],'-',valueslist[279])
	try:
		alieneducompletedyr=int(valueslist[278].strip())
	except:
		alieneducompletedyr=0
	aliencollege=valueslist[280]
	alienuniversityadd1=valueslist[282]
	alienuniversityadd2=valueslist[284]
	alienuniversitycity=valueslist[286]
	alienuniversityState=valueslist[288]
	alienuniversitycountry=valueslist[290]
	alienuniversityzip=valueslist[292]

	print('------ALIEN2--------',alieneducompletedyr,aliencollege,alienuniversityadd1,alienuniversityadd2,alienuniversitycity,alienuniversityState,alienuniversitycountry,alienuniversityzip)
	print(type(numEmployees))
	print(id,company,empAdd1,empAdd2,empcity,empState,empCountry,empZip,employerph,numEmployees,empYr,empLastName,empFirstName,empPhone,empEmail,attorneyLastName,attorneyFirstName,attorneyPhone,attorneyAdd1,attorneyAdd2,attorneyCity,attorneyState,attorneyCountry,attorneyZip,attorneyEmail,pwgtracking,OccupationTitle,skillLevel,pwgvalue,pwgDeterminationDate,pwgExpirationDate,owFromValue,owToValue,workAdd1,workAdd2,workCity,workState,workZip,jobTitle,majorField,numyrexp,jobDuties,specificSkill,swaStartDt,swaEndDt,newspaper,advDateFirst,advDateSecond,empWebSitePostDateFrom,empWebSitePostDateTo,jobSearchWebSiteFrom,jobSearchWebSiteTo,localNewsPaperDateFrom,localNewsPaperDateTo,alienCity,alienState,alienCountry,alienZip,aliencitizenshipcountry,aliencountryofbirth,alienclassofadmission,alienmajor,alieneducompletedyr,aliencollege,alienuniversityadd1,alienuniversityadd2,alienuniversitycity,alienuniversityState,alienuniversitycountry,alienuniversityzip)
	
	conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='misc',use_unicode=True, charset="utf8")
#conn.set_character_set('utf8')
	sql="""INSERT INTO icertdata(id,employer,empadd1,empadd2,empcity,empstate,empcountry,empzipcode,employerphone,empnumemployees,empyr,emplastname,empfirstname,empphone,empemail,attorneylastname,attorneyfirstname,attorneyphone,attorneyadd1,attorneyadd2,attorneycity,attorneystate,attorneycountry,attorneyzip,attorneyemail,PWnum,occupation,skilllevel,prevailingwage,determinationdate,expirationdate,OfferedWageFrom,offeredwageto,workadd1,workadd2,workcity,workstate,workzip,jobtitle,major,numyrexperience,jobduties,specificskill,SWAstartdate,SWAenddate,newspaper,advdatefirst,advdatesecond,empwebsitepostdatefrom,empwebsitepostdateto,jobsearchwebsitefrom,jobsearchwebsiteto,localnewspaperdatefrom,localnewspaperdateto,aliencity,alienstate,aliencountry,alienzip,aliencitizenshipcountry,aliencountryofbirth,alienclassofadmission,alienmajor,alieneducompletedyr,aliencollege,alienuniversityadd1,alienuniversityadd2,alienuniversitycity,alienuniversitystate,alienuniversitycountry,alienuniversityzip) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
#sql="""INSERT INTO icertdata(empnumemployees,empyr,numyrexperience,alieneducompletedyr) VALUES(%d,%d,%d,%d)"""
#sql="""INSERT INTO icertdata(empnumemployees) VALUES(%s)"""
	cur = conn.cursor()
#cur.execute('SET NAMES utf8;') 
#cur.execute('SET CHARACTER SET utf8;')
#cur.execute('SET character_set_connection=utf8;')
	try:
		cur.execute(sql,(x,company,empAdd1,empAdd2,empcity,empState,empCountry,empZip,employerph,numEmployees,empYr,empLastName,empFirstName,empPhone,empEmail,attorneyLastName,attorneyFirstName,attorneyPhone,attorneyAdd1,attorneyAdd2,attorneyCity,attorneyState,attorneyCountry,attorneyZip,attorneyEmail,pwgtracking,OccupationTitle,skillLevel,pwgvalue,pwgDeterminationDate,pwgExpirationDate,owFromValue,owToValue,workAdd1,workAdd2,workCity,workState,workZip,jobTitle,majorField,numyrexp,jobDuties,specificSkill,swaStartDt,swaEndDt,newspaper,advDateFirst,advDateSecond,empWebSitePostDateFrom,empWebSitePostDateTo,jobSearchWebSiteFrom,jobSearchWebSiteTo,localNewsPaperDateFrom,localNewsPaperDateTo,alienCity,alienState,alienCountry,alienZip,aliencitizenshipcountry,aliencountryofbirth,alienclassofadmission,alienmajor,alieneducompletedyr,aliencollege,alienuniversityadd1,alienuniversityadd2,alienuniversitycity,alienuniversityState,alienuniversitycountry,alienuniversityzip))
	except:
		print("DB ERROR!!!!!!!!!!!!!!!!!!")
#cur.execute(sql,(numEmployees,empYr,numyrexp,alieneducompletedyr))

	conn.commit()
	cur.close()
	conn.close()

        																												 
#pwsource varchar(30),  , educationmin varchar(100),,trainingrequired varchar(10),alteducation varchar(100), 
																																																																		