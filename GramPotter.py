######################################################################################
######  GramPotter by lsash   first ver = 25/6/2018  #################################
####################  some scraper that virtually touchable for any mat  #############
######################################################################################
#################if u want to do it 


from random import randrange
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import sys, time
import os, io, csv
#import urllib
#from urllib import FancyURLopener
import urllib.request
#from subprocess import call
import subprocess


from pynput import keyboard

def on_press(key):
	global heardy

	try: k = key.char # single-char keys
	except: k = key.name # other keys
	#print('Key pressed: ' + k)
	#if key == keyboard.Key.esc:
	#	print('esc from pynput.')
	#	return False # stop listener
	
	#if k in ['1', '2', 'left', 'right']: # keys interested
		# self.keys.append(k) # store it in global-like variable
		#print('Key pressed: ' + k)
		#return False # remove this if want more keys
	if k in ['e']:
		print("[HEARD=Explorer demand]")
		print("address=", basedir)
		try:
			#os.system("nautilus '" + basedir + "'")
			#with open("nauti_out.txt", "w") as file:
			#	subprocess.run(["nautilus", basedir], stdout=file, stderr=file)


			pid=os.fork()
			if pid==0: # new process
				os.system("nohup nautilus '" + basedir + "'")
				#os.system("nohup python ./myfile.py &")
				#feh -Z -d -F --randomize -B white -D 0.68 ./
				#feh -Z -d -F -B white -D 9.7 ./
				#feh -Z -d -F -B magenta -D 0.7 ./
		except:
			print("Oops!" + sys.exc_info()[0] + "occured.")
			return False # stop listener

	if k in ['up']:
		print("[HEARD=UP signal]")


	if k in ['down']:
		print("[HEARD=OMG downer.]")


	if k in ['t']:
		print("[HEARD=OMG t come.]")
		heardy = 1
		print("+++++++++++++++++++++++++++++++++++++++++++++seekMore=", heardy)

lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread

heardy = 0

#############################################################
######caller: harvester
######behave: calc how long does it take
#############################################################
def dph(count, blockSize, totalSize):
	"""A hook to report the progress of a download. This is mostly intended for users with slow internet 			connections. Reports every 5% change in download progress.
	"""
	global last_percent_reported
	percent = int(count * blockSize * 100 / totalSize)
	if last_percent_reported != percent:
		if percent % 5 == 0:
			sys.stdout.write("%s%%" % percent)
			sys.stdout.flush()
		else:
			sys.stdout.write(".")
			sys.stdout.flush()
	else:
			sys.stdout.write("*")
	last_percent_reported = percent

#############################################################
######caller: gram_src_grabber
######behave: down the DGD
#############################################################
def harvester(yurl):
	#print "harv_base=", basedir
	if not os.path.exists(basedir):
		os.makedirs(basedir)
	f = os.path.basename(yurl)
	if "?_nc_" in f:
		sc, eui = f.split("?_nc_")
		f = sc
		#print("[eui_suspic]" + f)
	fullfilename = os.path.join(basedir, f)
	if os.path.exists(fullfilename):
		#print "[exist---ed]u r already pac-pot aren't u?", f
		print ("[existed.]")
	else:
		print("[torch-able]" + yurl)
		#urllib.urlretrieve(yurl, fullfilename)
		#mop.retrieve(yurl, fullfilename)
		mop.retrieve(yurl, fullfilename, reporthook=dph)
		print (" ☆harvested.")

#############################################################
######caller: main
######behave: pretend apple
#############################################################
#http://wolfprojects.altervista.org/articles/change-urllib-user-agent/
#print URLopener.version
#class MyOpener(FancyURLopener):
class MyOpener(urllib.request.FancyURLopener):
	version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/604.1.31 (KHTML, like Gecko) Version/11.0 Safari/604.1.31'

#############################################################
###### caller: gram accessor
###### behave: rebooter
#############################################################
def down_pot_rotator():
	global DGD_Screen
	print ("******down pot, memory release is way to go")
	try:
		DGD_Screen.quit()#please close your eyes when this emit error it is not mine but selenium......!
	except:
		print ("caught")
	DGD_Screen = webdriver.Firefox(executable_path=r'../../geck/gecko/geckodriver')
	#DGD_Screen = webdriver.Firefox() #replace with .Firefox(), or with the browsing-machine of your choice
	DGD_Screen.set_window_size(1080, 680)
	#return wd
#############################################################
######caller: gram accessor
######behave: clicker
############################################################
def gram_click_obsessor():
	#for elem in element_scooper("//div[@class='rg_meta notranslate']"):
	######Insta fook gram changed their logic from a class to div class
	#for elem in element_scooper(lob, "//a"):
	for elem in element_scooper("//div"):
		try:
			x = elem.get_attribute("class")
			if "Righ" in x:#R I G H T  C H E V R O N
				print ("☆let us tick", end='')
				elem.click()
				return 0
		except:
			print ("click_obsess_exc=")
			print ("Oops!", sys.exc_info()[0], "occured." )
	return 72

