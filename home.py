# Read the content from the file
with open("file-handling.txt", "r") as file:
    data = file.read()

# Remove numbers from the data
data_without_numbers = ''.join(char for char in data if not char.isdigit())

# Write the modified data to a new file
with open("file-handling-copy.txt", "w") as file:
    file.write(data_without_numbers)


input_string = "djdgebhu2345asdcgg"

output_string = ""
for char in input_string:     #not meansremove the chat
    if char.isdigit():
        output_string += char

print(output_string)
