import csv

with open('filename', 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    header = csvreader.header()
    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))
