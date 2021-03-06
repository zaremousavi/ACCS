# Generated by Django 2.1.15 on 2021-05-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateCreate', models.DateTimeField(auto_created=True, verbose_name='تاریخ ایجاد')),
                ('Code', models.IntegerField(unique=True, verbose_name='کد شرکت')),
                ('Title', models.CharField(max_length=200, verbose_name='نام شرکت')),
                ('Conditions', models.IntegerField(default=1, verbose_name='وضعیت')),
                ('CreditDate', models.DateTimeField(verbose_name='اعتبار تاریخ')),
            ],
            options={
                'verbose_name': 'شرکت',
                'db_table': 'Company',
                'ordering': ['Code'],
            },
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['Code'], name='Company_Code_4672fb_idx'),
        ),
    ]
