#isgr-clipper
#written by lshash based on code at
#https://gist.github.com/marcoqu/e17e1c4414f8d18e6672976d941161fa

import time
import re
import md5
import requests
import json

import os
import urllib
import io
import datetime

######.
INSTAGRAM_URL = "https://www.instagram.com"
HASHTAG_ENDPOINT = "/graphql/query/?query_hash={}&variables={}"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
ACCESS_C = 24

######hash-tag/account?mode based.

######next page shot
def get_params(pots, end_cursor, mode, accnum, amount):
	if mode == 0:
		return '{{"tag_name":"{}","first":{},"after":"{}"}}'.format(pots, amount, end_cursor)
	if mode == 1:
		return '{{"id":"{}","first":{},"after":"{}"}}'.format(accnum, amount, end_cursor)



######json request
def get_next_page(csrf_token, ig_gis, query_id, params, mode):
	cookies = make_cookies(csrf_token)
	headers = make_headers(ig_gis)

	url = INSTAGRAM_URL + HASHTAG_ENDPOINT.format(query_id, params)

	print "request_url=" + str(url)

	req = requests.get(url, headers=headers, cookies=cookies)
	req.raise_for_status()
	json_obj = req.json()


	return post_makeup(json_obj['data'], mode), ec_makeup(json_obj['data'], mode)




######home page shot

######top html
def htmlcall(resty, mode):#init0
	if mode == 0:
		return requests.get(INSTAGRAM_URL + "/explore/tags/{}/".format(resty), headers={"user-agent": USER_AGENT})
	if mode == 1:
		return requests.get(INSTAGRAM_URL + "/{}/".format(resty), headers={"user-agent": USER_AGENT})



######json scraper, graphql makeup by Top Htm , 1 shot
def GraphqlMakeup(html, mode):#init2
	json_str = re.search(r'window._sharedData = (.*);</script>', html).group(1)
	json_obj = json.loads(json_str)

	if mode == 0:
		graphql = json_obj["entry_data"]["TagPage"][0]["graphql"]
	if mode == 1:
		graphql = json_obj["entry_data"]["ProfilePage"][0]["graphql"]



	return post_makeup(graphql, mode), ec_makeup(graphql, mode), uid_makeup(graphql, mode)



######js scraper by Top Htm , 1 shot
def get_query_id(html, mode):#init1
	if mode == 0:
		script_path = re.search(r'/static(.*)TagPageContainer\.js/(.*).js', html).group(0)
		script_req = requests.get(INSTAGRAM_URL + script_path)
		return re.findall('return e.tagMedia.byTagName.get\\(t\\).pagination},queryId:"([^"]*)"', script_req.text)[0]
	if mode == 1:
		script_path = re.search(r'/static(.*)ProfilePageContainer\.js/(.*).js', html).group(0)
		script_req = requests.get(INSTAGRAM_URL + script_path)

		print "plz let us write da javascript to file[see file]"
		with io.open('ppc.js','w',encoding='utf-8') as f:
			f.write(script_req.text)


		######*modify needed when index out of range*
		#################################################################################################
		#################################################################################################
		############query hash      there are 4 type for [account crawl]                         ########
		##################################for comment                                                ####
		##################################for profile                                                ####
		##################################for saved post                                             ####
		##################################for taggedpost not tagmedia                                ####
		#################################################################################################

		return re.findall('return null===\\([no]=e.profilePosts.byUserId.get\\(t\\)\\)\\|\\|void 0===[no]\\?void 0:[no].pagination},queryId:"([^"]*)"', script_req.text)[0]


#json detail seeker
def post_makeup(json_obj, mode):
	if mode == 0:
		edges = json_obj['hashtag']['edge_hashtag_to_media']['edges']
	if mode == 1:
		edges = json_obj['user']['edge_owner_to_timeline_media']['edges']

	return [o['node'] for o in edges]


