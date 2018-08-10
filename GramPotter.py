######################################################################################
######  GramPotter by lsash   25/6/2018  #############################################
######################################################################################
######  some scraper that virtually touchable for any mat  ###########################
######################################################################################

from selenium import webdriver

import sys
import os, io
#import urllib
from urllib import FancyURLopener

import httplib

def harvester(yurl):
	if not os.path.exists(basedir):
		os.makedirs(basedir)

	f = os.path.basename(yurl)
	fullfilename = os.path.join(basedir, f)

	if os.path.exists(fullfilename):
		print "[exist---ed]u r already pac-pot aren't u?"
	else:
		if "efg=" in fullfilename:
			print("[efg_suspic]" + yurl)
		else:
			print("[torch-able]" + yurl)
			#urllib.urlretrieve(yurl, fullfilename)
			mop.retrieve(yurl, fullfilename)


#http://wolfprojects.altervista.org/articles/change-urllib-user-agent/
#print URLopener.version

class MyOpener(FancyURLopener):
	version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/604.1.31 (KHTML, like Gecko) Version/11.0 Safari/604.1.31'

print "user_agent_masquerade=" + MyOpener.version

mop = MyOpener()




def down_pot_rotator(wd):
	print "******down pot, memory release is way to go"
	try:
		wd.quit()#please close your eyes when this emit error it is not mine but selenium......!
	except:
		print "caught"
	wd = webdriver.Firefox() #replace with .Firefox(), or with the browsing-machine of your choice
	wd.set_window_size(1080, 680)

	return wd

def url_scooper(wdr, u):
	print "************************browse = " + u
	wdr.get(u) #navigate to the page



def gram_click_obsessor(lob):
	#for elem in element_scooper("//div[@class='rg_meta notranslate']"):
	for elem in element_scooper(lob, "//a"):
		x = elem.get_attribute("class")
		if "Righ" in x:
			print "let us tick"
			elem.click()
			return 0

	return 72

def gram_src_grabber(lob):
	js_potter(lob, 0)
	for elem in element_scooper(lob, "(//img|//video)"):

		try:
			x = elem.get_attribute("src")#
			if "inst" in x:
				harvester(x)
		except:
			print "wat da for we imgvid?"
			js_potter(lob, 1)


def gram_href_grabber(lob):
	js_potter(lob, 0)
	for elem in element_scooper(lob, "//a"):
		x = elem.get_attribute("href")#
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



def js_potter(b, dboggy):
	innerHTML = b.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
	if(dboggy == 1):
		#print "%%%%%%B U G G Y %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
		#print innerHTML.encode('utf-8')
		#print "%%%%%%B U G G Y - E D .%%%%%%%%  plz define your scraper direction  %%%%%%%%%%%%"

		print "[analyse pot]  time 4 u to stop by ctrl c to see pot 4 ur better perceptron "
		with io.open('innerht.txt','w',encoding='utf-8') as f:
			f.write(unicode(innerHTML))



def element_scooper(br, ele):# get elements 4 deepen pot

	stat = 0
	while stat == 0:
		try:
			we = br.find_elements_by_xpath(ele)# return web element, this is clickable sometimes
			stat = 1
		except httplib.BadStatusLine:
			print "da line status seems bad."

	return we


def go_down_obsessor(bs, d):
	bs.execute_script("window.scrollBy(0," + str(d) + ")")


def crawl_them_all(brs, downer):
	for y in range(downer):
		print "attempt=" + str(y) + "/" + str(downer)
		go_down_obsessor(brs, 100)
		gram_href_grabber(brs)


def gram_accessor(address, dpot, b):
	lb = b
	url_scooper(lb, address)

	crawl_them_all(lb, dpot)
	
	print str(len(hlink)) + " pot torched. your proceed preference is " + res

	if res == "n":
		print "we've torched what's lost and what we grew"
		return lb, 72
	else:
		xp = 1
		yp = 1
		for xurl in hlink:
			if yp > 20:
				lb = down_pot_rotator(lb)
				yp = 1
			url_scooper(lb, xurl)

			print "[xattempt__]" + str(xp) + "/" + str(len(hlink))
			gram_src_grabber(lb)

			while gram_click_obsessor(lb) == 0:
				print "clicked done normally but next src grab?"
				gram_src_grabber(lb)
			xp+=1
			yp+=1

	return lb, 0#multi return is one of py-py-beauty




######main [hey-this-is-inst-gram-pot-ver]
#global val
hlink = []

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

browser = webdriver.Firefox() #replace with .Firefox(), or with the browsing-machine of your choice
browser.set_window_size(1080, 680)

#url = "https://www.instagram.com/" + name
#y not
url = name
#	act+=1


latest_bro, rc = gram_accessor(url, int(down), browser)#fuzzy exit velocity in the scroller behaviour, ton of fuzzy attempt from your side will end up eat it all 


try:
	latest_bro.quit()#please close your eyes when this emit error it is not mine but selenium......!
except:
	print "quitty fail, this is selenium things, not mine......!"




