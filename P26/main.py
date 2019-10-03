import itertools

def combination(ind, x):
     y = list(itertools.combinations(x,ind))
     z = []
     for element in y:
          a = list(element)
          z.append(a)

     return z