# Part 1: Average Rainfall Calculation

# Ask for the number of years
num_years = int(input("Enter the number of years: "))

# Initialize variables
total_months = 0
total_rainfall = 0.0

# Outer loop for each year
for year in range(num_years):
    print(f"\nYear {year + 1}")
    # Inner loop for each month
    for month in range(1, 13):
        while True:
            try:
                rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
                if rainfall < 0:
                    print("Please enter a non-negative number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        total_rainfall += rainfall
        total_months += 1

# Calculate the average rainfall per month
average_rainfall = total_rainfall / total_months

# Display the results
print(f"\nTotal number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")