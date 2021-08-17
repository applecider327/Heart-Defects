# Here the idea is to train a model with an organised training set, which should look something like the following:

train_set = 
[({'title_keyword': 'Alagille Syndrome',
   'title_description': 'Nothing',
   'body_keyword': 'Alagille Syndrome',
   'body_description': 'Nothing'},
  'Alagille Syndrome'),
 ({'title_keyword': 'Tetralogy of Fallot',
   'title_description': 'Nothing',
   'body_keyword': 'Nothing',
   'body_description': 'Nothing'},
  'Tetralogy of Fallot'),
 ({'title_keyword': 'Nothing',
   'title_description': 'Nothing',
   'body_keyword': 'Romano-Ward Syndrome',
   'body_description': 'Nothing'},
  'Romano-Ward Syndrome')]

# It is a list of tuples, each of which is of a form (dictionary of features, label). The task of mapping a label to each text piece in a massive scale 
# cannot be done automatically, and this is why preparing a training set of Y's and X's is unfeasible. There is a way to extract features (the X's) automatically,
# though, and below is all about that.



# Start with a list of raw texts that look like the following:

set_of_texts = 
["title_here. body_sentence1_here. body_sentence2_here. body_sentence3_here.",
 "title_here. body_sentence1_here. body_sentence2_here. body_sentence3_here.",
 "title_here. body_sentence1_here. body_sentence2_here. body_sentence3_here."]
 
# Now the objective is to create a function called key_features such that

f_series = pd.Series(set_of_texts).apply(key_features)

# gives the following feature set:

0   {'title_keyword': 'Alagille Syndrome', 'title_...
1   {'title_keyword': 'Tetralogy of Fallot', 'title_...
2   {'title_keyword': 'Nothing', 'title_...

# Below is the key_features function:

def key_features(text):
    features = {}
    title = nltk.sent_tokenize(text)[0]
    features["title_keyword"] = list(by_keywords(title).index)[0]
    features["title_description"] = "Nothing"
                   
    if len(nltk.sent_tokenize(text)) >= 2:
       body = nltk.sent_tokenize(text)[1:]
       features["body_keyword"] = list(by_keywords(" ".join(body)).index)[0]
       features["body_description"] = list(by_description(" ".join(body)).index)[0]
    else: 
       features["body_keyword"] = "Nothing"
       features["body_description"] = "Nothing"
               
    return features
