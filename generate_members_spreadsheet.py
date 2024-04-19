import csv
import os


def main():
    canvas_input_path = os.path.join(os.path.curdir, "canvas_csv")
    canvas_input_files = os.listdir(canvas_input_path)

    valid_csv_files = [f for f in canvas_input_files if f.endswith(".csv")]

    if not valid_csv_files:
        print("No valid Canvas CSV file, exiting.")
        return

    canvas_csv_path = os.path.join(canvas_input_path, valid_csv_files[0])
    canvas_csv = []
    with open(canvas_csv_path, "r") as cavnas_csv_raw:
        canvas_csv = list(csv.reader(cavnas_csv_raw))

    class_year = input("Please input the graduating year of the class for the spreadsheet being generated: ")
    while not str.isnumeric(class_year):
        class_year = input("Please input a valid year: ")

    class_list = [[f"Class of {class_year}", ""],
                  ["Last Name", "First Name"]]

    for line in canvas_csv:
        if canvas_csv.index(line) == 0: continue

        full_name = line[0].split(", ")
        first_name, last_name = full_name[1], full_name[0]
        if class_year in line[4]:
            class_list.append([last_name, first_name])


    csv_output_path = os.path.join(os.curdir, f"Current{class_year}Members.csv")
    with open(csv_output_path, "w") as csv_raw_write:
        csv_writer = csv.writer(csv_raw_write)
        csv_writer.writerows(class_list)

    


if __name__ == "__main__":
    main()
