def multiply_binary(a, b):
    result = 0
    shift = 0

    while b > 0:
        if b & 1:
            result += a << shift
        shift += 1
        b >>= 1

    return result

# Example (11 * 12):
x = multiply_binary(11, 12)
print(x)
