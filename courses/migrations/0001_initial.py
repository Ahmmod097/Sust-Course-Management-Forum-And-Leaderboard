# Generated by Django 3.1.5 on 2021-06-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=120)),
                ('course_code', models.CharField(max_length=6)),
                ('teacher_name', models.CharField(max_length=120)),
            ],
        ),
    ]
