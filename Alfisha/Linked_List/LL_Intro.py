class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    #Insert at the begining
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data)  + '-->'
            itr = itr.next

        print(llstr)     

    #Insert at the end   
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next 

        itr.next = Node(data, None)

    #Insert list of values as an input   
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    #Return length of the linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    #Remove an item from the list
    def remove_at(self, index):
        if index<0 or index>=self.get_length(): 
            raise Exception("Invalid Exception")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1 :
                itr.next = itr.next.next
                break
                
            itr = itr.next
            count += 1
    
    #Insert at specific index
    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Exception")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr =self.head
        while itr:
            if count == index -1 :
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

if __name__ == '__main__':        
    ll = LinkedList()
    ll.insert_at_begining(10)
    ll.insert_at_begining(20)
    

    ll.insert_at_end(40)
    ll.insert_at_end(60)
    ll.print()

    ll.insert_values(["Python", "Java", "C++", "PHP"])
    ll.print()
    ll.remove_at(1 )
    ll.print()
    ll.insert_at(1, "JS")
    ll.print()
    print("Length:", ll.get_length())
    