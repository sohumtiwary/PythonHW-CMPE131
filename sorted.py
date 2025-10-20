def reverse_sort_dictionary(data):
    if type(data) is not dict:
        raise TypeError("Input must be a dictionary.")

    result = []
    for key, value in sorted(data.items(), key=lambda item: item[0], reverse=True):
        if type(key) is not str:
            raise TypeError("All keys must be strings (names).")
        if not isinstance(value, (list, tuple)) or len(value) == 0:
            raise TypeError("Each value must be a non-empty tuple or list, e.g., (phone, age).")

        phone_number = value[0]
        if not isinstance(phone_number, int):
            raise TypeError("Phone number must be an integer.")

        result.append((key, phone_number))

    return result
