# Generated by Django 3.1.4 on 2021-03-20 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19App', '0006_economy20'),
    ]

    operations = [
        migrations.CreateModel(
            name='economy21',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country21', models.CharField(max_length=220)),
                ('gdp21', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'economy21',
            },
        ),
    ]
