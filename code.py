# from nltk.tokenize import _treebank_word_tokenizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

data = "great"
small = data.lower()
tokenized = small.split(' ')
final =[]
for word in tokenized:
    if word not in stopwords.words("english"):
        final.append(word)

def take_words(element):
    response ={}
    count =0
    for i in element:
        sub = i.review
        sub = sub.lower()
        sub1 = (sentinment_analyse(sub))
        response[count] = sub1
        print(response[count])
        count=count+1
         
    return(response)           
        

def sentinment_analyse(sample):
    score = SentimentIntensityAnalyzer().polarity_scores(sample)
    pos = score['pos']
    neg = score['neg']
    neu = score['neu']
    if(pos>=neg) and (pos>=neu):
        return("positive")
    elif(neg>=pos) and (neg>=neu):
        return("negative")
    else:
        return("neutral")        
        

