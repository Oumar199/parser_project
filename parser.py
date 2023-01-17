from parser_package.utils.np_chunks import contains_subtree
import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP | NP VP | S Conj S
PP -> P NP
NP -> N | Det N | Det Adj N | NP Adv | NP PP | NP Conj NP 
VP -> V | V V | VP Adv | VP NP | VP PP | VP Conj VP
Adj -> Adj Adj
"""


grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # the goal is to tokenize the given sentence and recuperate them if their are composed
    # by alphanumerical characters and if it is the case then transform to lower case
    tokens = [token.lower() for token in nltk.word_tokenize(sentence) if token.isalpha()]
    
    # return a list of tokens
    return tokens


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # initialize the list of chunks
    chunks = []
    
    for tree_ in list(tree.subtrees()):
        
        # recuperate the label
        label = tree_.label()
        
        # if it is the searched label then
        if label == 'NP':
        
            """ 
            J'ai écris la fonction suivante au niveau du fichier python dont le chemin figure comme suit:

            parer_package/utils/np_chunk.py

            La fonction a été importé en haut du fichier parser.py.
            
            Cette fonction nous permet de savoir si un arbre syntaxique contient un chunk dont le label est spécifié en para-
            -mètre. Cela nous permettra de savoir si on doit ajouter ou non un chunk parmi la liste des np chunks de notre programme.
            """

            # verify if the subtree contains subtrees with the same label
            non_unique = contains_subtree(tree_, 'NP')
            
            # it it is not the case then add a new chunk to the bunch of chunks
            if not non_unique:
                
                chunks.append(tree_)
    
    # return the bunch of chunks
    return chunks


if __name__ == "__main__":
    main()
