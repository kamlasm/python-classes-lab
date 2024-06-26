import random
# to pass the test function, please return a string of 'string' from then function
# eg: test() => 'string'
def test():
    return "string"

# write a function to remove all empty values (False, [], {}, (), "", None) EXCEPT 0 from an array.
# It should handle complex data types eg: {}, [] etc.
# eg: [0, False, "", [], {}, 1, 'Kevin'] => [0, 1, 'Kevin'];
def remove_blank(list):
    new_list = []
    for item in list:
        if item or ((type(item) == int) and item == 0):
            new_list.append(item)
    return new_list

# write a function to return a random element from an list
# eg: [1,"elephant", "apple", 67] => "elephant"
def random_element(list):
    import random 
    random_index = random.randint(0,len(list) - 1)
    return list[random_index]

# write a function that returns the second lowest and second highest number in a list
# eg: [1,2,3,4,5,6,7,8] => [2,7]
def second_lowest_second_highest(list):
    sorted_list = sorted(list)
    new_list = [sorted_list[1], sorted_list[-2]]
    return new_list

# write a function that will convert a price into coins needed to make up that price
# the coins available are 1, 2, 5, 10, 20, 50, 100
# the function should use the smallest number of coins possible
# eg: coins(1.99) => [100, 50, 20, 20, 5, 2, 2]
def coins(price):
    coins = [1, 2, 5, 10, 20, 50, 100]
    price = price * 100
    coins_needed = []
    
    while price > 0:

        if price >= max(coins):
            added_coin = max(coins)
            coins_needed.append(added_coin)
            price = price - added_coin
        else:
            coins.remove(max(coins))

    return coins_needed

# write a function to merge two lists and remove duplicates
# eg: mergeUnique([9,8,8,9], [7,8,8,7]) => [9,8,7]
def merge_unique(list1, list2):
    for item in list1:
        if item in list2:
            list2.remove(item)
    merged_list = list1 + list2
    return merged_list

# write a function to find the first n fibonacci numbers
# the fibonacci sequence is a series of numbers, each number is the sum of the last two
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 etc...
# eg: fibonacci(4) => [0,1,1,2]; fibonacci(8) => [0, 1, 1, 2, 3, 5, 8, 13];

def fibonacci(n):        
    sequence = []
    counter = n

    while counter > 0:
        if counter == n:
            sequence.append(0)
        elif counter == n - 1:
            sequence.append(1)
        else:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)            
        
        counter -= 1

    return sequence