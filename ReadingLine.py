# reader.py
import fileinput
import urllib2
import hashlib 
import sys
import os

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
CurrentFileName = ""
content = []
counter = 0
prgbar = ""
while counter != 115:
	a = conv(str(counter))
	CurrentFileName = "VirusShare_" + str(a) + ".md5"
	file = open(CurrentFileName, 'r')
	for line in file:
	    content.append(line.strip())
	counter += 1
	prgbar = "|"
	if sys.platform == 'linux-i386' or sys.platform == 'linux2':
		os.system("clear")
	elif sys.platform == 'win32':
		os.system("cls")
	else:
		os.system("cls")
	print "==========================================================="
	print u"Malware Removal Tool - -  [zekican@ozoktas.com] Copyright 2014"
	print "==========================================================="
	print("Loading Virus Databases : " + prgbar * counter)
viruses = []
FoundedMd = []
for root, dirs, files in os.walk('./'):
	for name in files:
		filename = os.path.join(root, name)
		
		if sys.platform == 'linux-i386' or sys.platform == 'linux2':
			os.system("clear")
		elif sys.platform == 'win32':
			os.system("cls")
		else:
			os.system("cls")
		print "==========================================================="
		print u"Malware Removal Tool - -  [zekican@ozoktas.com] Copyright 2014"
		print "==========================================================="
		print("Scanning infected files. Now I am scanning "+ filename)
		if(getmd5(filename) in content):
			print("MD5 : " + getmd5(filename))
			print("Virus Found ! File : " + filename )
			FoundedMd.append(getmd5(filename))
			viruses.append("\nVirus Found !! Details : \nMD5 : " + getmd5(filename) + "\nFile : " + filename)
			continue
if sys.platform == 'linux-i386' or sys.platform == 'linux2':
	os.system("clear")
elif sys.platform == 'win32':
	os.system("cls")
else:
	os.system("cls")
print "==========================================================="
print u"Malware Removal Tool - -  [zekican@ozoktas.com] Copyright 2014"
print "==========================================================="
print "======================Founded Threats======================"
print(viruses)
for vir in viruses:
	print "\n %s" % vir
for md in FoundedMd:
    print os.system("vtlite.py -s %s" % md)






