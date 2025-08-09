def factors(num):
    result = []
    for i in range(1, int(num**0.5) + 1): #squareroot
        if num % i == 0:
            result.append(i)
            if num // i != i:  # avoid duplicate when num is a perfect square
                result.append(num // i)
    return sorted(result)

# Example
n = 36
print(f"Factors of {n}: {factors(n)}")
