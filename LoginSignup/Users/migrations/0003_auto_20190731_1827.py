# Generated by Django 2.2.3 on 2019-07-31 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_guess_answered_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guess',
            name='answer_given',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Users.Choice'),
        ),
    ]