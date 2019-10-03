def decode(x):
     y = []
     for element in x:
          if type(element) is list:
               for num in range(element[0]):
                    y.append(element[1])
          else:
               y.append(element)

     return y