# Generated by Django 2.1.4 on 2019-01-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hillstations',
            name='logo',
            field=models.FileField(default=45, upload_to=''),
            preserve_default=False,
        ),
    ]
