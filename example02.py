from arrays import Array

def use_array():
  menu = Array(5)
  for i in range(5):
    menu[i] = i+1
  print(menu) # [1, 2, 3, 4, 5]

  print(menu.__len__()) # 5
  print(menu.__getitem__(2)) # 3
  menu.__setitem__(2, 10)
  print(menu) # [1, 2, 10, 4, 5]
  print(menu.__getitem__(2)) # 10
  print(list(menu.__iter__())) # [1, 2, 10, 4, 5]

if __name__ == '__main__':
  use_array()
  