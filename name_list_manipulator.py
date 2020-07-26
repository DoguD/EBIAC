import csv

# Open and read
male_names_file = open('src/names/tr_isim_erkek.csv')
female_names_file = open('src/names/tr_isim_kadin.csv')
male_names = csv.reader(male_names_file)
female_names = csv.reader(female_names_file)

# Create separate lists
male_names_list = []
for name in male_names:
    if name[0] == '[isim]':
        continue
    male_names_list.append((name[0], int(name[1])))
female_names_list = []
for name in female_names:
    if name[0] == '[isim]':
        continue
    female_names_list.append((name[0], int(name[1])))

# Create mixed list
mixed_list = []

min_length = min(len(male_names_list), len(female_names_list))
for index in range(min_length):
    mixed_list.append(female_names_list[index])
    mixed_list.append(male_names_list[index])
female_names_list = female_names_list[min_length]
for name in female_names_list:
    mixed_list.append(name)


# Sort the list according to use count
def sort_tuple(tup):
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            try:
                if (tup[j][1] > tup[j + 1][1]):
                    temp = tup[j]
                    tup[j] = tup[j + 1]
                    tup[j + 1] = temp
            except:
                pass
    return tup

mixed_list = sort_tuple(mixed_list)

# Write to file
output = open('src/names/ordered_mixed_name_list.csv', 'wb')
csv_out = csv.writer(output)
for row in mixed_list:
    try:
        csv_out.writerow(row)
    except:
        pass
