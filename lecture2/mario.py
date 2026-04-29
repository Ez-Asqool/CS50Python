# for _ in range(3):
#     print("#")

#print 
#
#
#


# def main():
#     print_column(3)


# def print_column(height):
#     # for _ in range(height):
#     #     print("#")
#     print("#\n" * height , end="")

# main()


#print ????
# def main():
#     print_row(4)


# def print_row(width):
#     # for _ in range(width):
#     #     print("?", end="")
#     print("?" * width )

# main()

"""
    print 3*3 squares
"""

def main():
    print_square(3)

# def print_square(size):
#         #for each row in square
#     for i in range(size):
#             #for each brick in row 
#         for j in range(size):
#                 #print brick
#             print("#", end="")
#         #move cursor to new line
#         print()
    
# def print_square(size):
#     for _ in range(size):
#         print("#" * size)

def print_square(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
