import numpy as n

def run_timing():
    times = []
    while True:
        one_run = input("Enter 10km run time: ")
        if not one_run:
            break
        try:
            times.append(float(one_run))
        except ValueError:
            print("Invalid input. Please enter a number.")

    if times == []:
        return "No data provided"
    avgtime = n.average(times)

    return(f"The average time over {len(times)} runs is {avgtime}")

if __name__ == "__main__":
    print(run_timing())
    