#############################################################
######caller: gram accessor
######behave: get all dl-able page url from da Screen and grope it
#############################################################
def gram_src_grabber():
	innerHTML = DGD_Screen.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
	with io.open('SpecificPageScrape.log','w',encoding='utf-8') as f:
		#f.write(unicode(innerHTML))#p 2.7
		f.write(innerHTML)#p 3
	for elem in element_scooper("(//img|//video)"):
		try:
			#print "class=", elem.get_attribute("class")
			x = elem.get_attribute("src")#
			c = elem.get_attribute("class")#
			a = elem.get_attribute("alt")#
			#if "inst" in x: > inst string contain or not is so important?
			if a is None:
				print("☆dGd-Video-Suspicious")
				#my food
				harv_ready(x)
			else:
				if "profile" in a:
					print(".", end='')
				elif "food" in a:
					print("☆", a)
					harv_ready(x)
				else:
					print("☆", a)
					#my food
					harv_ready(x)
		except StaleElementReferenceException as Exception:
			print("dgd stale element")
#############################################################
###### caller: src grabber
###### behave: append pot
#############################################################
def harv_ready(DGD_place):
	if DGD_place not in pine:
		pine.append(DGD_place)



#############################################################
###### caller: crawl them all
###### behave: get all jumper-able page url from Top Screen and put it into HLINK array
#############################################################
def gram_href_grabber():
	innerHTML = DGD_Screen.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
	with io.open('TopScrape.log','w',encoding='utf-8') as f:
		#f.write(unicode(innerHTML))#python 2.7
		f.write(innerHTML)#python 3
	for elem in element_scooper("//a"):

		try:
			x = elem.get_attribute("href")#
		except:
			print(sys.exc_info()[0])
			print("++++++so, retry booty++++++")
			gram_href_grabber()


		if "/p/" in x:
			if x not in hlink:
				print ("scraper_interest=" + (x))
				hlink.append(x)

#############################################################
###### caller: click obsessor
###### caller: src   obsessor
###### caller: href  obsessor
###### behave: elements finder
#############################################################
def element_scooper(ele):# get elements 4 deepen pot
	stat = 0
	while stat == 0:
		try:
			webelem = DGD_Screen.find_elements_by_xpath(ele)# return web element, this is clickable sometimes
		#except httplib.BadStatusLine:
		#	print "da line status seems bad."
		except:
			print ("elm_scoop=")
			print ("Oops!", sys.exc_info()[0], "occured." )
		finally:
			stat = 1
	return webelem

#############################################################
######caller: gram accessor
######behave: scroll window and call grabber
#############################################################
def crawl_them_all(downer):
	global skipper
	del pine[:]
	del hlink[:]

	for y in range(downer):
		print ("attempt=" + str(y) + "/" + str(downer))
		DGD_Screen.execute_script("window.scrollBy(0," + str(100) + ")")
		if y < skipper:
			print ("skipper said not yet.")
			time.sleep(1);
		else:
			gram_href_grabber()
			print (str(len(hlink)) + " hlink vacuumed.")

#############################################################
###### caller : do DGD_ down
###### behave : crawl, dl, and if needed, reboot browser
#############################################################
def gram_accessor(address, dpot):
	global heardy, lis
	ret = 0
	print ("************************browse = " + address)
	DGD_Screen.get(address) #navigate to the page
	crawl_them_all(dpot)
	print (str(len(hlink)) + " pot torched. your proceed preference is " + res)
	if res == "n":
		print ("we've torched what's lost and what we grew")
		return 72
	else:
		xp = 1
		yp = 1
		for xurl in hlink:
			print ("sig_check:", heardy)
			if heardy == 1:
				heardy = 0
				break
			if yp > 36:
				down_pot_rotator()
				yp = 1
			print ("************************browse = " + xurl)

			DGD_Screen.get(xurl) #navigate to the page
			print ("[xattempt__]" + str(xp) + "/" + str(len(hlink)) + " cat=" + cat + " " + str(cax) + "/"+ str(totalcats))
			gram_src_grabber()
			while gram_click_obsessor() == 0:
				print ("★")
				gram_src_grabber()
			print("★Scraper Gone. BTW, DGD's CAT=", cat)
			xp+=1
			yp+=1

	#why ite? because
	#if u do quit after
	#user input, then
	#broken pipe error occurred
	#since it cannot recognize browser anymore.
	#DGD_Screen.quit()#please close your eyes when this emit error it is not mine but selenium......!
	print("wild mode will close it. otherwise, u should close it manually.")


	if res == "ask":
		p = "";
		p = input("do you want to proceed? y=yeah d=double a=another? otherwise=cancel? ")
		print ("used last string of:", p)
		p = p[-1:]
		if p == "y":
			for DGD_Address in pine:
				harvester(DGD_Address)
		elif p == "d":
			for DGD_Address in pine:
				harvester(DGD_Address)
			ret = 1
		elif p == "a":
			ret = 1
		else:
			print("dl canceled.")
	if res == "please":
		for DGD_Address in pine:
			harvester(DGD_Address)
		DGD_Screen.quit()#please close your eyes when this emit error it is not mine but selenium......!
		
	return ret#multi return is one of py-py-beauty

