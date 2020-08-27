# As mentioned in the README file the system looks for keywords. Here's how I went about building one. The required libraries are: itertools, nltk, re, and pandas.

# Helper Function 1
# what it does: accepts a string object, word-tokenise it, and return all possible n-grams (mostly pentagrams) in a list of lists format.

def ngram(string):
    to_iter = nltk.word_tokenize(string)
    if len(to_iter) < 5:
        n = len(to_iter)
    else:
        n = 5
    result = []
    i = 0
    while i+n <= len(to_iter):
        result.append(to_iter[i:i+n])
        i += 1 
    return result
  
# ngram("Hello there, how is it going")

'''
[['Hello', 'there', ',', 'how', 'is'],
['there', ',', 'how', 'is', 'it'],
[',', 'how', 'is', 'it', 'going']]
'''


# Helper Function 2
# what it does: takes use of the ngram function. accepts a string object and returns a series of every permutation for every pentagram.

def all_possible(string):
    string = re.sub('[,()]', ' ', string)
    final = [list(itertools.permutations(each)) for each in ngram(string)]
    flat = [item for sublist in final for item in sublist]
    return pd.Series(flat).map(list).str.join(" ")
  
# all_possible("For instance, you will see something like this.")

'''
0      For instance you will see
1      For instance you see will
2      For instance will you see
3      For instance will see you
4      For instance see you will
5      For instance see will you
6      For you instance will see
7      For you instance see will
8      For you will instance see
9      For you will see instance
10     For you see instance will
11     For you see will instance
12     For will instance you see
13     For will instance see you
14     For will you instance see
15     For will you see instance
16     For will see instance you
17     For will see you instance
18     For see instance you will
19     For see instance will you
20     For see you instance will
21     For see you will instance
22     For see will instance you
23     For see will you instance
24     instance For you will see
25     instance For you see will
26     instance For will you see
27     instance For will see you
28     instance For see you will
29     instance For see will you
                 ...            
570    this . see something like
571    this . see like something
572    this . something see like
573    this . something like see
574    this . like see something
575    this . like something see
576    . see something like this
577    . see something this like
578    . see like something this
579    . see like this something
580    . see this something like
581    . see this like something
582    . something see like this
583    . something see this like
584    . something like see this
585    . something like this see
586    . something this see like
587    . something this like see
588    . like see something this
589    . like see this something
590    . like something see this
591    . like something this see
592    . like this see something
593    . like this something see
594    . this see something like
595    . this see like something
596    . this something see like
597    . this something like see
598    . this like see something
599    . this like something see
Length: 600, dtype: object
'''


# Helper Function 3
# what it does: takes use of the 'd' dictionary object (found in the 'dictionary.py' file). accepts a string and see what head term is it associated with.

def which_cat(string):
    for key in d:
      for each in d[key]:
        if each.lower() in string.lower():
          return key
    return None
  
# which_cat("Siewert Syndrome")

# "Kartagener Syndrome"


# Main Function
# what it does: takes use of all the helper functions above. accepts a text and finds out every explicit use of head terms and their entry terms, along with all other
# implicit cases.

def by_keywords(text):
    return all_possible(text).apply(which_cat).value_counts()
  
# Example 1
# by_keywords("Case report: Andersen Syndrome")

# Andersen Syndrome    24
# dtype: int64

# Example 2
# by_keywords("We suspect that ALCAPA is in place. There is also a possibility for Watson-Miller Syndrome.")

# Bland White Garland Syndrome    480
# Alagille Syndrome                48
# dtype: int64

# Example 3
# by_keywords("We diagnosed a tetralogy defect (specifically, Fallot's).")

# Tetralogy of Fallot    48
# dtype: int64
