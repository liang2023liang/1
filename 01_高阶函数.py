def test():
    print("test function run!!!")

def test03(a,b):
    print(f"test03{a},{b}")

def test2(func,*args,**kwargs):
    print("test2 function run...")
    func(*args,**kwargs)

a=test
a()

test2(a)

test2(test03,100,200)

print(test)
print(type(test))