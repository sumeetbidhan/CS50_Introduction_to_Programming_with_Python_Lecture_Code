def main():
    print_square(4)

def print_square(square):
    # for each row in sqaure
    for i in range(square):
        # For each brick in row
        for j in range(square):
            # Print brick
            print(" # ",end='')

        print()

if __name__ == '__main__':
    main()
