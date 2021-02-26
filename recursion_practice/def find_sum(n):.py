def find_sum(n):
    if n <= 9:
        return n
    
    last_digit = n % 10
    return find_sum(n // 10) + last_digit

print(find_sum(552))