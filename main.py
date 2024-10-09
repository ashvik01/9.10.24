arr= [1,2,4,9,7]

def left_rotate(arr,d):
    return arr[d:] + arr[:d]

d= 2
left= left_rotate(arr,d)
print(left)

def right_rotate(arr,d):
  arr[-d:] + arr[:-d]
  
d= 2
right= right_rotate(d, arr)
print(right)