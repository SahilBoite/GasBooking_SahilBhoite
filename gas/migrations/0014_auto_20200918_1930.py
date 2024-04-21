# Generated by Django 3.1 on 2020-09-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('gas', '0013_auto_20200918_1927'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GasReffling',
            new_name='GasReffiling',
        ),
        migrations.AlterModelOptions(
            name='gasreffiling',
            options={'verbose_name': 'GasReffiling',
                     'verbose_name_plural': '3.Gas Reffiling'},
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='reffeling',
            new_name='reffiling',
        ),
        migrations.RenameField(
            model_name='gasreffiling',
            old_name='reffeling_size',
            new_name='reffiling_size',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(
                blank=True, default='xvX9J7oL', editable=False, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='connection_number',
            field=models.CharField(
                blank=True, default='mPKclxuc', editable=False, max_length=10, unique=True),
        ),
    ]