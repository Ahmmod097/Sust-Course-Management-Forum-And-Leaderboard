# Generated by Django 3.1.5 on 2021-07-14 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_teacherinfo_uploaded_image'),
        ('courses', '0009_auto_20210713_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.teacherinfo'),
        ),
    ]
