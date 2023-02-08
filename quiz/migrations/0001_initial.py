# Generated by Django 4.1.4 on 2023-01-06 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_1', models.CharField(max_length=200)),
                ('choice_2', models.CharField(max_length=200)),
                ('choice_3', models.CharField(max_length=200)),
                ('choice_4', models.CharField(max_length=200)),
                ('choice_5', models.CharField(max_length=200)),
                ('votes_1', models.IntegerField(default=0)),
                ('votes_2', models.IntegerField(default=0)),
                ('votes_3', models.IntegerField(default=0)),
                ('votes_4', models.IntegerField(default=0)),
                ('votes_5', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
            ],
        ),
    ]