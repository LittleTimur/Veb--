# Generated by Django 5.0.6 on 2024-06-02 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announ', '0004_profile_is_verified_alter_profile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announmodel',
            name='announ_cat',
        ),
        migrations.RemoveField(
            model_name='announmodel',
            name='id_account',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cate',
        ),
        migrations.DeleteModel(
            name='announmodel',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
