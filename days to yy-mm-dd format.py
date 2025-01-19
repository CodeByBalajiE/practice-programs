# Function to convert total days into years, months, and days
def convert_days_to_ymd(total_days):
    # Assume a year has 365 days and a month has 30 days
    year = total_days // 365  # Calculate number of years
    remaining_days = total_days % 365  # Remaining days after years
    month = remaining_days // 30  # Calculate number of months
    days = remaining_days % 30  # Remaining days after months
    
    return year, month, days

# Input total number of days
total_days = int(input("Enter the total number of days: "))

# Convert days to years, months, and days
years, months, days = convert_days_to_ymd(total_days)

# Display the result
print(f"{total_days} days is equivalent to:")
print(f"{years} year(s), {months} month(s), and {days} day(s).")
