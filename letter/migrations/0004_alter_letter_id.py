# Generated by Django 4.0.6 on 2022-08-01 08:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0003_alter_letter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
