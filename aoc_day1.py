############### AoC Day 1 - Pt. 1 ###############
def read_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the content of the file and split it into lines
            lines = file.read().splitlines()
            return lines
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Read file
file_path = 'files/aoc_day1.txt'
myArray = read_file(file_path)

# Conver list items to lowercase to avoid errors in matching "SiX" to "6" etc.
myArray = list(map(str.lower, myArray))

# Create an array to store all possible int numbers
numberOfIterations = 10
includeChars = []

for i in range(numberOfIterations):
    includeChars.append(str(i))

# Initialize sum
totalSum = 0

for i in range(len(myArray)):
    # Only keep chars that exist in the includeChars array (0-9)
    myArray[i] = ''.join(char for char in myArray[i] if char in includeChars)

    # If the word has no digits, then set it to 0 (to avoid cases where there are no digits at all in the file)
    if len(myArray[i]) == 0:
        myArray[i] = 0
    # If the number has 1 digit, then duplicate it
    elif len(myArray[i]) < 2:
        myArray[i] = int(myArray[i] + myArray[i])
    # If it has 2 or more digits, keep only the first and last digits
    else:
        myArray[i] = int((myArray[i])[0] + (myArray[i])[-1])

    # Increment sum by the array's value
    totalSum += myArray[i]

# Prints
#print(myArray)
print(totalSum)


############### AoC Day 1 - Pt. 2 ###############
# Re-read the file and convert to lowercase
myArray = read_file(file_path)
myArray = list(map(str.lower, myArray))

# Create Matrix to match the first column with the second for replaces
matchMatrix = [
    ["one", "o1e"],
    ["two", "t2o"],
    ["three","t3e"],
    ["four", "4"],
    ["five", "5e"],
    ["six", "6"],
    ["seven", "7n"],
    ["eight", "e8t"],
    ["nine", "n9e"],
]

# Reset totalSum = 0
totalSum = 0

# Iterate through each word
for i in range(len(myArray)):

    # Iterate through each match in the matrix
    for match in matchMatrix:
        substring1, substring2 = match

        # Check if the substring exists in the current word
        if substring1 in myArray[i]:

            # Replace the substring with the corresponding number
            myArray[i] = myArray[i].replace(substring1, substring2)
    
    # Only keep the digits of the word
    myArray[i] = ''.join(char for char in myArray[i] if char in includeChars)

    # If the word has no digits, then set it to 0 (to avoid cases where there are no digits at all in the file)
    if len(myArray[i]) == 0:
        myArray[i] = 0
    # If the number has 1 digit, then duplicate it
    elif len(myArray[i]) < 2:
        myArray[i] = int(myArray[i] + myArray[i])
    # If it has 2 or more digits, keep only the first and last digits
    else:
        myArray[i] = int((myArray[i])[0] + (myArray[i])[-1])

    # Increment sum by the array's value
    totalSum += myArray[i]

print(totalSum)