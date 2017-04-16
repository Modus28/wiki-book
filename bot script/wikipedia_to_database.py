from bs4 import BeautifulSoup
import psycopg2
import requests
import json
import wikipedia

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
    text = text.replace("'","''")
    cur.execute("INSERT INTO wiki_links VALUES ('" + str(keyword) + "','" + text + "');")
    conn.commit()
	

def doQuery(keyword) :
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    text = text.replace("'","''")
    cur.execute( "SELECT text FROM wiki_links where keyword = '" + keyword + "';"  )
    print(cur.fetchone())

def add_wiki_to_db(word):
    text = wikipedia.summary(word, sentences = 100)
    doInsert(str(word),text)

def add_multiple_to_db(words):
    for word in words:
        add_wiki_to_db(str(word))


#fileHandle.write(line)

#fileHandle.close()
# fileHandle.write(str(a.encode('utf-8')))



