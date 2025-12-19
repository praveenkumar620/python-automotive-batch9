# Dictionary - A changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, which allows quick access to values

capitals = {
    'USA': 'Washington DC',
    'India': 'New Delhi',
    'China': 'Beijing',
    'Russia': 'Moscow'
}

print(capitals['Russia'])          # Moscow
print(capitals.get('Germany'))     # None (because key not present)
print(capitals.keys())             # All keys
print(capitals.values())           # All values
print(capitals.items())            # Key-value pairs

##########################################################

capitals.update({'Germany': 'Berlin'})     # Add new key-value
capitals.update({'USA': 'Las Vegas'})      # Update existing key
capitals.pop('China')                      # Remove China
capitals.clear()                           # Clear whole dictionary

for key, value in capitals.items():
    print(key, value)
