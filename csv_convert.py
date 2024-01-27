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
        for pair in association_list:
            writer.writerow(pair)










# Same as write_to_csv except it expects 3 arrays
def write_to_csv_triple(array1, array2, array3, filename):
    # Check if the lengths of the arrays are equal
    if len(array1) != len(array2) or len(array1) != len(array3):
        raise ValueError("The arrays must be of the same length.")

    # Create an association list
    association_list = list(zip(array1, array2, array3))

    # Write the association list to a CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        for pair in association_list:
            writer.writerow(pair)