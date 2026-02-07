#  تابع بازگشتی برای محاسبه تعداد برگ های درخت باینری(root) 
def Count_leaves(root):
    if root is None:
        return 0
    if root.Lchild is None and root.Rchild is None:                
        return 1
    return Count_leaves(root.Lchild) + Count_leaves(root.Rchild)

#تابع بازگشتی برای محاسبه تعداد گره های درجه یک ، درخت باینری 
def Count_1Deg(root):
    if root is None:
        return 0
    count = 0
    if (root.Lchild is None) != (root.Rchild is None):
        count = 1
    return Count_1Deg(root.Lchild) + Count_1Deg(root.Rchild) + count   

#تابع بازگشتی برای محاسبه تعداد گره های درجه دو ، درخت باینری 
def Count_2Deg (root):
    if root is None:
        return 0
    count = 0
    if root.Lchild and root.Rchild:
        count = 1
    return Count_2Deg(root.Lchild) + Count_2Deg(root.Rchild) + count

#تابعی بازگشتی برای محاسبه حاصل جمع تمامی داده های یک درخت دودویی 
def sum_Tree(root):
    if root is None:
        return 0
    return sum_Tree(root.Lchild) + sum_Tree(root.Rchild) + root.Data

#تابعی بازگشتی برای محاسبه تعداد نود های یک درخت باینری 
def Count(root):
    if root is None:
        return 0
    return 1 + Count(root.Lchild) + Count(root.Rchild)

#تابع بازگشتی برای محاسبه ارتفاع یک درخت باینری 
def hieght(root):
    if root is None:
        return 0
    return 1 + max(hieght(root.Rchild), hieght(root.Lchild))


#تابعی برای چاپ preorder یک درخت باینری 
def pre(root):
    if root is None:
        return
    print(root.Data)
    pre(root.Lchild)
    pre(root.Rchild)       

#تابعی بازگشتی که تارگتی را در یک درخت جستجو کند
def search(root, t):
    if root is None:
        return False
    if root.Data == t:
        return True
    return search(root.Lchild) or search(root.Rchild)      

#تابعی بازگشتی برای محاسبه مقدار حداکثر یک درخت 
def max_t(root):
    if root is None:
        return float("-Inf")
    return max(max_t(root.Lchild) , max_t(root.Rchild) , root.Data)
 