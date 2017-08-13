def get_average_from_list(list_of_numbers):
    total_sum = 0
    number_count = len(list_of_numbers)

    if number_count == 0:
        return total_sum

    for number in list_of_numbers:
        total_sum += number
    return total_sum / number_count


def skip_one_line(file_iterator):
    next(file_iterator)