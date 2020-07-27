def is_digit(x):
    return str(x).isnumeric()
    # return isinstance(x, int)
    # return isinstance(x, float)
    # return isinstance(x, object)


s = [None, [], "2", 2, 1.0, int, str, "B", "b"]

# Применение lambda функций
filtered_s = filter(is_digit, s)

print(list(filtered_s))
