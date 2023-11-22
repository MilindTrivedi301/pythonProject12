import csv

temp_data = []
id_update = 2
new_age = 33

with open('mydata.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp_data.append(row)

# for row in temp_data:
#     print(row[0])
#     print(row[2])
#     if row[0] == id_update:
#         row[2] = new_age

temp_data[2][2] = 27
print(temp_data)



with open('mydata.csv','w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(temp_data)