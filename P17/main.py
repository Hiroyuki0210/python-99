def split(x,ind):

     lis = []

     if ind == 0:
          y = []
     else:
          y = x[0:ind]

     if ind == len(x):
          z = []
     else:
          z = x[ind:len(x)]

     lis.append(y)
     lis.append(z)

     return lis