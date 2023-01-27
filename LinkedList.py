class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None

    def setVal(self, val):
        self.val = val

    def setNext(self, next):
        if self.next == None:
            self.next = next

    def getVal(self):
        return self.val
    
    def getNext(self):
        return self.next

class LinkedList:
    def __init__(self) -> None:
        self.head = Node() #dummy head
        self.ptr = self.head
        self.length = 0
    
    def add(self, val):
        # pointer points to last non-null node in list
        self.ptr.setNext(Node(val))
        self.ptr = self.ptr.getNext()
        self.length += 1
        
    def get(self, val: object):
        curr = self.head
        while (curr.getNext() != None):
            curr = curr.getNext()
            if curr.getVal() == val:
                return curr.getVal()
        return None # was not found
    
    def get(self, idx: int):
        if idx > self.length - 1:
            return None
        curr = self.head.getNext()
        for i in range(idx - 1):
            curr = curr.getNext()
        return curr.getVal()
    
    def remove(self, val):
        curr = self.head
        while( curr.getNext() != None ):
            if curr.getNext().getVal() == val:
                if curr.getNext().getNext() == None: #we are deleting the last item, update pointer to penultimate item
                    self.ptr = curr

                temp = curr.getNext().getVal()
                curr.setNext(curr.getNext().getNext())
                self.length -= 1
                return temp

            curr = curr.getNext()

        return None # removal unsuccessful, value not found
    
    def pop(self): # pop from end of list?
        temp = self.ptr.getVal()

        curr = self.head

        while( curr.getNext() != None ): # update ptr
            curr = curr.getNext()
            if curr.getNext().getNext() == None:
                self.ptr = curr

        return temp
        
    