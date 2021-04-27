import csv

with open("PassportInfo.csv") as data:
    passports = csv.reader(data, delimiter=' ')

    tally = 0

    for row in passports:
        print("Value: "+str(row[0]))
        if row[0] != "":
            for i in row:
                if i == "byr" or i== "iyr" or i== "eyr" or i== "hgt" or i== "hcl" or i== "ecl" or i== "pid":
                    counter += 1
                    print(row)
                else:
                    continue
        else: counter = 0

        if counter == 7:
            tally += 1
            print(tally)
        else:
            continue

print(tally)