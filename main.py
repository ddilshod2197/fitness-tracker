def survey_result_analyzer(survey_results):
    # Har bir savol bo'yicha foizlarni hisoblash
    for i, question in enumerate(survey_results):
        answers = question['answers']
        max_answer = max(answers, key=answers.get)
        max_answer_count = answers[max_answer]
        total_count = sum(answers.values())
        print(f"Savol {i+1}: {question['question']}")
        print(f"Eng ko'p tanlangan javob: {max_answer} ({max_answer_count} / {total_count} * 100%)")

    # Eng ko'p tanlangan javobni toping
    max_answer_counts = {}
    for question in survey_results:
        answers = question['answers']
        max_answer = max(answers, key=answers.get)
        max_answer_counts[max_answer] = max_answer_counts.get(max_answer, 0) + 1

    max_answer = max(max_answer_counts, key=max_answer_counts.get)
    print(f"Eng ko'p tanlangan javob: {max_answer}")

# Masalan
survey_results = [
    {'question': 'Q1', 'answers': {'A': 10, 'B': 5, 'C': 15}},
    {'question': 'Q2', 'answers': {'A': 20, 'B': 10, 'C': 10}},
    {'question': 'Q3', 'answers': {'A': 15, 'B': 20, 'C': 5}}
]

survey_result_analyzer(survey_results)
