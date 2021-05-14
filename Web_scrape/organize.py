import csv

# Sort CSV Data
with open("courseinfo.csv", 'r') as f:
    thereader = csv.reader(f)

    with open("final.csv", 'a', newline='') as fl:
        thewriter = csv.writer(fl)
        thewriter.writerow(["Course Name", "Units",
                            "Description", "Other"])
    for row in thereader:
        row = row[0].split("\n", 3)
        print(row[0])

        with open("final.csv", 'a', newline='') as fl:
            thewriter = csv.writer(fl)
            try:
                thewriter.writerow([row[0], row[1], row[2], row[3]])
            except:
                thewriter.writerow([row[0], row[1], row[2], "nothing"])
