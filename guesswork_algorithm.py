# Guesswork-derived algorithm.

# Accepts a string object of at least one sentence. The first sentence is deemed as the title part and the rest, if any, are all considered to be the body part. 
# The first sentence must be followed by a full stop (.). See below for details.
# Required: pandas, nltk, by_keywords, by_description

def hd_type(full_text): 
    title = nltk.sent_tokenize(full_text)[0] # separate title from the rest
    from_title = list(by_keywords(title).index)[0:] # any keyword spotted in the title?
    if from_title != "Nothing": # if there is,
        if len(from_title) == 1: # and if there's only one,
            return from_title # return it
    
    if len(nltk.sent_tokenize(full_text)) >= 2: # if there's body part as well
        body = nltk.sent_tokenize(full_text)[1:] # separate body from the title
        from_rest_by_key = list(by_keywords(" ".join(body)).index)[0] # keyword with the most appearance, if any
        if from_rest_by_key != "Nothing": # if there is,
            return from_rest_by_key # return it
    
        from_rest_by_desc = list(by_description(" ".join(body)).index)[0] # description with the most appearance, if any
        if from_rest_by_desc != "Nothing": # if there is,
            return from_rest_by_desc # return it
    
    if len(from_title) >= 2: # if there's two keywords found in the title and the body part is missing
        return from_title # call it a draw
    
    return "No match found" # if there's no information at all to be gained from anywhere
    
# Example 1
# hd_type("Watson-Miller Syndrome and Chronic Arthritis: An International Case Series. We describe 10 children with Alagille syndrome and inflammatory arthritis. 
#         In our centers, the prevalence of chronic arthritis in patients with Alagille syndrome is approximately 50 times higher compared with the general 
#         population. Arthritis was refractory to most treatment. Patients with Alagille syndrome should routinely be screened for musculoskeletal symptoms.")

# ['Alagille Syndrome']

# Example 2
# hd_type("Anaesthesia concerns and perioperative management in a child with DiGeorge syndrome with corrected tetralogy of Fallot with pulmonary atresia posted 
# for aparoscopic orchidopexy: Case report. DiGeorge syndrome is afflicted with multiple congenital anomalies such as conotruncal and craniofacial anomaly, 
# immune system dysfunction and hypoplasia/aplasia of parathyroid glands. Laparoscopy is a preferred surgical approach over open orchidopexy due to better 
# visualisation of impalpable testis avoiding long incision, minimal tissue damage and a faster recovery. We report a case of DiGeorge syndrome with corrected 
# tetralogy of Fallot with pulmonary atresia in a 1-year-old male child posted for laparoscopic orchidopexy. The anaesthesiologists face unique challenges due to 
# the multisystem involvement and the effects of laparoscopic surgery on multiple organs. Thorough understanding of DiGeorge syndrome is essential for a good 
# perioperative outcome.")

# ['DiGeorge Syndrome']

# Example 3

# hd_type("A case report - WPW Syndrome vs Romano Ward Syndrome")
# ['Wolff-Parkinson-White Syndrome', 'Romano-Ward Syndrome']

# Example 4

# hd_type("Case report: patients with severe heart underdevelopment. We introduce a patient whose left side of the heart has been severly underdeveloped.")
# ['Hypoplastic Left Heart Syndrome']

# Example 5
# hd_type("Fetal phenotypes emerge as genetic technologies become robust.")
# 'No match found'
