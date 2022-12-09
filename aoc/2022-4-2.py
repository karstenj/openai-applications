def solution_2022_4_2(input_list):
    result = 0

    for pair in input_list:
        start1, end1 = [int(x) for x in pair.split(',')[0].split('-')]
        start2, end2 = [int(x) for x in pair.split(',')[1].split('-')]

        if start1 <= end2 and end1 >= start2:
            result += 1
    return result