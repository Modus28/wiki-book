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
	
	

# doInsert('doggo', 'boring test' )
doQuery('doggo')
