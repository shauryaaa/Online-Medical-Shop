# Generated by Django 3.1.3 on 2020-12-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0007_auto_20201214_2206'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='order_id',
            new_name='c_id',
        ),
        migrations.AddField(
            model_name='orderlist',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
