# Function to check if a string is a valid IPv4 address
def is_valid_ip(ip):
    # Split the IP address into parts by '.'
    parts = ip.split(".")
    
    # Check if it has exactly 4 parts
    if len(parts) != 4:
        return False
    
    for part in parts:
        # Check if each part is numeric and within the range 0-255
        if not part.isdigit():  # Ensure it's a number
            return False
        num = int(part)
        if num < 0 or num > 255:  # Ensure it's in the valid range
            return False
        # Prevent leading zeros (e.g., "01")
        if len(part) > 1 and part[0] == "0":
            return False
    
    return True

# Input the IP address to validate
ip_address = input("Enter an IP address: ")

# Validate the IP address
if is_valid_ip(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")
