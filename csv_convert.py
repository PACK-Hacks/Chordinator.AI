import csv

def write_to_csv(array1, array2, filename):
    # Check if the lengths of the arrays are equal
    if len(array1) != len(array2):
        raise ValueError("The arrays must be of the same length.")

    # Create an association list
    association_list = list(zip(array1, array2))

    # Write the association list to a CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(['Element from Array 1', 'Element from Array 2'])  # Writing headers
        for pair in association_list:
            writer.writerow(pair)

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = ['a', 'b', 'c', 'd', 'e']
filename = 'output.csv'

write_to_csv(array1, array2, filename)