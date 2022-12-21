#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for z in range(list_length):
        result = 0
        try:
            result = my_list_1[z] / my_list_2[z]
        except IndexError:
            print("{}".format("out of range"))
        except (TypeError, ValueError):
            print("{}".format("division by 0"))
        finally:
            new_list.append(result or 0)
    return (new_list)
