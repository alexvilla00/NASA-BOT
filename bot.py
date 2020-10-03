import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("GkSKcH3MdcMEfsGxEUNWzuAXA","DeuD2v9Zxg7teF3HknJUNaZSNmApk9vESEfJ5PP7DLlKwKirKG")
auth.set_access_token("1312298521161334784-XtkujR8oEpD0AwL0aUNl5ZyNYbCYtm","JkMSJ5EFIwXqCBPydC7ObRJnyhdhdtD7BGJZqmXt9D1Vv")

# Create API object
api = tweepy.API(auth)

# Create a tweet
#api.update_status("Hola mundo")

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
