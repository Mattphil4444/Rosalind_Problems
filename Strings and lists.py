
tea_party = ['March Hare', 'Hatter', 'Dormouse', 'Alice']
print(tea_party[0])
print(tea_party)
# python lists start at 0

tea_party[0] = 'Cheshire Cat'
# this replaces the value at 0 in the list "tea_party"
print(tea_party)

tea_party.append('Jabberwocky')
# You can also add items to the end of an existing list by using the function append()
print (tea_party)

# If you need to obtain only some of a list, you can use the notation list_name[a:b]
# to get only those from index a up to but not including index b
print(tea_party[1:3])

# You can also use negative indices to count items backtracking from
# the end of the list.
print(tea_party[-2:])

# You can slice strings the same way that you slice lists
a = 'flimsy'
b = 'miserable'
c = b[0:1] + a[2:]
print (c)

