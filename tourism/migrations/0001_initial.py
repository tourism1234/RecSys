# Generated by Django 2.1.4 on 2019-01-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HillStations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('region', models.CharField(max_length=300)),
                ('airport_dist', models.FloatField()),
                ('railway_dist', models.FloatField()),
                ('elevation', models.IntegerField()),
                ('avg_rating', models.FloatField()),
            ],
        ),
    ]
