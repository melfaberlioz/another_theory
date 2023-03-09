# variable for user input
user_input = ''
# a list to store the values
inputs = []

while user_input.lower() != 'done':
    # user_input = input("Enter a new value, or done when done.")
    if user_input:
        inputs.append(user_input)
    # prompt for a new value
    user_input = input('Enter a new value, or done when done')
print(inputs)