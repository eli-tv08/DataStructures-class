class C_Queue:
    def __init__(self, max):
        self.list = [None] * max
        self.max = max
        self.front = -1
        self.rear = -1

    #اضافه کردن عنصر به صف حلقوی
    def  enqueue(self , data):
        if (self.rear +1) % self.max == self.front:
            print("Queue is full")
            return False
        
        if  self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max   

        self.list[self.rear] = data

    #حذف و برگرداندن عنصر ابتدای صف 
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        
        k = self.list[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        
        else:
            self.front = (self.front +1) % self.max

        return k
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear +1) % self.max == self.front
    
    #نمایش عناصر معتبر صف 
    def show_valid(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        k = self.front
        print(self.list[k])
        while k != self.rear:
            k = (k + 1) % self.max
            print(self.list[k])
    
    #پیدا کردن اولین data  
    def find(self, data):
        if self.is_empty():
            return None
        
        k = self.front
        if self.list[k] == data:
            return k
        
        while k != self.rear:
            k = (k + 1) % self.max
            if self.list[k] == data:
                return k
        return None    

    #جایگزینی تمام old با new 
    def Replace(self, old, new):
        if self.is_empty():
            return False
        
        replaced = False
        k = self.front

        if self.list[k] == old:
            self.list[k] = new
            replaced = True

        while k != self.rear:
            k = (k + 1) % self.max
            if self.list[k] == old:
                self.list[k] = new 
                replaced = True
        return replaced                   
