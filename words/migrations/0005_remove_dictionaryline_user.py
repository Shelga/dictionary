# Generated by Django 3.1.4 on 2021-04-29 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_auto_20210428_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dictionaryline',
            name='user',
        ),
    ]