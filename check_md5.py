import urllib2
import hashlib 
import sys
import os

if sys.platform == 'linux-i386' or sys.platform == 'linux2':
        os.system("clear")
elif sys.platform == 'win32':
        os.system("cls")
else:
        os.system("cls")
		
print "==========================================================="
print u"MD5 Checker Tool - - - - - - - - - - [zekican@ozoktas.com]"
print "==========================================================="

def conv(no):
	if len(no) == 1:
		return "0000" + no
	elif len(no) == 2:
		return "000" + no
	elif len(no) == 3:
		return "00" + no
	elif len(no) == 4:
		return "0" + no
	else:
		return no

def getmd5(filename):
	with open(filename) as file_to_check:
	    # read contents of the file
	    data = file_to_check.read()    
	    # pipe contents of the file through
	    md5_returned = hashlib.md5(data).hexdigest()
	    return md5_returned

counter = 0
while counter != 115:
	a = conv(str(counter))
	add = "http://virusshare.com/hashes/VirusShare_" + str(a) + ".md5"
	print("File Name : VirusShare_" + str(a) + ".md5" + "       MD5 : " + getmd5("VirusShare_" + str(a) + ".md5"))
	counter += 1
