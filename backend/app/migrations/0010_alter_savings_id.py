# Generated by Django 5.1.1 on 2024-12-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savings',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
