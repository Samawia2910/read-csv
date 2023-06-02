import csv
import pandas as pd
# import csv
# import pandas as pd
# with open("./test.csv", 'r') as file:
#   csvreader = csv.reader(file)
#   for row in csvreader:
#     print(row)

# data = pd.read_csv("test.csv")
# print(data)
# with open("./test.csv", 'r') as file:
#   csvreader = csv.reader(file, delimiter=':')
#   for row in csvreader:["Carname"]
#     print(row)
# data = pd.read_csv("test.csv", delimiter= ':')
# data
# import csv
#
# with open("./test.csv", 'r') as file:
#     csv_reader = csv.reader(file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]}  {row[3]}')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

# import csv
# import pandas as pd
# df = pd.read_csv("test.csv", usecols= ["Carname", "Speed"])
# print("The dataframe is:")
# print(df)
# # saving the dataframe
# # df.to_csv(r'E:\Project\readcsv\newfile.csv')
# df = pd.read_csv("test.csv", usecols= ["Carname","Color", "Age", "Speed", "AutoPass"])
# grouped = df.groupby(['AutoPass'])
# df1 = grouped.get_group(("Y"))
# print("The dataframe is:")
# print(df1)
# df1.to_csv(r'E:\Project\readcsv\newfile11.csv')

df = pd.read_csv("test.csv", usecols= ["Carname", "Speed"])
print("The dataframe is:")
print(df)
df.to_csv(r'E:\Project\readcsv\newfile.csv')

