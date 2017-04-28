#This program get GC details each day along with sequence id which is needed in 2nd program and inserts record into icertportal table
import datetime
from re import sub
import re
from decimal import Decimal
import pymysql
import ssl
import sys
import traceback
import datetime
from datetime import date, timedelta

def removequote(str):
    length=len(str)
    count=0
    str1=""
    for s in str:
        if(count==0 or count==length-1):
            if(s=="\""):
                str1=str1
            else:
                str1 = str1+s
        else:
            str1 = str1+s
        count+=1
    return str1
def mmddyyyy(str):
    print(str)
    strs = str.split("/")
    str = strs[2]+"-"+strs[0]+"-"+strs[1]
    return str
def removebracket(str):
    s=""
    for c in str:
        if(c=="["):
            str=s+" "
        elif(c=="]"):
            str=s+" "
        else:
            str=s+c
    return str

delta=1
#delta=165
da = date.today() - timedelta(days=delta)
print(da.strftime("%m/%d/%Y"))
detailurl="https://lcr-pjr.doleta.gov/index.cfm?event=ehLCJRExternal.dspCert&doc_id=3&visa_class_id=6&id="
url ="https://icert.doleta.gov/index.cfm?event=ehLCJRExternal.dspQuickCertSearchGridData&&startSearch=1&case_number=&employer_business_name=&visa_class_id=6&state_id=all&location_range=10&location_zipcode=&job_title=&naic_code=&create_date=undefined&post_end_date=undefined&h1b_data_series=ALL&start_date_from="+da.strftime("%m/%d/%Y")+"&start_date_to="+(da-timedelta(days=1)).strftime("%m/%d/%Y")+"&end_date_from=mm/dd/yyyy&end_date_to=mm/dd/yyyy&nd=1464942893598&page=2&rows=1000&sidx=create_date&sord=desc&nd=1464942948365&_search=false"
print(url)
try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
context = ssl._create_unverified_context()
page=urlopen(url,context=context)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
soups=str(soup)
print(soups)
count=0;cnt=0;
data = soups.split(",[")# there are some job titles with []. Need to change separator
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='misc',use_unicode=True, charset="utf8")
sql="""INSERT INTO icertportal(id,caseNumber,jobPostingDate,caseType,status,employer,startDate,endDate,jobTitle,state,url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
cur = conn.cursor()
company="";startDate="";endDate="";jobTitle="";state=""
for d in data:
    cnt+=1;#Checks 1st row
    if(cnt==1):
        str1 = d.split("[[")
        str = str1[1].split(",")
        company = removequote(str[5])
        detailurl=detailurl+removequote(str[0])
        jobTitle=removequote(str[8])

        if(removequote(str[6]).find("0")!=-1):
            print("First ROW INSIDE 1st IF")
            print(d)
            print("++++++++++++",removequote(str[0]),"|",removequote(str[1]),"|",removequote(str[2]),"|",removequote(str[3]),"|",removequote(str[4]),"|",removequote(str[5]),"|",removequote(str[6]),"|",removequote(str[7]),"|",removequote(str[8]),"|",removequote(str[9]))
            #print("------------",removequote(str[0]),"-",removequote(str[1]),"-",removequote(str[2]),"-",removequote(str[3]),"-",removequote(str[4]),"-",company,"-",startDate,"-",endDate,"-",jobTitle,"-",state,"--",detailurl)

            startDate=removequote(str[6])
            endDate=removequote(str[7])
            if(removebracket(str[8]).endswith('"')):
                jobTitle=jobTitle
                state=removequote(str[9])
                print("First ROW INSIDE jobtitle 1st match")
            else:
                if(removebracket(str[9]).endswith('"')):
                    print("First ROW INSIDE jobtitle 1st match 2nd")
                    jobTitle = jobTitle+removequote(str[9])
                    state=removequote(str[10])
        else:
            company=company+" "+removequote(str[6])
            if(removequote(str[7]).find("0")!=-1):
                print("First ROW INSIDE 2nd else IF")
                startDate=removequote(str[7])
                endDate=removequote(str[8])
                #jobTitle=removequote(str[9])
                if(removebracket(str[9]).endswith('"')):
                    jobTitle=removequote(str[9])
                    state=removequote(str[10])
                    print("First ROW INSIDE jobtitle 2nd match")
                else:
                    if(removebracket(str[10]).endswith('"')):
                        jobTitle = jobTitle+removequote(str[10])
                        state=removequote(str[11])
                        print("First ROW INSIDE jobtitle 2nd match 2nd")
            else:

                company=company+removequote(str[7])
                if(removequote(str[8]).find("0")!=-1):

                    startDate=removequote(str[8])
                    endDate=removequote(str[9])
                    #jobTitle=removequote(str[10])
                    if(removebracket(str[10]).endswith('"')):
                        jobTitle=removequote(str[10])
                        state=removequote(str[11])
                        print("First ROW INSIDE jobtitle 3rd match")
                    else:
                        if(removebracket(str[11]).endswith('"')):
                            jobTitle = jobTitle+removequote(str[11])
                            state=removequote(str[12])
                            print("First ROW INSIDE jobtitle 3rd match 2nd")
                    print("------",str[10],"---",jobTitle)
                    state=removequote(str[11])
                    print("First ROW INSIDE 3rd else IF JOBTITLE:",jobTitle)
        print("FIRST ROW:",removequote(str[0]),"-",removequote(str[1]),"-",removequote(str[2]),"-",removequote(str[3]),"-",removequote(str[4]),"-",company,"-",startDate,"-",endDate,"-",jobTitle,"-",state,"--",detailurl)
        try:
            cur.execute(sql,(removequote(str[0]),removequote(str[1]),mmddyyyy(removequote(str[2])),removequote(str[3]),removequote(str[4]),removequote(company),mmddyyyy(startDate),mmddyyyy(endDate),jobTitle,state,detailurl))
            detailurl="https://lcr-pjr.doleta.gov/index.cfm?event=ehLCJRExternal.dspCert&doc_id=3&visa_class_id=6&id="
        except:
            print("DB ERROR!!!!!!!!!!!!!!!!!!")
            detailurl="https://lcr-pjr.doleta.gov/index.cfm?event=ehLCJRExternal.dspCert&doc_id=3&visa_class_id=6&id="
            print(traceback.format_exc())
    if(d.find("A-")!=-1 and cnt>1):
        count+=1
        #print(d,count)
        str = d.split(",")
        company = removequote(str[5])
        detailurl=detailurl+removequote(str[0])
        jobTitle=removequote(str[8])

        #state=removequote(str[9])
        if(removequote(str[6]).find("0")!=-1):
            print("INSIDE 1st IF")
            print(d)
            print("++++++++++++",removequote(str[0]),"|",removequote(str[1]),"|",removequote(str[2]),"|",removequote(str[3]),"|",removequote(str[4]),"|",removequote(str[5]),"|",removequote(str[6]),"|",removequote(str[7]),"|",removequote(str[8]),"|",removequote(str[9]))
            #print("------------",removequote(str[0]),"-",removequote(str[1]),"-",removequote(str[2]),"-",removequote(str[3]),"-",removequote(str[4]),"-",company,"-",startDate,"-",endDate,"-",jobTitle,"-",state,"--",detailurl)

            startDate=removequote(str[6])
            endDate=removequote(str[7])
            if(removebracket(str[8]).endswith('"')):
                jobTitle=jobTitle
                state=removequote(str[9])
                print("INSIDE jobtitle 1st match")
            else:
                if(removebracket(str[9]).endswith('"')):
                    print("INSIDE jobtitle 1st match 2nd")
                    jobTitle = jobTitle+removequote(str[9])
                    state=removequote(str[10])
        else:
            company=company+" "+removequote(str[6])
            if(removequote(str[7]).find("0")!=-1):
                print("INSIDE 2nd else IF")
                startDate=removequote(str[7])
                endDate=removequote(str[8])
                #jobTitle=removequote(str[9])
                if(removebracket(str[9]).endswith('"')):
                    jobTitle=removequote(str[9])
                    state=removequote(str[10])
                    print("INSIDE jobtitle 2nd match")
                else:
                    if(removebracket(str[10]).endswith('"')):
                        jobTitle = jobTitle+removequote(str[10])
                        state=removequote(str[11])
                        print("INSIDE jobtitle 2nd match 2nd")
            else:

                company=company+removequote(str[7])
                if(removequote(str[8]).find("0")!=-1):

                    startDate=removequote(str[8])
                    endDate=removequote(str[9])
                    #jobTitle=removequote(str[10])
                    if(removebracket(str[10]).endswith('"')):
                        jobTitle=removequote(str[10])
                        state=removequote(str[11])
                        print("INSIDE jobtitle 3rd match")
                    else:
                        if(removebracket(str[11]).endswith('"')):
                            jobTitle = jobTitle+removequote(str[11])
                            state=removequote(str[12])
                            print("INSIDE jobtitle 3rd match 2nd")
                    print("------",str[10],"---",jobTitle)
                    state=removequote(str[11])
                    print("INSIDE 3rd else IF JOBTITLE:",jobTitle)
        print(d)
        print(removequote(str[0]),"|",removequote(str[1]),"|",removequote(str[2]),"|",removequote(str[3]),"|",removequote(str[4]),"|",removequote(str[5]),"|",removequote(str[6]),"|",removequote(str[7]),"|",removequote(str[8]),"|",removequote(str[9]),"|",removequote(str[10]),"|",removequote(str[11]))
        print(removequote(str[0]),"-",removequote(str[1]),"-",removequote(str[2]),"-",removequote(str[3]),"-",removequote(str[4]),"-",company,"-",startDate,"-",endDate,"-",jobTitle,"-",state,"--",detailurl)
        try:
            cur.execute(sql,(removequote(str[0]),removequote(str[1]),mmddyyyy(removequote(str[2])),removequote(str[3]),removequote(str[4]),removequote(company),mmddyyyy(startDate),mmddyyyy(endDate),jobTitle,state,detailurl))
            detailurl="https://lcr-pjr.doleta.gov/index.cfm?event=ehLCJRExternal.dspCert&doc_id=3&visa_class_id=6&id="
        except:
            print("DB ERROR!!!!!!!!!!!!!!!!!!")
            detailurl="https://lcr-pjr.doleta.gov/index.cfm?event=ehLCJRExternal.dspCert&doc_id=3&visa_class_id=6&id="
            print(traceback.format_exc())
            #print('ERROR: %sn' % str(err))
            print(removequote(str[0]),"-",removequote(str[1]),"-",removequote(str[2]),"-",removequote(str[3]),"-",removequote(str[4]),"-",removequote(str[5]),"-",removequote(str[6]),"-",removequote(str[7]),"-",jobTitle,"-",state,"--",detailurl)

conn.commit()
cur.close()
conn.close()
        #print(str[0],str[1],str[2],str[5],str[6],str[7],str[8],str[9])
print("TOTAL RECORD FETCHED:",count)
