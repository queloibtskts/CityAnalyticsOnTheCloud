from textblob import TextBlob
import os

class tweetTagger:
    
    def __init__(self, raw_tweet):
        self.analyseTweet(raw_tweet)  # Analysis
 
    def analyseTweet(self, raw_tweet):
        
        # Initialize tweet analysis
        tweet_analyser = tweetAnalyser(raw_tweet)
        
        # Topic Analysis
        topics = {}
        topics['vulgar_words'] = tweet_analyser.analyseVulgarWords()
        return topics

class tweetAnalyser:
    '''Tweet analysis functions.'''

    def __init__(self, raw_tweet):
        self.raw_tweet = raw_tweet
        self.blob = TextBlob(raw_tweet['text']) # PatternAnalyzer default

        hashtags_list = []
        for topic in self.raw_tweet['entities']['hashtags']:
            hashtags_list.append(topic['text'].lower())
        self.hashtags = set(hashtags_list)

        words_tokens = []
        for word in self.blob.words:
            words_tokens.append(word.lower())
        self.words = set(words_tokens)
        
        #categories = TermParser()
        self.vulgar_words = list(self.readtxt('../crawler/swear_word.txt'))
    
    def readtxt(self, path):
        '''Load vocabularies'''
        term = [] # e.g., vulgar words
        path = os.path.join(os.path.dirname(__file__), path)
        with open(path) as f:
            line = f.readline().strip()
            while line:
                term.append(line)
                line = f.readline().strip()

        f.close()
        return term

    
    def analyseVulgarWords(self):
        return self.containsTerms(self.vulgar_words)

    def hasHashtags(self, terms):
        '''Checks if tweet has any hashtags in the given list'''
        for hashtag in self.hashtags:
            for t in terms:
                if t in hashtag:
                    return True
        return False

    def hasWords(self, words):
        '''Checks if tweet has any words in the given list'''
        for word in words:
            if word in self.raw_tweet['text']:
                return True
        return False

    def containsTerms(self, terms):
        '''Checks if terms are in either topics or words'''
        return bool(self.hasHashtags(terms) or self.hasWords(terms))
