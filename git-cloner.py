import os

while(True) :
	gitdir = raw_input("please enter dir for download git = ")
	gitaddr = raw_input("please enter git address (exp : https://github.com/example/example.git) = ")
	os.popen("cd " + gitdir)
	os.popen("git clone " + gitaddr)
	if (gitdir == ''):
		print "please enter directory"
	if (gitaddr == ''):
		print "please enter git address"

