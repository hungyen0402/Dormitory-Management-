# Generated by Django 5.1.2 on 2024-10-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_core", "0003_deposit_confirm"),
    ]

    operations = [
        migrations.AddField(
            model_name="rooms",
            name="cur_people",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="rooms",
            name="sum_people",
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name="deposit",
            name="date_submit",
            field=models.CharField(max_length=100),
        ),
    ]
