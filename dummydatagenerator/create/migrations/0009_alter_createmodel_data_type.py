# Generated by Django 4.1.7 on 2023-03-07 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0008_alter_createmodel_data_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createmodel',
            name='data_type',
            field=models.TextField(choices=[('1', '文字'), ('2', '数値'), ('3', '日付'), ('4', '日時')], default='日付', verbose_name='データタイプ'),
        ),
    ]
