# Generated by Django 5.0.6 on 2024-06-01 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announ', '0002_remove_person_id_account_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='images/defaultimage.png', null=True, upload_to='images/'),
        ),
    ]
