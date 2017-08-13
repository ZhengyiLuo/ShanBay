import requests
import json
import re
access_token = "pEU2QXajcjMk382BTB4PWjTIiejaUQ"  #Swap this with your Shanbay Token

def addWord(word):
	print "adding word: " + word
	try:
		idStr = requests.get("https://api.shanbay.com/bdc/search/?word="+word+"&access_token=" + access_token)
		result = json.loads(idStr.text)
		wordId = 0
		if "data" in result:
			wordId = result["data"]["id"]
		else:
			print("Invalid Word") 
			return False

		add = requests.post('https://api.shanbay.com/bdc/learning/?access_token' + access_token, data = {'id':wordId})
		addresult = json.loads(add.content)
		if "msg" not in addresult or addresult["msg"] != "SUCCESS":
			print("Failed at Adding Word") 
		return True

	except Exception as e:
		print e
		return False


if __name__ == "__main__":
	f = open("words.txt")
	for l in f.readlines():
		if not re.match(r'^\s*$', l):
			res = addWord(l.strip())
			if res:
				pass
			else:
				while not addWord(l.strip()):
					continue

