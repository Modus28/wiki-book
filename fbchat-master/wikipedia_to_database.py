import urllib, urllib.request
from bs4 import BeautifulSoup
import psycopg2

params = {
  'dbname': 'd12u190iuusr3o',
  'user': 'quszuctlcqieqr',
  'password': '07351f585b5c9721034f3b7fa97c7d970a40a018d945a3b52e6a288fd7946cd8',
  'host': 'ec2-174-129-227-116.compute-1.amazonaws.com',
  'port': 5432
}


def doInsert(keyword,text) :
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("INSERT INTO wiki_links VALUES ('" + keyword + "','" + text + "');")
    conn.commit()
    conn.close()
	


def doQuery(keyword) :
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute( "SELECT text FROM wiki_links where keyword = '" + keyword + "';"  )
    print(cur.fetchone())
    conn.close()

# Written by Adam Beck. Takes in a URL, and returns an acceptably formatted
# string that contains all of the text from that webpage.
def htmlToText(url):
    fhand = urllib.request.urlopen(url)
    soup = BeautifulSoup(fhand)
    a = soup.find("div", {"id": "mw-content-text"}).text

    #fileHandle = open('output.txt', 'w')

    string = a.encode('utf-8')

    acceptable = ".,/';[]=-)(*&^%$#! \\"
    line = ""
    counter = 0
    trigger = False
    periodCounter = 0
    returnString = ""

    for i in string:
        if chr(i) is '.':
            periodCounter += 1
        if periodCounter == 3:
            periodCounter = 0
            returnString += ".\n\n"
            counter = 0
            continue

        counter += 1

        if acceptable.__contains__(chr(i)):
            returnString += chr(i)
            continue
        if str.isalnum(chr(i)):
            returnString += chr(i)
        if chr(i) is ' ' or chr(i) is '.':
            returnString += chr(i)

        if counter % 250 == 0:
            returnString += "-\n"
    return returnString

#fileHandle.write(line)

#fileHandle.close()
# fileHandle.write(str(a.encode('utf-8')))



