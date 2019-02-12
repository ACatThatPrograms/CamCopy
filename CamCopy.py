import shutil
import os, sys
import time
import pickle

version = "1.0.0"

#Function List

def varSet(): #Must be called after any menu initiated configuration changes

	global prefx, raw_ext, pic_ext

	(prefx, raw_ext, pic_ext) = confRead()
	
def printList():

	x = 0
	
	print('\n')

	for i in file_list:
		index = (file_list[x])
		x = x + 1
		print(index + ' | ')
	
	print("\n\nTotal: %s\n" % (x))

def confWrite(x, y, z): #Rewrites .conf file or creates if non-existant.

	conf_file = open('CamCopy.conf', 'w+')

	conf_file.write("Camera_Prefix : %s\n" % x)
	conf_file.write("Raw_Extension : %s\n" % y)
	conf_file.write("Pic_Extension : %s\n" % z)

	conf_file.close()
	
def confRead(): #Reads Conf and re-sets Variables

	conf_file = open('CamCopy.conf', 'r')
	
	x = conf_file.readline().split()
	prefx = x[2]
	
	x = conf_file.readline().split()
	raw_ext = x[2]
	
	x = conf_file.readline().split()
	pic_ext = x[2]
	
	x = None

	conf_file.close()
	
	return (prefx, raw_ext, pic_ext)
	
def initConf():

	conf_prefx = input("Please enter your camera's file prefix.\n\ne.g. If your picture files are 'CAN_DC_001.raw', enter 'CAN_DC_'\nCase isn't important.\n\nYour Camera's Image Prefix :> ")
	conf_raw_ext = input("\nPlease enter your camera's RAW file extension, without the period please.\ne.g. in the example above you would enter 'raw'.\n\nYour camera's raw extension :> ")
	
	x = input("\nPlease enter your camera's compressed picture format, or press enter to default to .jpg\n(Please type jpeg if it is used.) :> ")
	
	if len(x.lower()) > 2:
	
		conf_pic_ext = x
		
	else:
	
		conf_pic_ext = 'jpg'
	
	prefx = conf_prefx
	raw_ext = conf_raw_ext
	pic_ext = conf_pic_ext
	
	print("\nYour prefix will be set to: %s" % (prefx) )
	print("Your raw extension will be set to: %s" % (raw_ext) )
	print("Your compressed image extension will be set to: %s" % (pic_ext) )
	
	input("\nPress enter to continue ->")
	
	print("\n\nOne moment please\n")
	
	#Create and Insert Base data to config file
	
	confWrite(prefx, raw_ext, pic_ext)

#os.chdir(os.path.dirname(sys.argv[0])) #Change working directory to script root

print("\nWelcome to Camera Copy.\n\nVersion: %s\n" %(str(version)))

print("This program is aimed at photographers who shoot in RAW + Jpeg modes\nwho wish to copy their selected compressed images along with their RAW counterpart.")

exit = False

input("\nPress enter to continue ->")

#Global Variable Table Init

raw_file_list = [] #Contains all deviations of items in file_list

file_list = [] #User friendly file list

if os.path.isfile("CamCopy.conf"): #Load CamCopy File Config
	
	print("\nConfiguration found, loading now...")
	
	prefx, raw_ext, pic_ext = confRead()
	
	print("Configuration loaded.")


else: #Create CamCopy File and set-up Defaults

	print("\nYou seem to be missing a CamCopy config file in the active directory\nOne will be created for you now.\n\nYou will set-up a base configuration file now that can be changed later if needed.\n")
	
	initConf()
		
	#Create and Insert Base data to config file
	
	(prefx, raw_ext, pic_ext) = confRead() #Resets Variables
	
	print("All done!\n\n")
	
if os.path.isfile("rawlist.dat"): #Load CamCopy File Config
	
	print("\nImage list found, loading now...")
	
	img_file = open('rawlist.dat', 'rb')
	
	raw_file_list = pickle.load(img_file)
	
	img_file.close()
	
	print("Image list loaded.")
	
if os.path.isfile("imglist.dat"): #Load CamCopy File Config
	
	img_file = open('imglist.dat', 'rb')
	
	file_list = pickle.load(img_file)
	
	img_file.close()
	

	
print("\nType 'help' if you need further assistance. Type 'quit' to quit.")

#End variable Table Init

