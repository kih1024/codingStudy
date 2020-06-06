list2 = ["a","b"]
a = 3
def asd():
    global a
    a = 4

def s():
    print(a)

asd()
s()