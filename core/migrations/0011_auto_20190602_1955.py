# Generated by Django 2.2.1 on 2019-06-02 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190602_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='post_code',
            new_name='postcode',
        ),
    ]
