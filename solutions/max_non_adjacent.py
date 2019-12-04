

def max_non_adjacent(nums):

    # inc = 0
    # exc = 0

    # for n in nums:
    #     new_exc = inc if inc > exc else exc

    #     inc = exc + n

    #     exc = new_exc


    # return inc if inc > exc else exc

    previous, largest = 0,0

    for amount in nums:

        previous, largest = largest, max(largest, previous + amount)

    return largest


print(max_non_adjacent([7,4,7,1,2,3,4,5,6]))