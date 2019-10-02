def is_palindrome(x):
     origin_x = []

     for elemnt in x:
          origin_x.append(elemnt)

     x.reverse()
     change_x = x

     return (origin_x == change_x)
