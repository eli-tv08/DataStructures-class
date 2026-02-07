class dnode():
    def __init__(self ,x):
        self.Data = x
        self.next = None
        self.back = None


class dlinked_list :
    def __init__(self):
        self.head = None

    def ins_first(self, x):
        if self.head is None:
            self.head = dnode(x)
            return
        a = dnode(x)
        a.next = self.head
        self.head.back = a
        self.head = a

    def ins_last(self, x):
        if self.head is None:
            self.ins_frist(x)
            return
        c = self.head
        while c.next:
            c = c.next
        a = dnode(x)
        c.next = a
        a.back = c

    def ins_after(self, x, y):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c :
            if c.Data == x:
                if c.next is None:
                    self.ins_last(y)
                    return
                a = dnode(y)
                a.next = c.next
                c.next.back = a
                c.next = a
                a.back = c
                return
            c = c.next
        print("not found")

    def ins_before(self, x, y):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c:
            if c.Data == x:
                if c.back is None:
                    self.ins_frist(y)
                    return
                a = dnode(y)
                a.next = c
                a.back = c.back
                a.back.next = a
                c.back = a
                return
            c = c.next
        print("not found")

    def del_first(self):
        if self.head is None:
            print("error")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.back = None
        
    def del_last(self):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c.next:
            c = c.next
        if c.back is None:
            self.del_first()
            return
        c.back.next = None

    def del_before(self, x):
        if self.head is None:
            print("error")
            return
        if self.head.Data == x:
            print("error")
            return
        c = self.head
        while c :
            if c.Data == x:
                a = c.back
                c.back = a.back
                if a.back:
                    a.back.next = c
                return
            c = c.next
        print("x not found")
                                                
    def del_after(self, x):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c:
            if c.Data == x:
                if c.next:
                    a = c.next
                    c.next = a.next
                    if a.next :
                        a.next.back = c
                    return
                print("error")
                return
            c = c.next
        print("not found")

    def del_x(self, x):
        if self.head is None:
            print("error")
            return
        if self.head.Data == x:
            self.del_first()
            return
        c = self.head
        while c:
            if c.Data == x:
                if c.next is None:
                    self.del_last()
                    return
                c.back.next = c.next
                c.next.back = c.back
                return
            c = c.next
        print("not found")               

l = dlinked_list()
l.ins_first(1)
l.ins_last(2)
l.ins_last(3)
l.ins_after(2, 9)
l.del_before(3)
l.del_x(9)
