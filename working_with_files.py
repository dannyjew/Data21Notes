def open_and_print_file(file):
    try:
        # opens file
        opened_file = open(file, "r")  # default opens to read mode however we put "r" there to confirm its in read mode
        file_line_list = opened_file.readlines()
        for i in file_line_list:
            print(i.strip())

        # closes file
        opened_file.close()

    except FileNotFoundError as errmsg:
        print("There has been an error opening your file!")
        print(errmsg)
        raise

    finally:
        print("Execution Complete")


# write a function which writes to a file
def write_to_file(file, order_item):
    try:
        # this is another way to make the file close once it has been processed. "w" means to open in write mode, "a" means to append
        with open(file, "a") as opened_file:
            opened_file.write(order_item + "\n")
    except FileNotFoundError:
        print("file cannot be found")

# now lets use the two functions
write_to_file("order.txt", "lettuce")
open_and_print_file("order.txt")

