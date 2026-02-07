class Stack:
    def __init__(self, limit = 100):
        self.stack = []
        self.limit = limit

    #اضافه کردن عنصر بالای پشته
    def push(self, data):
        if len(self.stack) >= self.limit :
            print('stack is Full')        
            return False
        self.stack.append(data)
        return True

    #حذف و برگرداندن عنصر بالایی 
    def pop(self):
        if len(self.stack) == 0 :
            print("stack is empty")
            return None
        return self.stack.pop()

    #مشاهده عنصر بالایی بدون حذف
    def peek(self):
        if len(self.stack) == 0:
            print("stack is empty")
            return
        return self.stack[-1]
    
    #بررسی وجود یک مقدار در پشته
    def find(self, value): 
        return value in self.stack
    
    #نمایش همه عناصر
    def show(self): 
        return self.stack.copy() 
    
    #نمایش عناصر از بالا به پایین
    def display(self): 
        for i in reversed(self.stack): 
            print(i) 

    # جایگزینی اولین مقدار old با new 
    def replace(self, old, new): 
        replaced = False
        for i in range(len(self.stack)): 
            if self.stack[i] == old: 
                self.stack[i] = new 
                replaced =  True   
        return replaced  