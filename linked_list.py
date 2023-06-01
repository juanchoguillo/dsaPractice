class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

# Working LinkedList constructor 
class LinkedList:
    # Initializer 
    def __init__(self, value):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next 
    
    def append(self, value):
        new_node = Node(value=value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True
    
    def pop(self):
        if self.head == None:
            return None

        elif self.head == self.tail :
            self.head = None
            self.tail = None 
        else:
            temp = self.head 
            while temp.next is not self.tail:
                temp = temp.next 
            self.tail = temp
            temp.next = None
        
            return temp


    def prepend(self, value):
         new_node = Node(value=value)
         if self.head == None:
             self.head = new_node
             self.tail = new_node
         else:
             new_node.next = self.head 
             self.head = new_node

         return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
        return temp

    def get(self, index):
        if self.length == 0 :
            return None
        else:
            temp = self.head
            counter = 0
            while counter < index :
                temp = temp.next
                counter += 1
            return temp 
    
    def get_tutorial(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        else :
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value
            return temp
        
    def set_value_tutorial(self, index, value):
        temp = self.get_tutorial(index)
        if temp :
            temp.value = value
            return True 
        else:
            return False
        
    def insert(self, index, value):
        new_node = Node(value=value)
        temp_after = self.get_tutorial(index)
        if temp_after :
            temp_before = self.head
            for _ in range(index - 1):
                temp_before = temp_before.next
            temp_before.next = new_node
            new_node.next = temp_after
        return True 
    
    def insert_tutorial(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value=value)
        if index == self.length:
            return self.append(value=value)
        new_node = Node(value=value)
        temp = self.get_tutorial(index=index-1) 
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True 




    def insert(self, index, value):
        # create new Node 
        #  insert node 
        pass

my_linked_list = LinkedList(1)

my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
print("Other operation")
# my_linked_list.prepend(9)
# my_linked_list.print_list()
# print("Other operation")
# my_linked_list.pop()
# my_linked_list.print_list()
# print("Other operation")
# my_linked_list.pop_first()
# my_linked_list.print_list()

my_linked_list.insert(index=2, value=24)
my_linked_list.print_list()







    