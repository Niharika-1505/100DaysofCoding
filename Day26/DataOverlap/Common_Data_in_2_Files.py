with open("file1.txt") as file1:
    file1_list = file1.readlines()
with open("file2.txt") as file2:
    file2_list = file2.readlines()
common_values_across_files = [int(num) for num in file1_list if num in file2_list]
print(common_values_across_files)
