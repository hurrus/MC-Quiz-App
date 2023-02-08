from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Antworten(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_1 = models.CharField(max_length=200)
    votes_1 = models.IntegerField(default=0)
    choice_2 = models.CharField(max_length=200)
    votes_2 = models.IntegerField(default=0)
    choice_3 = models.CharField(max_length=200)
    votes_3 = models.IntegerField(default=0)
    choice_4 = models.CharField(max_length=200)
    votes_4 = models.IntegerField(default=0)
    choice_5 = models.CharField(max_length=200)
    votes_5 = models.IntegerField(default=0)
    correct_answer_number = models.IntegerField(default=0)
