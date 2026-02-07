class Queue(): 
    def __init__ (self, max): 
        self.list = [None] * max
        self.max = max
        self.front = -1 
        self.rear = -1 
         
    #اضافه کردن عنصر انتهای صف 
    def enqueue(self, data): 
        if self.rear >= (self.max - 1) :  
            print("Queue is Full") 
            return False
        
        if self.front == -1:   
            self.rear = 0 
            self.front = 0  
        else:        
            self.rear +=1       
        self.list[self.rear] = data 
        return True

    #حذف و برگرداندن عنصرابتدای صف 
    def dequeue(self): 
        if self.front == -1:       
            print("Queue is empty")
            return None
        
        x = self.list[self.front]

        if self.front == self.rear:    
            self.front = -1
            self.rear = -1 
            
        else:       
            self.front +=1
        return x
        
    #نمایش عناصر  
    def Show(self):
        if self.front == -1:
            print("Queue is empty")
            return

        for i in range(self.front, self.rear + 1):
            print(self.list[i])