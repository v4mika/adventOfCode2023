import re
import csv

f = open("adventofcode.com_2023_day_1_input.txt", "r")

def convertLine(line):
    nums_dict = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven": 7, "eight":8, "nine":9}
    i, j = 0, 0
    ret = []
    while (j < len(line)):
        for num in nums_dict.keys():
            new_num = -1
            if num in line[i:j]:
                new_num = nums_dict[num]
                ret.append(new_num)
                i = j - 1 # accounts for overlapping words eg "twone"
                break
        if line[j].isdigit():
            new_num = int(line[j])
            ret.append(new_num)
            i = j
        j += 1
    return ret
    
with open("adventofcode.com_2023_day_1_input.txt", "r") as f:
    # csv_file = open('day1tracker.csv', 'w', newline='')
    # spamwriter = csv.writer(csv_file)
    sum = 0
    for line in f:
        nums = convertLine(line)
        first = str(nums[0])
        last = str(nums[-1])
        num = int(first + last)
        sum += num
        # spamwriter.writerow([line.strip(), nums, num, sum])
print("final answer", sum)
# csv_file.close()