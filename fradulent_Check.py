import csv
import pandas

url='config1.properties'
dataset=pandas.read_csv(url)

with open('config1.properties', 'rb') as master:
    master_indices = dict((r[5], i) for i, r in enumerate(csv.reader(master)))

with open('tot_cr_txn_after.csv', 'rb') as hosts:
    with open('results.csv', 'wb') as results:    
        reader = csv.reader(hosts)
        writer = csv.writer(results)

        writer.writerow(next(reader, []) + ['RESULTS'])

        for row in reader:
            index = master_indices.get(row[1])
            print(index)
            if dataset['Total_deposits']>1000:
                message = 'FOUND ABNORMAL in master list (row {})'
            else:
                message = 'NOT FOUND in master list'
            writer.writerow(row + [message])