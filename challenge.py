items_i_like = ["Bike", "Cars", "Books", "Computer", "Guitar"]
my_iterator = iter(items_i_like)
print(my_iterator)
for item in range(len(items_i_like)):
    print(next(my_iterator))