# Generated by Django 4.2.9 on 2024-01-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_archives'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archives',
            name='file',
            field=models.FileField(max_length=245, upload_to='file/'),
        ),
    ]