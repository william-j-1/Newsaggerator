import sys,os
from bs4 import *
import requests
import mysql.connector

db = mysql.connector.connect(
     host="localhost",
     user="root",
     password="*******",
     database="news_sites"
    )
mycursor =db.cursor()
alphabet=["","a", "b", 'c', 'd', 'e']
later_alphabet=["","f","g","h","i","j"]
def get_websites(list,website_name):# used to get the top 5 news stories for each website
    for l in range(1,5):
            column_1=website_name+"col1"
            column_2=website_name+"col2"

            first_address = ("SELECT {} FROM {} WHERE ID_rank=%s").format(column_1,website_name)
            second_address = ("SELECT {} FROM {} WHERE ID_rank=%s").format(column_2,website_name)

            open_column1=(l,)
            mycursor.execute(first_address, open_column1)

            address_space = mycursor.fetchall()
            for x in address_space:
                first=x[0]

            open_column2=(l,)
            mycursor.execute(second_address, open_column2)
            address_space2=mycursor.fetchall()
            for x in address_space2:
                second=x[0]

            url=get_address(website_name)
            list[alphabet[l]]=search(url,first,second)

def get_address(name):# used to get the address for each website
    first=("SELECT site_database_name FROM site_names WHERE site_namescol =%s")
    open=(name,)
    mycursor.execute(first,open)
    weblink=mycursor.fetchall()
    url=weblink[0][0]
    return url

def search(websites,name1,name2): # used to find each website
    result=requests.get(websites)
    soup=BeautifulSoup(result.text,"html.parser")
    HeadLine=soup.find(class_ =name1).find(class_ =name2).getText()
    return(HeadLine.strip())


def get_links(list,data):
    for i in range(1,4):
        name=data+"links"
        first_address=("SELECT first_link FROM {} WHERE id_rank=%s").format(name)
        second_address=("SELECT second_link FROM {} WHERE id_rank=%s").format(name)
        open = (i,)
        mycursor.execute(first_address, open)

        link_space = mycursor.fetchall()
        for x in link_space:
            first = x[0]

        mycursor.execute(second_address, open)
        link_space2 = mycursor.fetchall()
        for x in link_space2:
            second = x[0]
        full_address = get_address(data)
        list[later_alphabet[i]]=search_for_url(full_address,first,second)

def search_for_url(website,name1,name2):
    result = requests.get(website)
    soup = BeautifulSoup(result.text, "html.parser")
    news_code = soup.find(class_=name1).find(class_=name2)
    name = news_code.find_all('a')
    for i in name:
        if 'href' in i.attrs:
            end_url=str(i.attrs['href'])
    return (website+end_url)

a="bbc_news"
list={}
get_websites(list,a)
print(list)
