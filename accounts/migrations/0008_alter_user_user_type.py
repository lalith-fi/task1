# Generated by Django 3.2 on 2021-08-05 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor')], default='Patient', max_length=255),
        ),
    ]
