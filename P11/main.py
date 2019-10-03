def encode_modified(x):
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
               if count != 1:
                    y = [count,a]
                    z.append(y)
               else:
                    z.append(a)
               count = 1
               a = el

     return z