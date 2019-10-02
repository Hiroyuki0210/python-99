def flatten(x):
     lis = []
     
     while len(x) > 0:
        node = x.pop(0)
        if type(node) is list:
            x = node + x
        else:
            lis.append(node)

     return lis