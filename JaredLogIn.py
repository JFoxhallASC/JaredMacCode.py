
# log in,

import time import *
print time

print ("WELCOME!")

name = raw_input("PUT YO USERNAME IN!")

USERNAME = 'runthejewls'

if name == (USERNAME):
	print ("WAIT ONE SEC LEMME CHEAK THE GUEST LIST...")
	time.sleep(5.0)
	print('...')
	time.sleep(3.0)
	print("CONGRATULATIONS. NOW ENTER YO PASSWORD!")

if name != (USERNAME):
	print ("GET OUT MY HOUSE!")
	time.sleep(5.0)
	sys.exit()


PASSWORD = raw_input("PUT YO PASSWORD IN!")
PASSWORD1 = 'thegreatesttrick'

if PASSWORD == (PASSWORD1):
	time.sleep(1.5)
	print "WELCOME IN!"

if PASSWORD != (PASSWORD1):
	print "wait one sec that might be the passowrd...."
	time.sleep(3.0)
	print "...wait..."
	time.sleep(3.0)
	print "SIKE YOU WOULD HAVE THOUGHT! GET YO ASS HOME!"
	sys.exit()




