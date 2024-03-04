
# A dictionary is a variable type that is like a "paired dataset"
# "keys" are paired with "values"

phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
print(phones)

# keys can be used to get values but not the other way around
print (phones['Zoe'])

#"print (phones['232-43-58'])" wouldn't give you Zoe

# these commands make a new empty dictionary
dictionary = {}
dictionary = dict()

# you can assign new values to an existing key
phones['Zoe'] = '658-99-55'

# or add a whole new value to a dictionary
phones['Bill'] = '342-18-25'

# you can delete a value from a dictionary
del phones['Zoe']
print (phones)