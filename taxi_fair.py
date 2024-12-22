def calculate_fare(distance):
    # Validate distance
    base_fare = 50  # Base fare for each trip
    distance_fare = 10  # Fare per kilometer
    
    
    total_fare = base_fare + (distance_fare * distance)
    return total_fare

def main():
  
    trips = [5, 10, 3]
    
    total_fare = 0  
    
   
    for i, distance in enumerate(trips, 1):
        fare = calculate_fare(distance)
        print(f"Trip {i}: ${fare}")
        total_fare += fare  
    
    
    print(f"Total Fare: ${total_fare}")


main()
