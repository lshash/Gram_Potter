######################################################################################
######  GramPotter by lsash   25/6/2018  #############################################
######################################################################################
######  some scraper that virtually touchable for any mat  ###########################
######################################################################################

from selenium import webdriver

import sys
import os
import urllib

def harvester(yurl):
	if not os.path.exists(basedir):
		os.makedirs(basedir)

	f = os.path.basename(yurl)
	fullfilename = os.path.join(basedir, f)

	if os.path.exists(fullfilename):
		print "[exist---ed]u r already pacman aren't u?"
	else:
		print("[toach-able]" + yurl)
		urllib.urlretrieve(yurl, fullfilename)



def url_scooper(u):
	print "************************browse = " + u
	browser.get(u) #navigate to the page



def gram_click_obsessor():
	for elem in element_scooper("//a"):
		x = elem.get_attribute("class")#since selenium xpath doesn't return att directly
		if "Righ" in x:
			print "let us tick"
			elem.click()
			return 0

	return 72

def gram_src_grabber():
	js_potter(0)
	for elem in element_scooper("(//img|//video)"):
		x = elem.get_attribute("src")#since selenium xpath doesn't return att directly
		if "inst" in x:
			harvester(x)


def gram_href_grabber():
	js_potter(0)
	for elem in element_scooper("//a"):
		x = elem.get_attribute("href")#since selenium xpath doesn't return att directly
		if "/p/" in x:
			if x not in hlink:
				print "scraper_interest=" + (x)
				hlink.append(x)



######url_refresher?
######hervester?
######clicker?

#?loop harvest-able? click-able?
######jsp
######scooper
#?



def js_potter(b):
	innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
	if(b == 1):
		print "%%%%%%B U G G Y %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
		print innerHTML.encode('utf-8')
		print "%%%%%%B U G G Y - E D .%%%%%%%%  plz define your scraper direction  %%%%%%%%%%%%%%%%"


def element_scooper(ele):# get elements 4 deepen pot
	return browser.find_elements_by_xpath(ele)# return web element, this is clickable sometimes



def go_down_obsessor(d):
	browser.execute_script("window.scrollBy(0," + str(d) + ")")


def crawl_them_all(downer):
	for y in range(downer):
		go_down_obsessor(50)
		gram_href_grabber()


def gram_accessor(address, dpot):
	url_scooper(address)

	crawl_them_all(dpot)
	
	print str(len(hlink)) + " pot toached. your proceed preference is " + res

	if res == "n":
		print "terminator"
		return 72
	else:
		for xurl in hlink:
			url_scooper(xurl)
			gram_src_grabber()

			while gram_click_obsessor() == 0:
				gram_src_grabber()

	return 0




######main [hey-this-is-inst-gram-pot-ver]
#global val
hlink = []

######approximate return amount
#this is up to your browser health, instagram health, and web world health
######down 100 will get  60 pot
######down 200 will get 120 pot
######down 300 will get 180 pot
######down 400 will get 240 pot
######down 500 will get 300 pot
######down   0 will get  12 'virgin' pot and it will be latest post
down = 50
res = "n"
if len(sys.argv) == 4:
	name = sys.argv[1]
	down = sys.argv[2]######plz input 0 for latest-update-only-grabber
	res  = sys.argv[3]

elif len(sys.argv) == 3:
	name = sys.argv[1]
	down = sys.argv[2]######plz input 0 for latest-update-only-grabber

elif len(sys.argv) == 2:
	name = sys.argv[1]
else:
	name = raw_input("name?")

basedir = "u_" + name
xbuggy = 2#for unbuggy u should define unreachable number [outside from -1 to your max grab]#depricated
act = 0

browser = webdriver.Firefox() #replace with .Firefox(), or with the browser of your choice
browser.set_window_size(1080, 680)

url = "https://www.instagram.com/" + name
#	act+=1


gram_accessor(url, int(down))#fuzzy exit velocity in the scroller behaviour, ton of fuzzy attempt from your side will end up eat it all 



browser.quit()#please close your eyes when this emit error it is not mine but selenium......!



