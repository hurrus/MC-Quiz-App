import re
from quiz.models import Antworten, Question

"""
Liest das Textfeld mit den MC Fragen ein und speichert diese in der Datenbank mit Hilfe des ORM. 
"""


# Todo: Bitte Unicode in UTF-8 konvertieren. Dient der besseren Lesbarkeit.

def save_questions_to_db(file_n):
    def extract_question_answers(text):
        question_answer_pattern = re.compile(r'^(\d+\.\s*.*?)(\(A\).*?\(B\).*?\(C\).*?\(D\).*?\(E\).*?)(\d+\.|$)',
                                             flags=re.DOTALL | re.MULTILINE)
        matches = question_answer_pattern.finditer(text)
        questions = []
        for match in matches:
            question = match.group(1)
            answers = match.group(2).split('\n')
            answers = [re.sub(r'^\(.\)\s+', "", answer.strip()) for answer in answers if answer]
            extra_text = match.group(3)
            question_answers = {"question": question}
            question_answers["answerA"] = answers[0]
            question_answers["answerB"] = answers[1]
            question_answers["answerC"] = answers[2]
            question_answers["answerD"] = answers[3]
            question_answers["answerE"] = answers[4]
            question_answers["extra_text"] = extra_text
            questions.append(question_answers)
        return questions

    with open(file_n, 'r') as f:
        text = f.read()
        questions = extract_question_answers(text)
        for question in questions:
            question_model = Question(question_text=question['question'])
            question_model.save()
            answer_model = Antworten(
                question=question_model,
                choice_1=question['answerA'],
                choice_2=question['answerB'],
                choice_3=question['answerC'],
                choice_4=question['answerD'],
                choice_5=question['answerE'],
                votes_1=0,
                votes_2=0,
                votes_3=0,
                votes_4=0,
                votes_5=0,
                correct_answer_number=0
            )
            answer_model.save()
