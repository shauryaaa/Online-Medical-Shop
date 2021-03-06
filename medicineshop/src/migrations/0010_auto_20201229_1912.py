# Generated by Django 3.0.5 on 2020-12-29 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0009_auto_20201215_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='m_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Medicine'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='c_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Customer'),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='c_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Customer'),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='m_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Medicine'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='c_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Customer'),
        ),
    ]
