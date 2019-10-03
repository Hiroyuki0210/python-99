def encode(x):
     x.append(100)
     a = x[0]
     same = 0
     count = 0
     z = []

     for el in x:
          if el == a:
               count += 1
               a = el
               
          if el != a:
               y = [count,a]
               z.append(y)
               count = 1
               a = el
               print(a)

     return z