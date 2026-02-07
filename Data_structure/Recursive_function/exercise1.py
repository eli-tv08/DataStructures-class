#تابع بازگشتی که مقدار fib(n) را محاسبه کند
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

#تابع بازگشتی که حاصل تقسیم صحیح دو عدد مثبت a و b را محاسبه کند
def Div(a, b):
    if b == 0:
        print("error")
        return
    if a < b:
        return 0
    return Div(a - b, b) + 1

#تابعی بازگشتی که حاصلضرب دو عدد مثبت a و b را محاسبه کند
def mul(a, b):
    if b == 0:
        return 0
    return mul(a, b - 1) + a