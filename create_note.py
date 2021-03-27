#!/bin/python

#
#       ███╗░░██╗██╗██╗░░██╗░█████╗░██████╗░░█████╗░██╗░░██╗███████╗
#       ████╗░██║██║██║░░██║██╔══██╗██╔══██╗██╔══██╗██║░██╔╝╚════██║
#       ██╔██╗██║██║███████║███████║██████╔╝██║░░██║█████═╝░░░███╔═╝
#       ██║╚████║██║██╔══██║██╔══██║██╔══██╗██║░░██║██╔═██╗░██╔══╝░░
#       ██║░╚███║██║██║░░██║██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗
#       ╚═╝░░╚══╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝
#
#       DRAFTED BY NIHAR SAMANTARAY ON 22-03-21. [https://nihars.com]
#       SOURCE [create_note.py] LAST MODIFIED ON 27-03-21

import datetime
from os import system

path='content/note/'
title = input("Title: ");
subtitle = input("Sub Title: ");

d=datetime.datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z")
date=d[0:-2]+':'+d[-2:]

filename=title.lower().replace(" ","_")

f = open(path+filename+".markdown","w+")
f.write("---\n")
f.write("title: "+title+"\n")
f.write("subtitle: "+subtitle+"\n")
f.write("date: "+date+"\n")
f.write("---\n")
f.close()

system('$EDITOR '+path+filename+".markdown")

