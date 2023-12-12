def read_data() -> list:
    with open("input.txt") as f:
        return f.read().splitlines()

def sum_of_caliberation_values():
    sum=0
    data = read_data()
    map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    numbers = list(map.keys())
    numbers+=list(map.values())
    for row in data:
        digits = ''
        for start in range(len(row)):
            for end in range(start+1, len(row)+1):
                substring = row[start:end]
                if(substring in numbers):
                    if(str.isdigit(substring)):
                        digits+=substring
                    else:
                        digits+=map.get(substring)
        if(len(digits) == 1):
            sum+=int(digits+digits)
        else:
            sum+=int(digits[0]+digits[len(digits)-1])
    print(sum)
    
sum_of_caliberation_values()
