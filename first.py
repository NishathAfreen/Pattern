n=int(input())
x=(n*2)-1
for i in range(x,0,-1):
      for j in range(0,x-i):
             print(" ",end=" ")
      for k in range(0,i):
             print("*",end=" ")
      print()
x1=x-1
for i in range(1,x):
   for j in range(x1-i,0,-1):
          print(" ",end=" ")
   for k in range(0,i+1):
          print("*",end=" ")
   print()


      


     
       
      

      

