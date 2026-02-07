class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    #اضافه کردن عنصر به ابتدای لیست
    def insert_first(self,x):
        if self.head == None:
           self.head = Node(x)
        else:
           a = Node(x)           
           a.next = self.head         
           self.head = a       

    #اضافه کردن عنصر به آخر لیست
    def insert_last(self,x):
        if self.head is None:
            self.head = Node(x)
        else:
            a = Node(x)          
            c = self.head          
            while c.next:          
                c = c.next
            c.next = a             

    def insert_after(self, x, y):
        if self.head is None:
            print('list is empty')
            return
    
        c = self.head
        while c:
            if c.data == x:
                a = Node(y)                 
                a.next = c.next
                c.next = a
                return
            c = c.next     
        print("not found")  

    def insert_befor(self, x, y):
        if self.head is None:
           print(" list is empty")
           return
        if self.head.data == x:
            self.insert_first(y)
            return
        c = self.head
        while c.next:
            if c.next.data == x:
                a = Node(y)
                a.next=c.next
                c.next=a
                return
            c = c.next
        print("not found")

    #حذف اولین نود لیست  
    def Del_firt(self):
        if self.head is None:
            print("error 0")
            return
        c = self.head
        self.head = c.next

    #حذف آخرین نود لیست
    def Del_last(self):    
        if self.head is None:
           print("error 0")
           return
        if self.head.next is None:
            self.Del_firt()
            return 
        c = self.head
        while c.next.next:
            c = c.next
        c.next = None

    def Del_after(self,x):
        if self.head is None:
            print("error 0")
            return
        c = self.head 
        while c and c.next:
          if c.data == x:
            a = c.next
            c.next = a.next
            return
          c = c.next
        print("not found")

    def Del_befor(self,x):
        if self.head is None:           
            print("error 0")
            return
        if self.head.data == x:         
            print("error x1")
            return
        if self.head.next is None:      
           print("error 1")
           return
        if self.head.next.data == x:    
               self.Del_firt()
               return
        c = self.head
        while c.next and c.next.next:
               if c.next.next.data == x:
                   a = c.next
                   c.next = a.next
                   return
               c = c.next
        print("not found")

    def Del_all(self):
        while self.head:
           self.Del_firt()

    def Del_x(self,x):
        if self.head is None:
            print("error 0")
            return
        if self.head.data == x:
            self.Del_firt()
            return
        c = self.head
        while c.next:
            if c.next.data == x:
                c.next = c.next.next
                return
            c = c.next
        print("not found")         

    #چاپ کل لیست        
    def print_list(self): 
        c = self.head 
        while c: 
            print(c.data, end=" -> ") 
            c = c.next 
        print("None")        