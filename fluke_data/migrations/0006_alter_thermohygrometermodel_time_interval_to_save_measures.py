# Generated by Django 5.0.7 on 2024-09-05 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fluke_data', '0005_remove_calibrationcertificatemodel_instrument_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thermohygrometermodel',
            name='time_interval_to_save_measures',
            field=models.IntegerField(default=5),
        ),
    ]
