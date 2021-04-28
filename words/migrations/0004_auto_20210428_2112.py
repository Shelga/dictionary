# Generated by Django 3.1.4 on 2021-04-28 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_auto_20210427_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='DictionaryLine',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=50)),
                ('translation', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('password_conf', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Dictionary',
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
        migrations.AddField(
            model_name='dictionaryline',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words.user'),
        ),
    ]