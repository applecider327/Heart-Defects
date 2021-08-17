# As mentioned in the README file sometimes it's the descriptions that come into play. Libraries required: nltk, re, and pandas.

# Helper Function 1
# what it does: identify the heart defect type in question given a sentence of its description. takes use of description_patterns (refer to description_patterns.py)
# and search_id_k from extracting_data. 

def describes_what(sent):
    n = [description_patterns.index(each) for each in description_patterns if len(re.findall(str(each[0]), sent)) != 0]
    if n == []:
        return None
    return search_id_k(ids[n[0]])[0]
    
# Example 1
# describes_what("We introduce a patient with the following four conditions: ventricular septal defect, right ventricular hypertrophy, overriding aorta, and pulmonary stenosis.")

# "Tetralogy of Fallot"

# Example 2
# describes_what("Her left coronary artery is connected to the pulmonary artery instead of the aorta.")

# "Anomalous Left Coronary Artery"

# Main Function
# what it does: basically an extension of describes_what; takes in a paragraph and looks at every sentence for the right description patterns and returns all match.
# note: any description that spans over two or more sentences won't be detected.

def by_description(text):
    series = pd.Series(nltk.sent_tokenize(text.lower()))
    if len(series.apply(describes_what).value_counts()) > 0:
        return series.apply(describes_what).value_counts()
    else:
        return pd.Series([0], index = ["Nothing"])

# Example 1
# by_description("We introduce a newborn with duplication of one of the chromosome 18s. There also seems to be a hole in the septum that usually separates the two lower chambers of a heart.")

# Trisomy 18 Syndrome                  1
# Heart Septal Defects, Ventricular    1
# dtype: int64
