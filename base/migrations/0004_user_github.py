# Generated by Django 4.1.2 on 2022-11-19 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Github',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
