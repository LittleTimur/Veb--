# Generated by Django 5.0.6 on 2024-06-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announ', '0003_alter_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='defaultimage.png', null=True, upload_to='images/'),
        ),
    ]
