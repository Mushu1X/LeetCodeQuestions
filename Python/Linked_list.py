class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next



class LinkedList:

    def __init__(self):
        self.head = None


    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):

        if self.head is None:
            print("empty linked list")
            return 
        

        itr = self.head
        arr = []
        while itr:
            arr.append(itr.data)
                
            itr = itr.next

        print(arr)


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)


    def insert_values(self, data_list):

        self.head = None 
        for data in data_list:
            self.insert_at_end(data)



if __name__ == '__main__':

    ll = LinkedList()

    aa=  LinkedList()

    ll.insert_at_begining(5)
    ll.insert_at_begining(10)
    ll.insert_at_begining(29)
    ll.insert_at_end(78)

    aa.insert_values([23, 45, 67, 98])

    aa.print()

    ll.print()

