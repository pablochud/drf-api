# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('slogan', models.CharField(max_length=500)),
                ('founded_date', models.CharField(max_length=500)),
                ('website', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('number', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('hired_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('number', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=1000)),
                ('opening_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('business_hours_start', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)], default=8)),
                ('business_hours_end', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)], default=17)),
                ('chain', models.ForeignKey(to='retail.Chain')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='store',
            field=models.ForeignKey(to='retail.Store'),
        ),
    ]
