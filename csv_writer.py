import csv

def write(dicts, filename, headers):
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers, lineterminator='\n')

        writer.writeheader()

        for d in dicts:
            # filter to only the columns we want
            row = { column_name: d[column_name] for column_name in headers }
            writer.writerow(row)
