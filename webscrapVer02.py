# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 22:10:39 2019

@author: Vikas
"""
import requests 
from bs4 import BeautifulSoup 
import re
import pandas as pd
from tabulate import tabulate

URL = "https://www.indeed.co.in/jobs?q=python&start=0"
r = requests.get(URL)  
soup = BeautifulSoup(r.text, 'html.parser') 
cnt=soup.find("div", {"id": "searchCount"}).getText()
cnt=cnt.replace('Page 1 of ','')
cnt=cnt.replace(',','')
TotalJob = re.findall('\d+',cnt)
TotalJob = int(TotalJob[0])
TotalPage=round(TotalJob/10)
#try:
print("Total Number of Python Jobs :",TotalJob)
print(" With Total No of Page Listing : ",TotalPage)
TopPage=int(input('Number of Pages to Fetch:'))
#except:
#    print('Integer value required. Program Terminating.')
df = pd.DataFrame(columns =['Company','CompanyEsc','CompanyLink','Location','Country','Zip','City','JobTitle']) 
for i in range(TopPage):
#for i in range(2):
    URL = "https://www.indeed.co.in/jobs?q=python&start="+str(i)
    if(i==0):
        print("Getting Data...............")
    print('#',end='')
    r = requests.get(URL)  
    soup = BeautifulSoup(r.text, 'html.parser') 
    str_soup=str(soup)
    p=re.compile("cmp:'(.*?)',cmpesc:'(.*?)',cmplnk:'(.*?)',loc:'(.*?)',country:'(.*?)',zip:'(.*?)',city:'(.*?)',title:'(.*?)'")   
    #print(p.findall(str_soup)) 
    data=p.findall(str_soup)
    df1 = pd.DataFrame(data,columns =['Company','CompanyEsc','CompanyLink','Location','Country','Zip','City','JobTitle'])
    df=df.append(df1,ignore_index = True)
JobProfile=df['JobTitle'].unique()
JobLocation=df['Location'].unique()
while(True):
    print("\n\n***** Welcome to Python Job listing *****\nPlease choose an action from below menu:")
    print ('Enter 1 to Job Profiles :')
    print ('Enter 2 to Locations:')
    print ('Enter 3 to Exit:')
    try:
        inp=int(input('Choice (1-3) :'))
    except:
        print('Integer value required. Program Terminating.')

    if inp==1:
        j=1
        l=len(JobProfile)
        while(True):
            print("Enter Profile Number between 1-",l)
            for job in JobProfile:
                print(j," : ",job)
                j=j+1
            try:
                ip=int(input('Press 0 to Exit /n Your Choice:'))
                if(ip!=0):
                    a=JobProfile[ip-1]
                    profile=df[df['JobTitle'].str.contains(str(a))]
                    print(tabulate(profile[['JobTitle','Company','Location']], headers='keys', tablefmt='psql'))
                    break
                else:
                    break
            except:
                print('Integer value in Range required. Program Terminating.')
                break
            j=1
    elif inp==2:
        j=1
        l=len(JobLocation)
        while(True):
            print("Enter Job Location Number between 1-",l)
            for location in JobLocation:
                print(j," : ",location)
                j=j+1
            try:
                ip=int(input('Press 0 to Exit /n Your Choice:'))
                if(ip!=0):
                    a=JobLocation[ip-1]
                    profile=df[df['Location'].str.contains(str(a))]
                    print(tabulate(profile[['Location','JobTitle','Company']], headers='keys', tablefmt='psql'))
                    break
                else:
                    break
            except:
                print('Integer value in Range required. Program Terminating.')
                break
            j=1
    elif inp==3:
        break