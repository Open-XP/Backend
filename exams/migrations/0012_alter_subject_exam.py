# Generated by Django 4.2.7 on 2024-05-25 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0011_alter_waec_total_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='exams.waec'),
        ),
    ]