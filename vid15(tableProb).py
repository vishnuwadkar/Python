#Write a program to calculate tables of a number and then stor it in a file
i=0
while i < 5:
    n = int(input("Enter a number: "))
    table = [n*i for i in range(1, 11)] #prints a table of numbers from 1 to 10
    with open("table.txt", "a") as f:
        f.write(f"The table of {n} is: {str(table)}\n")  #writes the table to a file
    i+=1

