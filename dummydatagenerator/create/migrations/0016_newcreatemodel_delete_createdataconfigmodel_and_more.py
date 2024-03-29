# Generated by Django 4.1.7 on 2023-03-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0015_alter_createdataconfigmodel_date_step_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewCreateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=50)),
                ('column_type', models.CharField(max_length=20)),
                ('generate_type', models.CharField(max_length=20)),
                ('link_column_name', models.CharField(max_length=50)),
                ('data_type', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('number_min', models.FloatField()),
                ('number_max', models.FloatField()),
                ('number_step', models.FloatField()),
                ('date_min', models.DateField()),
                ('date_max', models.DateField()),
                ('date_step', models.IntegerField()),
                ('datetime_min', models.DateTimeField()),
                ('datetime_max', models.DateTimeField()),
                ('datetime_step', models.IntegerField()),
                ('link_text', models.TextField()),
                ('link_number_min', models.FloatField()),
                ('link_number_max', models.FloatField()),
                ('link_number_step', models.FloatField()),
                ('link_date_min', models.IntegerField()),
                ('link_date_max', models.IntegerField()),
                ('link_datetime_min', models.IntegerField()),
                ('link_datetime_max', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='CreateDataConfigModel',
        ),
        migrations.DeleteModel(
            name='CreateLinkDataConfigModel',
        ),
        migrations.DeleteModel(
            name='CreateModel',
        ),
    ]
