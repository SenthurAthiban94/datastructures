class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# Singly Linked List
class SingleLinkedList:
    def __init__(self,value=None):
        self.head = None
        self.tail = None
        self.length = 0
        
        if(value!=None):
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length +=1
            
    def __str__(self):
        temp_node = self.head
        result = '' if self.head else str(None)
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+= ' -> '
            temp_node = temp_node.next
        return result
    
    # Insert into End of the linked list        
    def append(self,value):
        new_node = Node(value)
        if self.head !=None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length+=1
    
    # Insert into Beginning of the linked list
    def prepend(self,value):
        new_node = Node(value)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        self.length +=1
        
    # Insert into any place of the linked list        
    def insert(self,index,value):
        if index>self.length or index <0:
            return False
        
        new_node = Node(value)
        
        if self.head is not None:
            temp_node = self.head
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                for _ in range(index-1):
                    temp_node = temp_node.next
                new_node.next = temp_node.next
                temp_node.next = new_node
                if(new_node.next is None):
                    self.tail = new_node
        else: 
            self.head = new_node
            self.tail = new_node
        self.length+=1
        
        return True

    def traversal(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    def search(self,value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index+=1
        return -1
            
    def get(self,targetindex):
        if targetindex==-1: return self.tail
        if targetindex <0 or targetindex>= self.length:
            return None
        
        current = self.head
        for _ in range(targetindex):
            current = current.next
        
        return current
        
    def set(self, index, value):
        node_tobe_updated = self.get(index)
        if node_tobe_updated is not None:
            node_tobe_updated.value = value
            return True
        else: 
            return False
    
    def popFirst(self):
        pop_node = self.head
        if pop_node:
            if pop_node.next is None: self.tail = None
            self.head = pop_node.next
            pop_node.next = None
            self.length -=1
            
        return pop_node
    
    def pop(self):
        pop_node = self.tail
        if pop_node:
            temp = self.head
            if temp.next:
                while temp.next is not self.tail:
                    temp = temp.next                
                self.tail = temp
                temp.next = None
            self.length -=1
            
        return pop_node

    def remove(self,index):
        if index>=self.length: return None
        if index==0:
            return self.popFirst()
        else:
            previous_node = self.get(index-1)
            popped_node = previous_node.next
            previous_node.next = popped_node.next
            popped_node.next = None
            return popped_node
    
    def reverse(self):
        prevNode = None
        current = self.head
        for _ in range(self.length):
            nextnode = current.next
            current.next = prevNode
            prevNode = current
            current  = nextnode
        self.head, self.tail = self.tail, self.head
    
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def remove_duplicates(self):
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node
    
    def deleteAll(self):
        self.head = None
        self.tail = None
        self.length = 0

ll = SingleLinkedList(2)
print(ll.insert(1,1))
print(ll.insert(0,3))
print(ll.insert(0,4))
print(ll.insert(0,5))
# # # print(ll.traversal())
# print(ll)
# # print(ll.search(5))
# print(ll.get(-1).value)
# print(ll.set(3,2))
print(ll)
# print(ll.popFirst().value)
# print(ll.popFirst().value)
print(ll.pop().value)
print(ll)
ll.pop()
print(ll)
print(ll.remove(0))
print(ll)
# ll.deleteAll()
print(ll)
ll.reverse()                            # reverse the Linked List
print(ll)
print(ll.find_middle().value)           # Find Middle Node
ll.remove_duplicates()                  # Remove Duplicate Nodes
print(ll)