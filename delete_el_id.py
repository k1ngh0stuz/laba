def delete_id():
    numbers = [100, 101, 102, 103, 104, 105, 106]

    numbers.remove(int(input()))
    return numbers


print(delete_id())