def book_seat(total_seats, booked_seats, seat_number):
   
    if seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked.")
    elif seat_number > total_seats or seat_number < 1:
        print(f"please choose a seat between 1 and {total_seats}.")
    else:
        booked_seats.append(seat_number)
        print(f"Seat {seat_number} has been booked.")

def cancel_seat(total_seats, booked_seats, seat_number):
   
    if seat_number not in booked_seats:
        print(f"Seat {seat_number} is not booked.")
    else:
        booked_seats.remove(seat_number)
        print(f"Booking for seat {seat_number} is canceled successfully.")

def available_seats(total_seats, booked_seats):
    
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

def main():
    
    total_seats = 10
    booked_seats = [2, 5, 7]
    
    
    book_seat(total_seats, booked_seats, 3)  
    cancel_seat(total_seats, booked_seats, 5)  
    cancel_seat(total_seats, booked_seats, 10)  
    
    
    available = available_seats(total_seats, booked_seats)
    print(f"Available seats: {available}")


main()
