import csv

def transform_user_details(csv_name = "user_details.csv"):
    with open(csv_name) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        iterable_csv = iter(csvreader)
        next(iterable_csv)

        new_user_data = []

        for row in iterable_csv:
            transformation = []
            transformation.append(row[1])
            transformation.append(row[2])
            transformation.append(row[-1])
            new_user_data.append(transformation)
            print(transformation)

        return new_user_data



def create_csv_file(old_user_details = "user_details.csv", new_file_name = "new_user_data.csv"):
    new_user_details = transform_user_details(old_user_details)

    with open(new_file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_details)


create_csv_file()