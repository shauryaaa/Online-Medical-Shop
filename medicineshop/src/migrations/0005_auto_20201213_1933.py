# Generated by Django 3.1.3 on 2020-12-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_auto_20201213_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='percent',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.IntegerField(),
        ),
    ]
