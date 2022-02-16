import random
class Solution:
    def __init__(self):
        self.dic  = {}

    def encode(self, longUrl):
        # Encodes a URL to a shortened URL.
        CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while True:
            key = ''.join(random.sample(CHARS, 6))
            if not self.dic.get(key): 
                break
        self.dic[key] = longUrl
        return 'http://tinyurl.com/' + key


    def decode(self, shortUrl):
        # Decodes a shortened URL to its original URL.
        key = shortUrl[-6:]
        return self.dic[key]

# Your Codec object will be instantiated and called as such:
# Codec codec = new Codec();
# codec.decode(codec.encode(url));
