# Generated by Django 2.0.4 on 2018-05-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social_Network', '0003_auto_20180502_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(),
        ),
    ]