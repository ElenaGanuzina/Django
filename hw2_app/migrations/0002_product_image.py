# Generated by Django 4.2.4 on 2023-09-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw2_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
