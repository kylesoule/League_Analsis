import json
import twitter

consumer_key = "shPOAAxu9r6FLWeAcn4zqhnJK"
consumer_secret = "L3NZ9SkgFHsfJRg7pQHRqZknmbXTdfb7D9f8rMeBX1XqJEX3Kz"
access_key = "752977686578892800-yoJdbsW6QkDrMZ4Dr1CRIPPRo07yHUp"
access_secret = "iVeNmCw1iDZQxaeO0VpSnoydgc2cOAcnFCIu3HbOjKw6n"

api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                  access_token_key=access_key, access_token_secret=access_secret)

id = 0
words = []
results = api.GetUserTimeline(screen_name="realDonaldTrump", count=200)
for status in results:
    j = json.loads(str(status))
    
    if id == 0:
        id = int(j["id"])
    else:
        if int(j["id"]) < id:
            id = int(j["id"])
    
    try:
        fav_count = j["favorite_count"]
    except:
        fav_count = "MISSING"
    
    #print("{id}\t{f}\t{c}".format(id=j["id"], c=j["created_at"], f=fav_count))
    tweet = j["text"].encode('utf-8')
    words.append(tweet.split(" "))
    #print("{tweet}".format(tweet=j["text"].encode('utf-8')))

print words
#print id