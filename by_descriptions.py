# As mentioned in the README file sometimes it's the descriptions that come into play. 

# Helper Function 1
# what it does: identify the heart defect type in question given a sentence of its description. takes use of description_patterns (refer to description_patterns.py)
# and search_id_k from fetching_terms_and_descriptions.

def describes_what(sent):
    n = [description_patterns.index(each) for each in description_patterns if len(re.findall(str(each[0]), sent)) != 0]
    if n == []:
        return None
    return search_id_k(ids[n[0]])[0]
    
