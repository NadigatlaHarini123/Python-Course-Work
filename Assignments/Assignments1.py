# -------------------------------
# BookMyShow Ticket Booking System
# -------------------------------

# Taking booking details from the user

# Booking ID (integer)
booking_id = int(input("Enter Booking ID: "))

# User name (string)
user_name = input("Enter User Name: ")

# Movie name (string)
movie_name = input("Enter Movie Name: ")

# Ticket price (float)
ticket_price = float(input("Enter Ticket Price: "))

# Selected seats (list) – split by comma
seats = input("Enter Selected Seats (comma-separated): ").split(",")

# Show timings stored as a tuple (start time, end time)
start_time = input("Enter Show Start Time: ")
end_time = input("Enter Show End Time: ")
show_timings = (start_time, end_time)

# Discount percentage (float)
discount = float(input("Enter Discount Percentage: "))

# Theatre facilities stored as a set (unique values)
facilities = set(input("Enter Theatre Facilities (comma-separated): ").split(","))

# Theatre details (dictionary)
theatre_name = input("Enter Theatre Name: ")
theatre_location = input("Enter Theatre Location: ")
screen_number = int(input("Enter Screen Number: "))

theatre_details = {
    "Name": theatre_name,
    "Location": theatre_location,
    "Screen": screen_number
}

# -------------------------------
# Displaying output using different formatting methods
# -------------------------------

# Using comma separation (sep=',')
print("\n--- Using Comma Separation (sep=',') ---")
print("Booking ID, User, Movie:", booking_id, user_name, movie_name, sep=", ")

# Using percentage formatting (% operator)
print("\n--- Using Percentage Formatting (% operator) ---")
print("Discount Applied: %.2f%%" % discount)

# Using f-strings
print("\n--- Using f-strings ---")
print(f"User Name: {user_name}")
print(f"Movie Name: {movie_name}")
print(f"Ticket Price: ₹{ticket_price}")
print(f"Show Time: {show_timings[0]} - {show_timings[1]}")
print(f"Seats Booked: {', '.join(seats)}")

# Using .format() method
print("\n--- Using .format() Method ---")
print("Theatre Details: Name - {}, Location - {}, Screen - {}".format(
    theatre_details["Name"],
    theatre_details["Location"],
    theatre_details["Screen"]
))

