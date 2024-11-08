old = 1
current = 1
result = 0
for i in range(5):
     if(i == 0 or i==1 and i > -1  ):
         print(1)
     else:
         result = current+ old
         old = current
         print(result)
         current = result