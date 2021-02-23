def hello():
    print("Hello student")

def add(x=1,y=1):
    print ("The total is:", x + y)

def show(*args):
    print(args)

def showd(**kwargs):
    print(kwargs)

showd(x=1,y=5)
showd(name='Keith')
showd()
hello()
hello()
hello()
add(5,6)
add(3,4)
add(x=5)
show()
show('a',5,[1,2])
show(1,2,3,4,5)