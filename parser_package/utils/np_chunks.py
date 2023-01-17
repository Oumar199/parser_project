
def contains_subtree(tree, label: str = 'NP', skip_first: bool = True):
    """Verify if a tree contains a subtree

    Args:
        tree (Tree): A tree from a parsed sentence
        label (str, optional): The label of the chunk that we search for. Defaults to 'NP'.
        skip_first (bool, optional): Skip the parent. Defaults to True.

    Returns:
        bool: True if the tree contains the subtree (for which we predefined the label), False else
    """
    
    # get all subtrees of the given tree 
    for i, subtree in enumerate(list(tree.subtrees())): 
        
        # if we want only the descendent so we skip the first element
        if i == 0 and skip_first:
            
            continue
        
        # verify if a subtree is a noun phrase chunk
        if subtree.label() == label:
            
            # return True if it is the case
            return True
    
    # return False if we didn't find a noun phrase subtree
    return False

def get_chunks(tree, label_: str = 'NP'):
    
    # initialize the list of chunks
    chunks = []
    
    for tree_ in list(tree.subtrees()):
        
        # recuperate the label
        label = tree_.label()
        
        # if it is the searched label then
        if label == label_:
            
            # verify if the subtree contains subtrees with the same label
            non_unique = contains_subtree(tree_, label)
            
            # it it is not the case then add a new chunk to the bunch of chunks
            if not non_unique:
                
                chunks.append(tree_)
    
    # return the bunch of chunks
    return chunks
