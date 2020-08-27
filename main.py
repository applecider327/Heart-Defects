# Where everything comes together.

# The main function. Takes in a medicinal text and analyses to see what cogenital heart defect is being described. As of now the hierarchy goes: title > explicit 
# keyword found in the body text > implicit descriptions. This is likely subject to change. As of now it only accepts inputs in a format where the title is the very
# beginning sentence followed by a full stop (.).

def hd_type(full_text):
    title = nltk.sent_tokenize(full_text)[0]
    from_title = list(by_keywords(title).head(2).index)
    if len(from_title) > 0:
        return from_title
        
    from_rest_by_key = list(by_keywords(full_text).head(2).index)   
    if len(from_rest_by_key) > 0:
        return from_rest_by_key
    
    from_rest_by_desc = list(pd.Series(nltk.sent_tokenize(full_text)).apply(by_description).head(2).index)
    if len(from_rest_by_desc) > 0:
        return from_rest_by_desc
    
    return "No match found"
    
# Example 1
# hd_type("Case Report: Watson-Miller Syndrome. We present a 10-year-old patient previously diagnosed with 22q11 deletion syndrome.")

# ['Alagille Syndrome']

# Example 2
# hd_type("A study of connection between LEOPARD Syndrome and Marfan's Syndrome. A recent research at Johns Hopkins university suggests that...")

# ['Marfan Syndrome', 'LEOPARD Syndrome']

# Example 3

# hd_type("Ventricular defects in Cogenital Heart Defects. We present a patient with the following four conditions: pulmonary stenosis, ventricular septal defect, 
right ventricular hypertrophy, and overriding aorta.")

# ['Heart Septal Defects, Ventricular'] -> Would have been better labeled with "Tetralogy of Fallot". 
