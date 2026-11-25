scores = []

for i in range(1, 6):
    scores.append(int(input(f"Enter Quiz {i} score:")))

total_score = sum(scores)
number_quizzes = len(scores)
average_score = total_score / number_quizzes
highest = max(scores)
lowest = min(scores)
ascending = sorted(scores)
descending = sorted(scores, reverse=True)
print("===== QUIZ SCORE REPORT =====")
print(f"Quiz Scores: {scores}")
print(f"Number of Quizzes: {number_quizzes}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Ascending: {ascending}")
print(f"Descending: {descending}")
print(f"Original Scores: {scores}")
