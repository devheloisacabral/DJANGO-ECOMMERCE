# Generated by Django 5.0.6 on 2024-07-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='marca_imgs/'),
        ),
    ]