while exit == False:
	
	cl_input = input("\n:> ").split()
	
	#Check for command and truncate table to length of 2 if more than two values are given. Also pulls command(com) and command_variable (com_var)
	
	if len(cl_input) < 1:
	
		continue
	
	com = cl_input[0]
	
	if len(cl_input) > 1:
	
		while len(cl_input) > 2:
		
			del cl_input[-1]
		
		com_var = cl_input[1]
		
	#Command List Tree
	
	if com.lower() == "help":
		
		print("\nconfig		Reruns initial configuration set-up")
		print("\nprefx X		Sets camera prefix name to X")
		print("rawext X	Sets raw file extension type to X (No periods needed)")
		print("picext X	Sets picture file extension type to X (No periods needed)")
		print("\nadd		Starts add file dialogue")
		print("list		View active file list.")
		print("clearlist	Clears active file list.")
		print("copy		Starts copy dialogue.")
		print("\ncheck		Checks current configuration")
		print("\nAdvanced Operation Commands")
		print("\ndelprefx		Removes prefix, use for non-prefix copying")
		continue
		
	elif com.lower() == "config":
	
		print('\n')
		initConf()
		varSet()
		print("Reconfigured.")
		
	elif com.lower() == "prefx" or com.lower() == "rawext" or com.lower() == "picext":
	
		if len(cl_input) > 1:
		
			
			if com.lower() == "prefx":
			
				confWrite(com_var, raw_ext, pic_ext)
				
				print("\nCamera prefix changed to %s" % (com_var))
			
			elif com.lower() == "rawext":
			
				confWrite(prefx, com_var, pic_ext)
				
				print("\nRaw extension changed to %s" % (com_var))
			
			elif com.lower() == "picext":
			
				confWrite(prefx, raw_ext, com_var)
				
				print("\nCompressed Picture Extension changed to %s" % (com_var))
			
			(prefx, raw_ext, pic_ext) = confRead()
		
		else:
		
			print("\nThis command requires a variable.")
			
	### DEBUG COMMANDS
		
	elif com.lower() == "checkfile": #Debug checking of configuration file
	
		(a, b, c) = confRead()
		
		print("\n%s\n%s\n%s" % (a, b ,c))
		
	elif com.lower() == "rawlist": #Debug checking of configuration file
	
		print(raw_file_list)
		
	### END DEBUGS
		
	elif com.lower() == "check":
		
		print("\nCamera Prefix: 		%s\nRaw Extension: 		%s\nPicture Extension: 	%s" % (prefx, raw_ext , pic_ext))
		
	elif com.lower() == "add":
	
		if len(cl_input) == 1:
		
			files = (input("\n\nPlease enter file numbers to add, seperated by spaces.\nOmit the prefix and extention please.\n\nFiles :> ").split())
		
			x = 0
		
			for i in files:
				
				a_file_raw = ("%s%s.%s" % (prefx, files[x], raw_ext))
				a_file_clean = ("%s%s" % (prefx, files[x]))
				file_list.append(a_file_clean.upper()) #Appends lowercase filename for user-friendly listing
				
				raw_file_list.append(a_file_raw.lower()) # Appends lowercase filename to raw list
				raw_file_list.append(a_file_raw.upper()) # Appends uppercase filename to raw list
				a_file_raw = ("%s%s.%s" % (prefx.upper(), files[x], raw_ext.lower())) #Appends upper prefix & lower extension to raw list
				raw_file_list.append(a_file_raw)
				a_file_raw = ("%s%s.%s" % (prefx.lower(), files[x], raw_ext.upper())) #Inverse of above to raw list
				raw_file_list.append(a_file_raw)
				
				#Below are appendings for compressed file-type
				
				a_file_raw = ("%s%s.%s" % (prefx, files[x], pic_ext))
				raw_file_list.append(a_file_raw.lower()) # Appends lowercase filename to raw list
				raw_file_list.append(a_file_raw.upper()) # Appends uppercase filename to raw list
				a_file_raw = ("%s%s.%s" % (prefx.upper(), files[x], pic_ext.lower())) #Appends upper prefix & lower extension to raw list
				raw_file_list.append(a_file_raw)
				a_file_raw = ("%s%s.%s" % (prefx.lower(), files[x], pic_ext.upper())) #Inverse of above to raw list
				raw_file_list.append(a_file_raw)
				
				x = x + 1
			
			print("\nFiles added. Check active file list with the 'list' command.\n\nYour list will be saved in same directory for future use.")
			
			img_file = open('rawlist.dat', 'wb')
			
			pickle.dump(raw_file_list, img_file)
			
			img_file.close()
			
			img_file = open('imglist.dat', 'wb')
			
			pickle.dump(file_list, img_file)
			
			img_file.close()
		
		else:
		
			print("\nThis command requires no variables.")
			
	elif com.lower() == "list":
	
		printList()
		
	elif com.lower() == "clearlist":
	
		yn = input("\nAre you sure you want to clear the active file list? y/n :> ")
		
		while True:
		
			if yn.lower() == 'y':
			
				raw_file_list = []
				file_list = []
				
				### PUT LIST CLEARING CODE HERE, EITHER PICKLE EMPTY TABLE OR DEL LIST FILES. FIGURE IT OUT.
				
				os.remove('imglist.dat')
				
				os.remove('rawlist.dat')
				
				print("\nList cleared.\n")
				break
				
			elif yn.lower() == 'n':
			
				print("\nNot clearing.\n")
				break
			
			else:
			
				print("\nPlease re-think your decision and try again.\n")
				break
				
	elif com.lower() == "copy":
	
		x = input("\nWhat is the full source directory? :> ")
		
		source_path = x
		
		try:
		
			source_dir = os.listdir(x)
			
		except:
		
			print("Source directory not found. Please correct the path and try again")
			continue
		
		target_dir = input("\nWhat is the full target directory? :> ")
		
		try:
		
			z = os.listdir(target_dir)
			
		except:
		
			print("\nTarget Directory not found, try again please.\n")
			
			continue
		
		print("\nDouble check your input below.\n")
		
		print("Source: %s\nTarget: %s\n" % (source_path, target_dir))
		
		yn = input("Is this correct? y/n :> ")
		
		if yn.lower() == 'y':
		
			print('\n')
		
			for file in source_dir:
			
				if file in raw_file_list:
				
					full_file = "%s\%s" % (source_path, file)
					
					shutil.copy(full_file, target_dir)
					print("%s copied." % (file))
				

			print("\nAll done.")
			
		else: 
		
			print("\nRe-try and correct your mistakes carefully please.\n")
			
	
	elif com.lower() == "delprefx":
		
		prefx = ''
		
		print("\nPrefx cleared. This setting is not persistant; Use config, or prefx command to reset prefix.")
	
	elif com.lower() == "quit":
	
		print("\nGoodbye!")
		break
		
	else:
	
		print("\nCommand not recognized, type 'help' for assistance.")