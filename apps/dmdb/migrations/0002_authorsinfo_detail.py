# Generated by Django 2.0.3 on 2019-05-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorsinfo',
            name='detail',
            field=models.CharField(default='', max_length=4096),
        ),
    ]
