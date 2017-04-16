import fbchat
import re
import psycopg2
import wikipedia
params = {
  'dbname': 'd12u190iuusr3o',
  'user': 'quszuctlcqieqr',
  'password': '07351f585b5c9721034f3b7fa97c7d970a40a018d945a3b52e6a288fd7946cd8',
  'host': 'ec2-174-129-227-116.compute-1.amazonaws.com',
  'port': 5432
}
conn = psycopg2.connect(**params)
cur = conn.cursor()
class hackCWRUProject(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read

        keywords = message
        if str(author_id) != str(self.uid):
            #responseText = validateOutput(keywords);
            #wikiText = searchDatabase(keywords);
            fullText = validateOutput(keywords);
            a = str(fullText[1]);
            for i in range(0, len(a), 500):
                self.send(author_id, a[i:i+500]);

def validateOutput(keywords):
    if keywords[1:5] == "help":
        return ['help',"commands are /help, /search [article]..."]
    elif keywords[1:7] == "search":
        keyword = keywords[8:]
        return searchDatabase(keyword)
    else:
        return ['valid',"Please type in a valid command"]


def searchDatabase(keyword):
    key = str(keyword).upper();
    cur.execute( "SELECT * FROM wiki_links WHERE UPPER(keyword) like '%" + key + "%';"  )
    valueOf = cur.fetchone()
    if valueOf == None:
        return lookupWikipedia(keyword)
    return valueOf;

def splitTextIntoFormattedChuncks(fullText):
    lists = [];
    for i in range(0, len(fullText), 500):
        lists.append(fullText[i:i+500])
    return lists

def lookupWikipedia(keyword):
    text = wikipedia.summary(keyword, sentences = 100)
    doInsert(str(keyword),text)
    key = str(keyword).upper();
    cur.execute( "SELECT * FROM wiki_links WHERE UPPER(keyword) like '%" + key + "%';"  )
    valueOf = cur.fetchone()
    return valueOf;

def doInsert(keyword,text) :
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    text = text.replace("'","''")
    cur.execute("INSERT INTO wiki_links VALUES ('" + str(keyword) + "','" + text + "');")
    conn.commit()

bot = hackCWRUProject("wikibook2017@gmail.com", "HACKCWRU!")
bot.listen()
