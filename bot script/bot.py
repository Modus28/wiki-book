import fbchat
import re
import psycopg2
params = {
  'dbname': 'd12u190iuusr3o',
  'user': 'quszuctlcqieqr',
  'password': '07351f585b5c9721034f3b7fa97c7d970a40a018d945a3b52e6a288fd7946cd8',
  'host': 'ec2-174-129-227-116.compute-1.amazonaws.com',
  'port': 5432
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
            chunks_of_texts = splitTextIntoFormattedChuncks(validateOutput(keywords));
            for each in chunks_of_texts:
                self.send(author_id, each);

def validateOutput(keywords):
    if keywords[1:5] == "help":
        return "commands are /help, /search [article]..."
    elif keywords[1:7] == "search":
        keyword = keywords[8:]
        return searchDatabase(keyword)
    else:
        return "Please type in a valid command"


def searchDatabase(keyword):
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute( "SELECT * FROM wiki_links WHERE keyword like '%" + keyword + "%';"  )
    valueOf = cur.fetchone()
    if valueOf == None:
        return "We could not find any entries on this input. Try something else."
    return valueOf;

def splitTextIntoFormattedChuncks(fullText):
    lists = [];
    for i in range(0, len(fullText), 500):
        lists.append(fullText[i:i+500])
    return lists


bot = hackCWRUProject("wikibook2017@gmail.com", "HACKCWRU!")
bot.listen()
