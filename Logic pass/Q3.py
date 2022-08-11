count = 0

my_string = input("Enter the sentence:")
my_char = input("the letter you want to count:")

for i in my_string:
    if i == my_char:
        count += 1

print(count)