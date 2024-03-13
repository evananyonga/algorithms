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
    
    # knowing the size of the linked list
    def size(self):
        """
        Returns the number of nodes in a list and --
        Takes linear time -- O(n)
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self, item):
        """
        Adds a new node containing data (item) at the head of the list
        This operation takes constant time O(1)
        """
        new_node = Node(item)
        new_node.next_node = self.head
        
        self.head = new_node

    def __repr__(self) -> str:
        """
        Return a string representation of the list
        Takes constant time O(n)
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)