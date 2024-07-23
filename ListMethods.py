class ListMethods():
    @staticmethod
    def find_smallest(num_arr):
        if len(num_arr) != 0:
            smallest = num_arr[0]
            for item in num_arr:
                if item < smallest:
                    smallest = item
            return smallest
        else:
            return None

    @staticmethod
    def find_largest(num_arr):
        if len(num_arr) != 0:
            largest = num_arr[0]
            for item in num_arr:
                if item > largest:
                    largest = item
            return largest
        else:
            return None

    @staticmethod
    def remove_duplicates(num_arr):
        new_arr = []
        if len(num_arr) != 0:
            for num in num_arr:
                if ListMethods.check_item(new_arr, num) != True:
                    new_arr.append(num)
        return new_arr

    @staticmethod
    def check_item(num_arr, element):
        if len(num_arr) != 0:
            for item in num_arr:
                if item == element:
                    return True
        return False

    @staticmethod
    def second_largest(num_arr):
        if len(num_arr) != 0:
            highest = num_arr[0]
            second_max = num_arr[1]

            for item in num_arr:
                if item > highest:
                    second_max = highest
                    highest = item
                elif item > second_max and item != highest:
                    second_max = item
            return second_max
        else:
            return None

    @staticmethod
    def second_smallest(num_arr):
        if len(num_arr) != 0:
            lowest = num_arr[0]
            second_min = num_arr[1]

            for item in num_arr:
                if item < lowest:
                    second_min = lowest
                    lowest = item
                elif item < second_min and item != lowest:
                    second_min = item
            return second_min
        else:
            return None

    @staticmethod
    def nth_highest(num_arr, nth_value):
        if len(num_arr) != 0:
            temp_arr = ListMethods.remove_duplicates(num_arr)
            highest_arr = []

            for rep in range(nth_value):
                if nth_value >= len(temp_arr):
                    return ListMethods.find_smallest(temp_arr)
                elif nth_value == 1:
                    return ListMethods.find_largest(temp_arr)
                elif nth_value == 2:
                    return ListMethods.second_largest(num_arr)
                else:
                    highest = ListMethods.find_smallest(temp_arr)
                    for item in temp_arr:
                        if item > highest and ListMethods.check_item(highest_arr, item) != True:
                            highest = item
                    highest_arr.append(highest)
            return highest_arr[-1]
        else:
            return None

    @staticmethod
    def nth_lowest(num_arr, nth_value):
        if len(num_arr) != 0:
            temp_arr = ListMethods.remove_duplicates(num_arr)
            lowest_arr = []

            for rep in range(nth_value):
                if nth_value >= len(temp_arr):
                    return ListMethods.find_largest(temp_arr)
                elif nth_value == 1:
                    return ListMethods.find_smallest(temp_arr)
                elif nth_value == 2:
                    return ListMethods.second_smallest(num_arr)
                else:
                    lowest = ListMethods.find_largest(temp_arr)
                    for item in temp_arr:
                        if item < lowest and ListMethods.check_item(lowest_arr, item) != True:
                            lowest = item
                    lowest_arr.append(lowest)
            return lowest_arr[-1]
        else:
            return None

arr = [5, 7, 1, 2, 10, 11, 12, 13, 15]
uniqueLength = len(ListMethods.remove_duplicates(arr))
print(f"Highest to Lowest")
for i in range(uniqueLength):
    print(f"{(i + 1)} --> {ListMethods.nth_highest(arr, (i + 1))}")
print(f"\nLowest to Highest")
for i in range(uniqueLength):
    print(f"{(i + 1)} --> {ListMethods.nth_lowest(arr, (i + 1))}")
