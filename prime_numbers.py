
def prime_numbers(n):
    numbers_list = []

    for num in range(n+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                numbers_list.append(num)
    return numbers_list


n = int(input("enter number: "))

result = prime_numbers(n)
print(result)