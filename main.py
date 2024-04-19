import csv
import os
import os


def main():
    input_path = os.path.join(os.path.curdir, "input_csv")

    input_files = os.listdir(input_path)

    valid_csv_files = [f for f in input_files if f.endswith(".csv")]

    if not valid_csv_files:
        print("No valid CSV input file, exiting.")
        return

    csv_input = os.path.join(input_path, valid_csv_files[0])

    starting_line_str = input("Which line do the names of the students begin (with the first line of the spreadsheet being line 1)? ")
    while not str.isdigit(starting_line_str):
        starting_line_str = input("Invalid number, try again: ")

    starting_line = int(starting_line_str)

    names_array = None

    with open(csv_input, "r") as csv_raw:
        csv_file = csv.reader(csv_raw)

        names_array = list(csv_file)[(starting_line - 1):]

        # This is where the 2023-2024 specific code starts, the code above is
        # perfect for reading CSV files in the future.
        
        # for line in names_array:
        #     print(line)

    first_last = input("Are the names of the students formatted 'Last, First', or 'First, Last'? \
                        \nType one of the following options: \
                        \n1: Last, First \
                        \n2: First, Last \
                        \n3: Already combined in the format 'Last, First'\
                        \n4: Neither, exit\n")
    while first_last not in ["1", "2", "3"]:
        first_last = input("Invalid option. Enter 1, 2, 3, or 4: ")

    if first_last == "4":
        print("Exiting.")
        return

    full_names_array = []

    if first_last in ["1", "2"]:
        first_index, last_index = 1, 0

        if first_last == "2":
            first_index, last_index = 0, 1

        for name in names_array:
            full_names_array.append(f"{name[last_index]}, {name[first_index]}")
    else:
        for name in names_array:
            full_names_array.append(name)

    #test
    # for full_name in full_names_array:
    #     print(full_name)


    canvas_group_name = input("What should the name of the assigning group be? ")


    # Canvas CSV code below
    canvas_path = os.path.join(os.path.curdir, "canvas_csv")
    input_canvas_files = os.listdir(canvas_path)
    valid_canvas_csv_files = [f for f in input_canvas_files if f.endswith(".csv")]

    if not valid_canvas_csv_files:
        print("No valid Canvas CSV file, exiting.")
        return

    canvas_csv_path = os.path.join(canvas_path, valid_canvas_csv_files[0])
    canvas_csv_array = []
    with open(canvas_csv_path, "r") as canvas_csv_raw:
        canvas_csv_array = list(csv.reader(canvas_csv_raw))

    # print(canvas_csv_array)

    for name_assignment in canvas_csv_array:
        if canvas_csv_array.index(name_assignment) == 0:
            continue

        canvas_first_last = name_assignment[0]

        if canvas_first_last in full_names_array:
            name_assignment[4] = canvas_group_name
            print(f"'{canvas_first_last}' is of group '{canvas_group_name}'")

    with open(canvas_csv_path, "w") as canvas_raw_write:
        csv_writer = csv.writer(canvas_raw_write)
        csv_writer.writerows(canvas_csv_array)
        


if __name__ == "__main__":
    main()
