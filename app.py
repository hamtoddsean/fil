import os,time
f='fint.csv'
d=os.path.abspath(f)
if os.path.exists(d):
  print('yes')
  print(d)
  time.sleep(600)