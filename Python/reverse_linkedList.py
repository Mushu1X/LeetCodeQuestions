class Node:

    def __init__(self, data = None, next = None):

        self.data = data
        self.next = next


class LinkedList():

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


    def reverse_list(self, head):

        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        return prev







if __name__ == '__main__':

    ll = LinkedList()

    ll.insert_at_begining(5)
    ll.insert_at_begining(10)
    ll.insert_at_begining(29)

    ll.print()

    ll.head = ll.reverse_list(ll.head)

    ll.print()









