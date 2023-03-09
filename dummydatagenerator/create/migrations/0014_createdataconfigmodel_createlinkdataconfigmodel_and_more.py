# Generated by Django 4.1.7 on 2023-03-07 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0013_alter_createmodel_column_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateDataConfigModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('number_min', models.FloatField()),
                ('number_max', models.FloatField()),
                ('number_step', models.FloatField()),
                ('date_min', models.DateField()),
                ('date_max', models.DateField()),
                ('date_step', models.DateField()),
                ('datetime_min', models.DateTimeField()),
                ('datetime_max', models.DateTimeField()),
                ('datetime_step', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CreateLinkDataConfigModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('number_min', models.FloatField()),
                ('number_max', models.FloatField()),
                ('number_step', models.FloatField()),
                ('date_min', models.IntegerField()),
                ('date_max', models.IntegerField()),
                ('datetime_min', models.IntegerField()),
                ('datetime_max', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='createmodel',
            name='data_type',
            field=models.CharField(max_length=20),
        ),
    ]