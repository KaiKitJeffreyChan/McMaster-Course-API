import csv

# Sort CSV Data
with open("courseinfo.csv", 'r') as f:
    thereader = csv.reader(f)
    for row in thereader:
        # row = row.split("\n", 3)
        print(row[0])

        # with open("final.csv", 'w', newline='') as fl:
        #     thewriter = csv.writer(fl)
        #     thewriter.writerow(["Course Name", "Units",
        #                         "Description", "Other"])
        #     try:
        #         thewriter.writerow([row[0], row[1], row[2], row[3]])
        #     except:
        #         thewriter.writerow([row[0], row[1], row[2]])
