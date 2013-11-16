import json
import sys


words_tweet_ids = {}
input = open(sys.argv[1])
count = 0
for line in input:
    count = count + 1
    data = json.loads(line)
    #print data.keys()
    tweets = data['statuses']
    #if (len(tweets) > 0):
     #   for x in tweets:
      #      print  count, x['id'], x['created_at']
    alpha = data['search_metadata']
    keyword = alpha['query']
    keyword = keyword.replace("+", " ")
    max_id = alpha['max_id']
    keyword = keyword.encode('utf-8')
    apple = {keyword : max_id}
    words_tweet_ids.update(apple)
    
#print type(words_tweet_ids)    
print json.dumps(words_tweet_ids)    
    
        
        
        
    
    
