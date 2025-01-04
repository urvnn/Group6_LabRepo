def main():
    filename = input("Enter the filename: ")
    print (filename)
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    while True:
        print(f"The file has {len(lines)} lines.")
        line_number = int(input("Enter a line number (0 to quit): "))
        
        if line_number == 0:
            break
        elif 1 <= line_number <= len(lines):
            print(lines[line_number - 1].strip())
        else:
            print("Invalid line number.")

if __name__ == "__main__":
    main()
