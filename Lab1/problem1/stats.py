def mean(listofnumbers):
    if not listofnumbers:
        return None
    return sum(listofnumbers) / len(listofnumbers)

def median(listofnumbers):
    if not listofnumbers:
        return None
    sortednum = sorted(listofnumbers)
    n = len(sortednum)
    mid = n // 2
    if n % 2 == 1:  # Odd length
        return sortednum[mid]
    else:  # Even length
        return (sortednum[mid - 1] + sortednum[mid]) / 2

def mode(listofnumbers):
    if not listofnumbers:
        return None
    frequency = {}
    for number in listofnumbers:
        frequency[number] = frequency.get(number, 0) + 1

    maxfreq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == maxfreq]

    if len(modes) == len(listofnumbers):
        return None
    elif len(modes) == 1:
        return modes[0]
    else:
        return modes

if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        listofnumbers = list(map(float, user_input.split()))
        print(f"Mean: {mean(listofnumbers)}")
        print(f"Median: {median(listofnumbers)}")
        print(f"Mode: {mode(listofnumbers)}")
    except ValueError:
        print("Please enter valid numbers.")
