# Generated by Django 2.0.8 on 2018-09-27 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='psa_members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('employer', models.CharField(max_length=200)),
                ('membership_number', models.CharField(max_length=5)),
                ('application_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
