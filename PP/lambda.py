num = [1 , 2 , 3 , 4 , 5]

l = list(map(lambda x : x ** 2,num))
print(l)

eve = [2 , 4 , 6 , 8 , 10]
odd = [1 , 3 , 5 , 7 , 9]
multiple = list(map(lambda x , y : x * y,eve,odd))
print(multiple)

numb = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
even = list(filter(lambda x : x % 2 == 0 , numb))
print(even)

names = ["somebody","nobody","asvi","jenny","dusya","classrep"]
sort_name = sorted(names,key = lambda x : len(x))
print(sort_name)