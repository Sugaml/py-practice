def count_up_to(n):
    """Generator function that yeilds numbers from 1 to n."""
    count=1
    while count<=n:
        yield count
        count+=1

# Using the generator function
numbers=count_up_to(5)

#Iterating over the generator to retrive values
for num in numbers:
    print(num)