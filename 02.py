# 02.py
vgl = input(" ")
try:
  vgl = int (vgl)
mod = vgl% 2
if mod > 0:
  print("Odd")
  else:
  print("Even")
  except ValueError:
    print("invalid")
