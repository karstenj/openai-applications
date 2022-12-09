def solution_2022_1_2(input_list):
    result = 0
    current_total = 0
    top_three = []

    for item in input_list:
        if item == '':
            top_three.append(current_total)
            top_three.sort(reverse=True)
            top_three = top_three[:3]
            current_total = 0
        else:
            current_total += int(item)

    result = sum(top_three)
    return result