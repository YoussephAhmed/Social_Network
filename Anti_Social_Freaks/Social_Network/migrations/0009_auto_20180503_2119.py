# Generated by Django 2.0.4 on 2018-05-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social_Network', '0008_auto_20180503_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
