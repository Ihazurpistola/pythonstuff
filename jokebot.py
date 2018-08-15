import praw
import config
import time
import os
import requests

def bot_login():
	print ("Logging in")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Mats joke comment responder")
	print ("Logged in")
	return r

def run_bot(r, comments_replied_to):
	print ("Searching....")

	for comment in r.subreddit('testingground4bots').comments(limit=10):
		if "!joke" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
			print ('String with \"!joke\" found in the comment ' + comment.id)

			comment_reply = "You requested a joke! Here it is:\n\n"

			joke = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']

			comment_reply += ">" + joke

			comment.reply(comment_reply)
			print ('Replied to comment ' + comment.id)

			comments_replied_to.append(comment.id)

			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	print ("Nothing there, sleeping for 30 seconds...")
	#Sleep for 10 seconds....
	time.sleep(30)

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split ("\n")
	return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print (comments_replied_to)

while True:
	run_bot(r, comments_replied_to)