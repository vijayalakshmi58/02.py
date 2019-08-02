# 02.py
jun = input(" ")
try:
  jun = int (jun)
frs = jun% 2
if frs > 0:
  print("Odd")
  else:
  print("Even")
  except ValueError:
    print("invalid")
