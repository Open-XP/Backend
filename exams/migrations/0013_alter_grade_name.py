# Generated by Django 5.0 on 2024-01-01 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0012_alter_question_subject_alter_question_topic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='name',
            field=models.CharField(choices=[('SS1', 'SS 1'), ('SS2', 'SS 2'), ('SS3', 'SS 3')], max_length=15),
        ),
    ]