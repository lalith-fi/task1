# Generated by Django 3.2 on 2021-08-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Address',
            field=models.TextField(blank=True, max_length=1050),
        ),
    ]
