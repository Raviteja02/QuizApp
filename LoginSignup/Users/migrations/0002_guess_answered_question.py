# Generated by Django 2.2.3 on 2019-07-31 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guess',
            name='answered_question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Users.Question'),
            preserve_default=False,
        ),
    ]