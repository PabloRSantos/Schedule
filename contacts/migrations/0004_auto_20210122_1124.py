# Generated by Django 3.1.5 on 2021-01-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/%Y/%m'),
        ),
    ]