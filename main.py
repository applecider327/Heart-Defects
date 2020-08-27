# Where 

def by_description(text):
    series = pd.Series(nltk.sent_tokenize(text.lower()))
    return series.apply(describes_what).value_counts()
