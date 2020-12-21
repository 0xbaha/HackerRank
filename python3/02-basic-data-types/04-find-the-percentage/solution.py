if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Extract the value into a list: query_score
    query_score = student_marks[query_name]

    # Sum the score in the list: total_score
    total_score = sum(query_score)

    # Average the scores: avg
    avg = total_score/len(query_score)

    # Print the result
    print("{:.2f}".format(avg))

# NOTES:
# Last code using
#   print("{:.2f}".format(avg))
# instead of 
#   print(round(avg,2))
# because round() function do not give additional 0 in the end

