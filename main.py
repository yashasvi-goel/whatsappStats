import re

start="^((0)[0-9]|[1-2][0-9]|(3)[0-1])(\/)(((0)[1-9])|((1)[0-2]))(\/)(\d\d|\d{4}),\s(([0-9][0-9]):([0-9][0-9]) -)"
class Data:
    def __init__(self,date,time,author,message):
        self.date=date
        self.time=time
        self.author=author
        self.message=message

def getDataPoint(line): 
    splitLine = line.split(' - ')
    dateTime = splitLine[0]
    date, time = dateTime.split(', ')
    message = ' '.join(splitLine[1:])
    splitMessage = message.split(': ') 
    author = splitMessage[0] 
    message = ' '.join(splitMessage[1:])
    return date, time, author, message

def parse(rawChat):
    rawChat.readline()
    coll=[]
    temp=[]
    curr=Data(None,None,None,"")
    while True:
        message=rawChat.readline()
#        print message
        if not message:
            if len(temp)>0:
                curr.message=' '.join(temp)
#                print curr.date+" "+curr.author+" "+curr.message
                coll.append(curr)
                curr=Data(None,None,None,"")
            break
        if re.match(start,message):
            if len(temp)>0:
                curr.message=' '.join(temp)
#                print curr.date+" "+curr.author+" "+curr.message
                coll.append(curr)
                curr=Data(None,None,None,"")
            temp=[]
            curr.date,curr.time,curr.author,tempMessage= getDataPoint(message)
            temp.append(tempMessage)
        else:
            temp.append(message)
    sent=0
    recv=0 
    return coll 

rawChat= open('','r')#path of chat
extractedData=parse(rawChat)
print extractedData[1968].author
print len(extractedData)
