# Generated by Django 2.0.3 on 2019-04-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0003_problem_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='password',
        ),
        migrations.AddField(
            model_name='userdetail',
            name='institute',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='name',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='rating',
            field=models.IntegerField(default=10020),
        ),
    ]
