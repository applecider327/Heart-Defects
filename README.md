**Introduction**

This is an NLP project for automatically identifying which type of congenital heart defect is being described in a text such as a medical case report. This is a strategy for document classification. Given a set of case reports, we would like to be able to identiy the reports that involve instances of known congenital heart defects.

The idea is simple. A text is divided into two parts, the title and the body. For each component the system looks for key features (specifically, keywords and descriptions) and utilises this information collectively to come up with a final call. For instance, a keyword 'Tetralogy of Fallot' or its description maybe found either in the title or in the body part in a case report about 'Fallot's Tetralogy'.

These key features are then utilised to come up with the final decision. Now there are two ways for this:

**Guesswork-derived algorithm** 

In this case the key features are fed to an algorithm that I've personally designed. Common sense tells you that the title is the most important piece of information to determine what a text is going to be about, and that is the key idea of the algorithm.

**ML-derived algorithm**

Now this is the usual way. Python's NLTK offers a number of text classification algorithms. The idea is to train one of them (say, Naive Bayes Classifier) by feeding it an organised training set. The ML algorithm 'learns' from the dataset to determine which features are important.

Unfortunately, preparing a large, organised training set is technologically demanding and highly time-consuming, so training a built-in classification model is not to be covered here. 

creating such feature set of sufficient size is very cumbersome and not so feasible, and therefore training one is not covered here. There is, however, a feature extracting function and instructions as to how to train a nltk classification model on your own with the right dataset. Refer to mass_classification.py for details.

To get started, read the files in the following order: fetching_terms_and_descriptions -> dictionary.py -> by_keywords.py -> description_patterns.py -> by_descriptions.py -> hd_type.py


