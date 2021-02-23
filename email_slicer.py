# Alex Brumfield-Meyers
# 2/23/2021
# Takes in user email address, splits to username and domain and
# recognizes if the domain is among popular domains or something custom.

# Create list of popular email domains
popular = {
    'gmail': 'Google',
    'hotmail': 'Hotmail',
    'yahoo': 'Yahoo',
    'aol': 'America Online',
    'outlook': 'Microsoft'
}

# Take email address from user
email = input('Enter your email address: ').strip()

# Slice and store username
username = email[:email.index('@')]

# Slice and store domain name
domain = email[email.index('@') + 1:email.index('.')]

# Check if the domain is popular or not, and assign correct result output
if domain in popular:
    result = f'Looks like Your username = {username} is registered in {popular[domain]}. Neat!'

else:
    result = f'Your username = {username} is custom set up at {domain}. Neat!'

print(result)
