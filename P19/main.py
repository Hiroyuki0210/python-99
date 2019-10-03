def rotate(x, ind):
     y = x[0:ind]
     z = x[ind:len(x)]

     lis = []
     lis.extend(z)
     lis.extend(y)

     return lis