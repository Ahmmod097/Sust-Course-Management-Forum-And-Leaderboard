# Generated by Django 3.1.5 on 2021-06-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_teacherinfo_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherinfo',
            name='code',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
