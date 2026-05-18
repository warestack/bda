# import csv

# with open("movies.csv", "r", newline="", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# import csv

# with open("movies.csv", "r", newline="", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     print(reader)

# import csv

# with open("movies.csv", "r", newline="", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row[4])

####

    


# import csv
# from itertools import islice

# with open("movies.csv", "r", newline="", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     print(header)

#     for _ in range(5):
#         print(next(reader))
    
#     for row in islice(reader, 5):
#         print(row)
    
#     file.seek(0)
#     reader2 = csv.DictReader(file)
#     for row in reader2:
#         if "Action" in row["genres"]:
#             print(row)
#             break

######

import csv

with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
  
    for i, row in enumerate(reader,start=2):
        try:
            int(row["year"])
            int(row["runtime_min"])
            float(row["rating_imdb"])

            int(row["votes"])

            if row["revenue_musd"] != "":
                float(row["revenue_musd"])

            if row["metascore"] != "":
                float(row["metascore"])

        except ValueError as e:
            print(f"Problematic row: {i}")
            print(row)
            print(e)
            break
