import fbchat
import re
import psycopg2
import wikipedia
params = {
  'dbname': 'redacted',
  'user': 'redacted',
  'password': 'redacted',
  'host': 'redacted',
  'port': redacted
}
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
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    key = str(keyword).upper();
    cur.execute( "SELECT * FROM wiki_links WHERE UPPER(keyword) like '%" + key + "%';"  )
    # 'SELECT * FROM wiki_links WHERE ATOM like ATOM';'DROP TABLE wiki_links"
    valueOf = cur.fetchone()
    conn.close();
    if valueOf == None:
        return lookupWikipedia(keyword)
    return valueOf;

def splitTextIntoFormattedChuncks(fullText):
    lists = [];
    for i in range(0, len(fullText), 500):
        lists.append(fullText[i:i+500])
    return lists

def lookupWikipedia(keyword):
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    try:
        text = wikipedia.summary(keyword, sentences = 100)
    except wikipedia.exceptions.DisambiguationError:
        return ['Error', "This query is too general. Please refine it more."]
    doInsert(str(keyword),text)
    key = str(keyword).upper();
    cur.execute( "SELECT * FROM wiki_links WHERE UPPER(keyword) like '%" + key + "%';"  )
    valueOf = cur.fetchone();
    conn.close();
    return valueOf;

def doInsert(keyword,text) :
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    text = text.replace("'","''")
    cur.execute("INSERT INTO wiki_links VALUES ('" + str(keyword) + "','" + text + "');")
    conn.commit()
    conn.close();

bot = hackCWRUProject("wikibook2017@gmail.com", "HACKCWRU!")
bot.listen()