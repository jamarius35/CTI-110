# Jamarius Berry
# 11/5/2024
# P4HW1
# Calculate grades and give an average along with letter grade


def get_letter_grade(average):
    """Return the letter grade based on the numerical average."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def get_valid_score():
    """Get a valid score between 0 and 100 from the user."""
    while True:
        try:
            score = float(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score! Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")

# Enter your scores in this program
try:
    # Get number of scores from user
    while True:
        try:
            num_scores = int(input("How many scores would you like to enter? "))
            if num_scores > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    # Collect scores
    student_scores = []
    for i in range(num_scores):
        print(f"\nEntering score {i + 1} of {num_scores}")
        score = get_valid_score()
        student_scores.append(score)

    # Display results
    print("\nResults:")
    print("-" * 40)
    
    # Find and display lowest score
    lowest_score = min(student_scores)
    print(f"Lowest score: {lowest_score}")

    # Remove lowest score and display modified list
    modified_scores = student_scores.copy()
    modified_scores.remove(lowest_score)
    print(f"Scores after dropping lowest: {modified_scores}")

    # Calculate and display average
    average = sum(modified_scores) / len(modified_scores)
    print(f"Average of modified scores: {average:.2f}")

    # Display letter grade
    letter_grade = get_letter_grade(average)
    print(f"Letter Grade: {letter_grade}")

except Exception as e:
    print(f"An error occurred: {e}")
