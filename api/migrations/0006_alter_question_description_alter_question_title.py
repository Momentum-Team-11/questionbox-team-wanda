# Generated by Django 4.0.3 on 2022-04-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_question_description_alter_question_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(default=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(default=True, max_length=100, null=True),
        ),
    ]
