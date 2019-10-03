def duplicate(x,y):
     lis = []

     for j in range(len(x)):
          for i in range(y):
               lis.append(x[j])

     return lis