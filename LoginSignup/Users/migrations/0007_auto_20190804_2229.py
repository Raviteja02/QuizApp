# Generated by Django 2.2.3 on 2019-08-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_quiz_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='score',
            field=models.CharField(max_length=10, null=True),
        ),
    ]