# def find_solution(str,index1, count):

#     length = len(str)
#     count1 = 0
#     count2 = 0

#     for index in range(index1,length -1):
#         if index < length -1:
#             count1 = find_solution(str, index + 1, count)
        
#         if index < length - 2 and int(str[-2]) < 26:
#             count2 = find_solution(str, index + 2, count)
        
    

#     return  count + 1



# find_solution("111",0, 0)

def is_char_valid(str):
    code = int(str)
    return 0 if code > 26 or code < 1 else 1

def get_message_count(msg):

    msg_str = str(msg)

    length = len(msg_str)

    if length == 1:
        count = 1
    elif length == 2:
        count = 1 + is_char_valid(msg_str)

    else:
        count = get_message_count(msg_str[1:])

        if is_char_valid(msg_str[2:]):
            count += get_message_count(msg_str[2:])

    return count


# assert get_message_count(111) == 3

# assert get_message_count(1) == 1

# assert get_message_count(1111) == 5


def  get_count(str):

    length = len(str)

    dp = [0]*(length+1)

    dp[0] = 1

    dp[1] = 1 if int(str[0])!= 0 else 0

    for i in range(2,length+1):
       first = int(str[i-1:i])
       second = int(str[i-2:i])

       if first >= 1 and first <= 9:
           dp[i] += dp[i-1]

       if second >= 10 and second <= 26:
           dp[i] += dp[i-2]
    
    print(dp)
    return dp[length]


print(get_count("111"))