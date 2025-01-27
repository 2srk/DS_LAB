def count_upper_and_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count


upper, lower = count_upper_and_lower("Hello World!")
print(f"Upper case letters: {upper}, Lower case letters: {lower}")