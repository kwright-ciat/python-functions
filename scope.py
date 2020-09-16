def show():
   A = 'inside show'
   print(A)

def gshow():
   global A
   A = 'inside show'
   print(A)

A = 'outside'
print(A)

show()
print(A)
gshow()
print(A)