#############################################################
######  caller: Main per DGD_
######  behave: make browser for da DGD_
#############################################################
def doDGD_down(name):
	global DGD_Screen
	global basedir
	bd = "u_" + name
	basedir = bd

	print ("******")
	print ("DGD_base=", basedir)
	print ("******")

	#browser = webdriver.Firefox() #replace with .Firefox(), or with the browsing-machine of your choice
	DGD_Screen = webdriver.Firefox(executable_path=r'../../geck/gecko/geckodriver')
	DGD_Screen.set_window_size(1080, 680)
	#url = "https://www.instagram.com/" + name
	#y not
	url = name
	#	act+=1
	rc = gram_accessor(url, int(down))#fuzzy exit velocity in the
	#scroller behaviour, ton of fuzzy attempt from your side will end up eating it all 
	#print ("gram accessor done, DGD_Sc Quit After 5 Sec.")
	if rc == 1:
		randomy()
######
######
######m
######a
######i
######n
######
######w
######i
######l
######l
######
######s
######t
######a
######r
######t
######
######
######
######
######
######

#############################################################
######  M A I N
#############################################################
DGD_Screen = ''
last_percent_reported = 0
print ("user_agent_masquerade=" + MyOpener.version)
mop = MyOpener()
######main [hey-this-is-inst-gram-pot-ver]
#global val
hlink = []
pine = []
######approximate return amount
#this is up to your browsing-machine health, instagram health, and web world health
######down 100 will get  60 pot
######down 200 will get 120 pot
######down 300 will get 180 pot
######down 400 will get 240 pot
######down 500 will get 300 pot
######down   1 will get  12 'virgin' pot and it will be latest post
######down   0 will mess up so never use
down = 20
skipper = -1

res = "No Good. Please don't."
cat = "cat"
basedir = "pot"
totalcats = 0
cax = 0

def randomy():
    global res, cat
    f = open('where.csv', 'r',encoding='utf-8')
    reader = csv.reader(f)
    header = next(reader)
    #fruits = ['url_dummy[spl]cat_dummy']
    fruits = []
    for row in reader:
        fruits.append(row[0]+"[spl]"+row[2])
    f.close()
    rand = randrange(len(fruits))
    spl = fruits[rand].split("[spl]")
    res = "ask"#########if you want to dl u must do this
    cat = spl[1]
    doDGD_down(spl[0])
    print("please review da DGD's category in CSV data file, which are really suit for it?")
    #time.sleep(5)




def category_bulk(rmode):
    global res, cat, cax, totalcats
    #######################csv read
    #######################get category candidate
    f = open('where.csv', 'r',encoding='latin-1')
    reader = csv.reader(f)
    header = next(reader)
    fruits = []
    rbak = "＊"
    gcn = 0
    for row in reader:
            #if fruits[-1] != row[2]:
            if rbak != row[2]:
                    fruits.append(rbak + "@" + str(gcn))
                    rbak = row[2]
                    gcn = 0
            gcn = gcn + 1
    fruits.append(rbak + "@" + str(gcn))


    f.close()
    for x in range(len(fruits)):
            spx = fruits[x].split("@")

            print (str(x)+"="+spx[0]+"("+spx[1]+")", end='  ')
    #p = raw_input("which cat you take? all is all. ")
    p = input("which cat you take? all is all. ")
    #######################DGD_ read
    res = rmode
    f = open('where.csv', 'r',encoding='latin-1')
    reader = csv.reader(f)
    header = next(reader)
    ######################execution, you should f7 if u r in debug-pots
    ######################execution, you should f7 if u r in debug-pots
    ######################execution, you should f7 if u r in debug-pots
    ######################execution, you should f7 if u r in debug-pots
    ######################execution, you should f7 if u r in debug-pots
    ######################execution, you should f7 if u r in debug-pots
    ######################execution, you should f7 if u r in debug-pots
    cax = 1
    spx = fruits[int(p)].split("@")
    totalcats = spx[1]
    for row in reader:
            #print row[0]
            if p == "all":
                    cat = row[2]
                    doDGD_down(row[0])
            else:
                    if spx[0] == row[2]:
                            cat = row[2]
                            doDGD_down(row[0])
                            cax = cax + 1
    f.close()



######################################
###### M A I N #######################
######################################
######################################
p = input("**************\ne signal boots nautilus.\nt signal will down it.\n*********\nrandom-fun? y=yeah b=bulky otherwise=wild? ")

if p == "y":
    randomy()
elif p == "b":
    category_bulk("ask")
else:
    print("this is real bulky mode.")
    category_bulk("please")


print("all done＊")




