import fbchat
import time
client = fbchat.Client("wikibook2017@gmail.com", "HACKCWRU!")
friends = client.getUsers("kelvin")  # return a list of names

friend = friends[0]
s = "boi"
for i in range(10):
    time.sleep(.4)
    s += "i"
    sent = client.send(friend.uid, s)
if sent:
    print("Message sent successfully!")
# IMAGES
client.sendLocalImage(friend.uid,message='<message text>',image='<path/to/image/file>') # send local image
imgurl = "http://i.imgur.com/LDQ2ITV.jpg"
client.sendRemoteImage(friend.uid,message='<message text>', image=imgurl) # send image from image url