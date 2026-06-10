# Railway Reservation Seat Analyzer

seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# Function to count booked and available seats
def count_seats(seats):
    booked = seats.count("Booked")
    available = seats.count("Available")
    return booked, available

# Function to find the first available seat
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1   # Seat numbers start from 1
    return None

# Function to calculate occupancy percentage
def occupancy_percentage(seats):
    booked = seats.count("Booked")
    return (booked / len(seats)) * 100

# Function to display available seat numbers
def display_available_seats(seats):
    print("Available Seat Numbers:", end=" ")
    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1, end=" ")
    print()

# Main Program
booked, available = count_seats(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)

print("\nFirst Available Seat:", first_available(seats))

print("\nOccupancy Percentage: {:.2f}%".format(
    occupancy_percentage(seats)
))

display_available_seats(seats)
