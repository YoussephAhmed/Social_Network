# Generated by Django 2.0.4 on 2018-05-01 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Social_Network', '0003_auto_20180501_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction', models.IntegerField()),
                ('status', models.IntegerField()),
                ('From', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('To', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Social_Network.Profile')),
            ],
        ),
    ]
