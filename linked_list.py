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

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or `None` if it's not found
        Takes O(n) time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Inserts a new node conataining data at the index position.
        Insertion takes O(1) time but finding the node at the insertion point takes O(n) time.
        Takes overall O(n) time
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            _next = current.next_node

            prev_node.next_node = new
            new.next_node = _next


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