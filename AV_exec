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
print u"Malware MD5 Hashes Download Tool - -  [zekican@ozoktas.com] Copyright 2014"
print "==========================================================="



def rep(number):
    rounded = round(number, -len(str(number)))
    if not rounded: # 0 evaluates to False
        rounded = 10**(len(str(number))-1)
    return "{number:05}".format(number=int(rounded))
def download(address):
	url = str(address)

	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break

	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print status,

	f.close()

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
		
def getMainMenu():
	print (30 * '-')
	print ("   M A I N - M E N U")
	print (30 * '-')
	print ("1. Update")
	print ("2. Scan")
	print ("3. Check Integrity")
	print ("4. Exit")
	print (30 * '-')
	 
	###########################
	## Robust error handling ##
	## only accept int       ##
	###########################
	## Wait for valid input in while...not ###
	is_valid=0
	 
	while not is_valid :
			try :
					choice = int ( raw_input('Enter your choice [1-4] : ') )
					is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
			except ValueError, e :
					print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
	 
	### Take action as per selected menu-option ###

print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Update")
print ("2. Scan")
print ("3. Check Integrity")
print ("4. Exit")
print (30 * '-')
 
###########################
## Robust error handling ##
## only accept int       ##
###########################
## Wait for valid input in while...not ###
is_valid=0
 
while not is_valid :
        try :
                choice = int ( raw_input('Enter your choice [1-4] : ') )
                is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
 
### Take action as per selected menu-option ###
 
if choice == 1:
		counter = 0
		while counter != 115:
			a = conv(str(counter))
			add = "http://virusshare.com/hashes/VirusShare_" + str(a) + ".md5"
			download(add)
			print("MD5 : " + getmd5("VirusShare_" + str(a) + ".md5"))
			counter += 1

		print("Download Compeleted.\n Any questions : zekican@ozoktas.com")
		getMainMenu()
elif choice == 2:
		os.system("ReadingLine.py")
		getMainMenu()
elif choice == 3:
        os.system("Check_MD5.py")
	getMainMenu()
elif choice == 4:
		print("Thanks.\nAny questions : zekican@ozoktas.com")
		sys.exit(0)
else:
        print ("Invalid number. Try again...")		
		
