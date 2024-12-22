def calculate_positive_feedback_percentage(ratings):
    
    
    if len(ratings) == 0:  
        return 0.0

  # Count the number of positive ratings (4 or 5) in the list.
    positive_ratings = sum(1 for rating in ratings if rating == 4 or rating == 5)
    
    # Calculate the positive feedback percentage as a percentage of the total number of ratings.
    positive_percentage = (positive_ratings / len(ratings)) * 100
    return positive_percentage

def main():
    ratings = [5, 4, 3, 5, 2, 4, 1, 5]
    positive_feedback_percentage = calculate_positive_feedback_percentage(ratings)
    print(f"Positive Feedback: {positive_feedback_percentage:.2f}%")


main()
