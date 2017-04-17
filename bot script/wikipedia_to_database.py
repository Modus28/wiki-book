from bs4 import BeautifulSoup
import psycopg2
import requests
import json
import wikipedia

params = {
  'dbname': 'redacted',
  'user': 'redacted',
  'password': 'redacted',
  'host': 'redacted',
  'port': redacted
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



