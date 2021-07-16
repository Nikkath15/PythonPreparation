def my_gen():
   n = 1
   print('this statement is printed first')
   yield n
   n += 1
   print('this statement is printed second')
   yield n
   n += 1
   yield n
   
for item in my_gen():
     print(item)