#json detail seeker
def ec_makeup(json_obj, mode):
	if mode == 0:
		return json_obj['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
	if mode == 1:
		#print json_obj
		return json_obj['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']


#json detail seeker
def uid_makeup(json_obj, mode):
	if mode == 0:
		return "this_is_hash_tag_grabber"
	if mode == 1:
		#print json_obj
		return json_obj['user']['id']



######main routine
def scrape_pot(interesty, md, sleep=3):

	"""
	Yields scraped posts, one by one
	"""

	######init
	first_page = htmlcall(interesty, md)#init0
	query_id = get_query_id(first_page.text, md)#init1
	print "qid=" + query_id
	#home_posts = gpfh(first_page.text, md)
	home_posts, end_cursor, userid = GraphqlMakeup(first_page.text, md)#init2
	print "end-cur=" + str(end_cursor)
	for post in home_posts:
		print "home-page-play, ctl+c u can cancel this session......"
		yield post


	######for extra access
	csrf_token = get_csrf_token(first_page.cookies)#common
	rhx_gis = get_rhx_gis(first_page.text)#common
	#end_cursor = get_end_cursor_from_html(first_page.text)#common
	while end_cursor is not None:
		print "cursor-page-come, ctl+c u can cancel this session......"
		params = get_params(interesty, end_cursor, md, userid, ACCESS_C)#un common
		ig_gis = get_ig_gis(rhx_gis, params)
		posts, end_cursor = get_next_page(csrf_token, ig_gis, query_id, params, md)
		for post in posts:
			yield post
		time.sleep(sleep)


######common.
def get_csrf_token(cookies):
	return cookies.get("csrftoken")


def get_rhx_gis(html):
	return re.search(r'rhx_gis":"([^"]*)"', html).group(1)

def get_end_cursor_from_html(html):
	return re.search(r'end_cursor":"([^"]*)"', html).group(1)



def get_ig_gis(rhx_gis, params):
	return md5.new(rhx_gis + ":" + params).hexdigest()


def make_cookies(csrf_token):
	return {
		"ig_pr": "2",
		"csrftoken": csrf_token,
	}

def make_headers(ig_gis):
	return {
		"x-instagram-gis": ig_gis,
		"x-requested-with": "XMLHttpRequest",
		"user-agent": USER_AGENT
	}


#We grab the media with urllib
def save_pics(xid, xurl, xdir, typen, upt):
	fullfilename=os.path.join(xdir,str(upt) + typen + xid + ".jpg")
	if os.path.exists(fullfilename):
		print "already got"
	else:
		print("touching="+xurl)
		urllib.urlretrieve(xurl,fullfilename)

#We grab the media with urllib
def save_vids(xid, xurl, xdir, upt):
	fullfilename=os.path.join(xdir,str(upt) + "_vidpot_" + xid + ".mp4")
	if os.path.exists(fullfilename):
		print "already got"
	else:
		print("touching="+xurl)
		urllib.urlretrieve(xurl,fullfilename)


def gett(t):
	return datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

# main
mode = raw_input("hashtag[0]? or user?[1] ")
targ = raw_input("name? ")
mate = raw_input("how many material are you plan to clip? ")

if mode == "0":
	sdir = "#_" + targ
elif mode == "1":
	sdir = "u_" + targ
else:
	print "can't handle sorry"
	exit(72)

if not os.path.exists(sdir):
	os.makedirs(sdir)


act = 0
for post in scrape_pot(targ, int(mode)):

	uplt = gett(post['taken_at_timestamp'])#guess
	print "act " + str(act)

	if post['__typename'] == "GraphImage":
		print "basic"
		act+=1
		save_pics(post['id'], post['display_url'], sdir, "_basic_", uplt)
	if post['__typename'] == "GraphVideo":
		print "vid_pot"
		act+=1
		save_vids(post['id'], post['video_url'], sdir, uplt)
	if post['__typename'] == "GraphSidecar":
		#save_pics(post['id'], post['display_url'], sdir, "sc")
		sidecar_nodes = post['edge_sidecar_to_children']['edges']
		for subpost in sidecar_nodes:
			print "sub_sc"
			act+=1
			save_pics(subpost['node']['id'], subpost['node']['display_url'], sdir, "_scsub_", uplt)






