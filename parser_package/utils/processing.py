from parser_package import *

def preprocess(sentence: str):
    """Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.

    Args:
        sentence (str): Le texte à traiter
    """
    
    # the goal is to tokenize the given sentence and recuperate them if their are composed
    # by alphanumerical characters and if it is the case then transform to lower case
    tokens = [token.lower() for token in nltk.word_tokenize(sentence) if token.isalpha()]
    
    # return a list of tokens
    return tokens
    
