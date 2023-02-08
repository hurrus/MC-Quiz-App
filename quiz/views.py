from django.shortcuts import render, get_object_or_404, redirect

from quiz.models import Question, Antworten


def question_view(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = Antworten.objects.get(question=question)
    next_question = Question.objects.filter(id__gt=question_id).first()
    prev_question = Question.objects.filter(id__lt=question_id).last()
    next_question_id = next_question.id if next_question else None
    prev_question_id = prev_question.id if prev_question else None
    if request.method == 'POST':
        selected_choice = request.POST.get('choice')
        if selected_choice == '1':
            answers.votes_1 += 1
        elif selected_choice == '2':
            answers.votes_2 += 1
        elif selected_choice == '3':
            answers.votes_3 += 1
        elif selected_choice == '4':
            answers.votes_4 += 1
        elif selected_choice == '5':
            answers.votes_5 += 1
        answers.save()
        return redirect('question_result', question_id=question_id)
    context = {'question': question, 'answers': answers, 'next_question_id': next_question_id,
               'prev_question_id': prev_question_id}
    return render(request, 'quiz/quiz.html', context)


def result_view(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = Antworten.objects.filter(question=question)
    context = {'question': question, 'answers': answers}
    return render(request, 'quiz/result.html', context)
