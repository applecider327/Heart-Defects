# For mass classification.

# As mentioned, the idea is to train a model with an appropriate train set. The train set should look like this:

feature_set = 
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

# It is a list of tuples, each of which is of a form (dictionary_of_features, label). To create one we'll need to start with a list of raw texts
# that look like the following:

set_of_texts = 
["title_here. body_sentence1_here. body_sentence2_here. body_sentence3_here.",
 "title_here. body_sentence1_here. body_sentence2_here. body_sentence3_here.",
 "title_here. body_sentence1_here. body_sentence2_here. body_sentence3_here."]
 
# Now the objective is to create a function called key_features such that

f_series = pd.Series(set_of_texts).apply(key_features)

# results in

0   {'title_keyword': 'Alagille Syndrome', 'title_...
1   {'title_keyword': 'Tetralogy of Fallot', 'title_...
2   {'title_keyword': 'Nothing', 'title_...

# so that the following line of code 

[pair for pair in zip(list(f_series), ["Alagille Syndrome", "Tetralogy of Fallot", "Romano-Ward Syndrome"])]

# gives the feature_set.


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

