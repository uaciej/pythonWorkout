'''
 Create a CSV file, in which each line contains 10 random integers between 10
and 100. Now read the file back, and print the sum and mean of the numbers
on each line. 
'''
import csv
from random import randint

def create_csv():
    with open('../randomNumbers.csv', 'w') as f:
        writer = csv.writer(f)
        for _ in range(10):
            numbers = [randint(10, 100) for _ in range(10)]
            writer.writerow(numbers)

def count_from_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                print(f"sum : {sum(int(num) for num in row)}")
                print(f"mean : {sum(int(num) for num in row)/len(row)}\n")


if __name__ == "__main__":
    create_csv()
    count_from_csv("../randomNumbers.csv")
