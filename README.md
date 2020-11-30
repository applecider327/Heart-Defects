# NLP-Congenital-Heart-Defects

**Introduction**

This is an NLP (Natural Language Processing) project for automatically identifying which type of congenital heart defect is being described in a text such as a medical case report. This is a strategy for document classification. Given a set of case reports, we would like to be able to determine which reports involve instances of known or newly diagnosed congenital heart defects. We may then determine if other aspects of case presentation vary based on correlation with specific defects.

**Single text classification**

In this scenario, a text is divided into two parts, title and body. For each component the system looks for key features (specifically, keywords and descriptions) and utilises this information collectively to come up with a final call. The title part holds greater significance than the rest, however, and as such it may override any other parts of the text. For instance, a text piece with the title "Case Report: Fallot's Tetralogy" already offers enough information for the system to output "Tetralogy of Fallot". Refer to hd_type.py for details.

**Mass text classification**

Python's nltk offers a number of text classification algorithms. The idea is to train one of them (say, Naive Bayes Classifier) by feeding it a feature set of specific format and test the algorithm on a large scale. Unfortunately, creating such feature set of sufficient size is very cumbersome and not so feasible, and therefore training one is not covered here. There is, however, a feature extracting function and instructions as to how to train a nltk classification model on your own with the right dataset. Refer to mass_classification.py for details.

To get started, read the files in the following order: fetching_terms_and_descriptions -> dictionary.py -> by_keywords.py -> description_patterns.py -> by_descriptions.py -> hd_type.py


