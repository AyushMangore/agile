# Generated by Django 3.2.7 on 2021-11-12 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nemesis', '0005_myuser_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='verification_status',
            field=models.CharField(default='Not Verified', max_length=100),
        ),
    ]
