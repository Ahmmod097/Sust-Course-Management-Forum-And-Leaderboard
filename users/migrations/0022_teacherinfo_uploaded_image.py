# Generated by Django 3.1.5 on 2021-07-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20210713_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherinfo',
            name='uploaded_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]