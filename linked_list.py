class Node:
    """
    An object for storing a single node of a linkedList
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """ 
    Singly Linked List
    """

    def __init__(self):
        # always set newer lists to empty
        self.head = None

    # checking status of linkedlist
    def is_empty(self):
        return self.head == None
    
