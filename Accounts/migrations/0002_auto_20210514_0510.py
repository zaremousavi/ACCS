# Generated by Django 2.1.15 on 2021-05-14 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupacc',
            name='kind',
            field=models.CharField(choices=[('1', 'ترازنامه ای'), ('2', 'سود و زیانی'), ('3', 'کنترلی')], max_length=1, verbose_name='نوع'),
        ),
    ]