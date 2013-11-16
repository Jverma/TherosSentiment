Files : 

1. test.py 
This in the mail file, which when executed (as explained below) will return a corpus of tweets relevant to the search query. 

2. bs.txt 
Initially it contains a JSON-encoded dictionary with cards as keys and 1 as default values. The script alpha.py will update this everyday. 

3. alpha.py 
This extracts the metadata from the tweets obtained by running test.py. We use this to save the ids of the last tweet obtained on any day. 



Steps to Execute : 

1. Enter Your access_token_key, access_token_secret, consumer_key, consumer_secret in test.py (lines 10, 11, 13, 14)

2. type python test.py bs.txt > output.txt on command line
This will create an output json file containing recent 100 search results for the keywords taken from bs.txt 

3. type python alpha.py output.txt > bs.txt
This will replace the dictionary in bs.txt by one containing cards as keys and the last tweet_id as the value. 

4. Un-Comment line 67 and 68 in test.py
This will now take tweet_ids into account. 

5. Now repeat step 2 and 3 everyday. Make sure to create a new output file everyday and run alpha.py on this new file. bs.txt can be used again and again as we don't need to save that information. 