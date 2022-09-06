####### open file ######
with open('first_file.txt') as f:
    first_data = f.readlines()
    print(first_data)

with open('second_file.txt') as s:
    second_data = s.readlines()
    print(second_data)

######## compare file #####

result_1 = [num for num in first_data if num in second_data]

# to remove the new space sign(\n and string)
result_2 = [int(num) for num in first_data if num in second_data]

####### extract #########

print(result_1)
print(result_2)