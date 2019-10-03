def compress(x):
     y = []
     a = -1
     
     for element in x:
          if element != a:
               y.append(element)
          a = element

     return y
