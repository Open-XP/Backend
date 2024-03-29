# Generated by Django 5.0 on 2024-01-01 18:51

import django.db.models.deletion
import exams.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0010_exam_exam_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Grade',
                'verbose_name_plural': 'Grades',
            },
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_type',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='exams.exam'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterUniqueTogether(
            name='subject',
            unique_together={('name', 'exam')},
        ),
        migrations.AddField(
            model_name='topic',
            name='grade',
            field=models.ForeignKey(default=exams.models.get_default_grade, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='exams.grade'),
        ),
        migrations.AlterUniqueTogether(
            name='topic',
            unique_together={('name', 'grade', 'subject')},
        ),
    ]
