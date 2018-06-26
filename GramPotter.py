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
		print "[exist---ed]"
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
	atts = []
	for elem in element_scooper("//a"):
		x = elem.get_attribute("href")#since selenium xpath doesn't return att directly
		if "/p/" in x:
			print "scraper_interest=" + (x)
			atts.append(x)

	return atts


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



def go_down_obsessor(d, a):
	for y in range(d):
		browser.execute_script("window.scrollBy(0," + str(a) + ")")


def gram_accessor(address, downer, damount):
	url_scooper(address)
	go_down_obsessor(downer, damount)

	xurls = gram_href_grabber()
	for xurl in xurls:
		url_scooper(xurl)
		gram_src_grabber()

		while gram_click_obsessor() == 0:
			gram_src_grabber()



######main [hey-this-is-inst-gram-pot-ver]
if len(sys.argv) == 2:
	name = sys.argv[1]
else:
	name = raw_input("name?")

basedir = "u_" + name
xbuggy = 2#for unbuggy u should define unreachable number [outside from -1 to your max grab]#depricated
act = 0

browser = webdriver.Firefox() #replace with .Firefox(), or with the browser of your choice
url = "https://www.instagram.com/" + name
#	act+=1


gram_accessor(url, 400, 100)#fuzzy exit velocity in the scroller behaviour



browser.quit()#please close your eyes when this emit error it is not mine but selenium......!



