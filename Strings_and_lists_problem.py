
big_string = "Je4PBNtGh9KHPG2JvVllWWUCJwWgUParamesotritonoXp7xQIsSwlwgxpzJyFUVihoiyOk7YJ0exxxqUJW1mdFWZiTN2IFprczDTrQJwdndLR3k8WqUw34rF0yk4FFnBoQU1cNhardwickii1w5XSMT6djUldf. 29 42 135 144"

res = [int(i) for i in big_string.split() if i.isdigit()]

print(big_string[res[0]:res[1]+1] + " " + big_string[res[2]:res[3]+1])
