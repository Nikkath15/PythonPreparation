numbers = [10,20,30,40,50]
new_numbers = list(filter(lambda x: (x%2==0),numbers))
print(new_numbers)