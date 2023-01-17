# import nltk
from typing import Union
from parser_package.utils.processing import preprocess

def get_trees(texts: Union[str, list], parser, to_list: bool = True):
    
    # get a list of sentences if texts is of type string
    if type(texts) is str: texts = [texts]
    
    # initialize trees
    trees = []
    
    # parse sentences
    for sentence in texts:
        
        # recuperate tokens
        tokens = preprocess(sentence)
        
        try:
            
            # parse the sentence
            tree = parser.parse(tokens)
            
            # convert the tree to a list if necessary
            if to_list: tree = list(tree)
            
            # add the new tree to the bunch of trees
            trees.append(tree)
            
        except Exception as e:
            
            # if the parsing don't work for that sentence then print a error
            print(f"Le parser n'arrive pas à analyser la phrase {sentence}")
            print(e)
    # return a list of trees
    return trees
