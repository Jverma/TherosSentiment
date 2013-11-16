import oauth2 as oauth
import urllib2 as urllib
import json




# See Assignment 1 instructions or README for how to get these credentials
access_token_key = "67781222-8QLayUx94IsmotU7RQXRSYPz1Oo3AEhpjPlMprc"
access_token_secret = "B8Xz9Ps36ZcWe14bdCRvRsVHfWqt3xjWtS1eHANHk"

consumer_key = "d4AisMgdWPZuXqkxge93A"
consumer_secret = "SGeYiSnnP4yM6ZJUfCH5OawDhIHHp8XJtAxBQKwzRU"

_debug = 0

oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  keywords = ["Battlewise Valor", "Cavalry Pegasus",
"Celestial Archon", 
"Chained to the Rocks",
"Chosen by Heliod",
"Dauntless Onslaught",
"Decorated Griffin",
"Divine Verdict",
"Elspeth, Sun's Champion",
"Ephara's Warden",
"Evangel of Heliod",
"Fabled Hero",
"Favored Hoplite",
"Gift of Immortality",
"Glare of Heresy",
"Gods Willing",
"Heliod, God of the Sun",
"Heliod's Emissary",
"Hopeful Eidolon",
"Hundred-Handed Ones",
"Lagonna-Band Elder",
"Last Breath",
"Leonin Snarecaster",
"Observant Alseid",
"Ordeal of Heliod",
"Phalanx Leader",
"Ray of Dissolution",
"Scholar of Athreos",
"Setessan Battle Priest",
"Setessan Griffin",
"Silent Artisan",
"Soldier of the Pantheon",
"Spear of Heliod",
"Traveling Philosopher",
"Vanquish the Foul",
"Wingsteed Rider",
"Yoked Ox",
"Aqueous Form",
"Artisan of Forms",
"Benthic Giant",
"Bident of Thassa",
"Breaching Hippocamp",
"Coastline Chimera",
"Crackling Triton",
"Curse of the Swine",
"Fate Foretold",
"Gainsay",
"Griptide",
"Horizon Scholar",
"Lost in a Labyrinth",
"Master of Waves",
"Meletis Charlatan",
"Mnemonic Wall",
"Nimbus Naiad",
"Omenspeaker",
"Ordeal of Thassa",
"Prescient Chimera",
"Prognostic Sphinx",
"Sea God's Revenge",
"Sealock Monster",
"Shipbreaker Kraken",
"Stymied Hopes",
"Swan Song",
"Thassa, God of the Sea",
"Thassa's Bounty",
"Thassa's Emissary",
"Triton Fortune Hunter",
"Triton Shorethief",
"Triton Tactics",
"Vaporkin",
"Voyage's End",
"Wavecrash Triton",
"Abhorrent Overlord",
"Agent of the Fates",
"Asphodel Wanderer",
"Baleful Eidolon",
"Blood-Toll Harpy",
"Boon of Erebos",
"Cavern Lampad",
"Cutthroat Maneuver",
"Dark Betrayal",
"Disciple of Phenax",
"Erbos, God of the Dead",
"Erebos's Emissary",
"Fellhide Minotaur",
"Fleshmad Steed",
"Gray Merchant of Asphodel",
"Hero's Downfall",
"Hythonia the Cruel",
"Insatiable Harpy",
"Keepsake Gorgon",
"Lash of the Whip",
"Loathsome Catoblepas",
"March of the Returned",
"Mogis's Marauder",
"Nighthowler",
"Ordeal of Erebos",
"Pharika's Cure",
"Read the Bones"]
  for x in keywords:
    x = str(x)
    url = "https://api.twitter.com/1.1/search/tweets.json?q="   
    url = url+x
    parameters = []
    response = twitterreq(url, "GET", parameters)
    for line in response:
      apple = json.loads(line)
      print apple
if __name__ == '__main__':
  fetchsamples()


	

 





    
