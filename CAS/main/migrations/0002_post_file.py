# Generated by Django 2.2.4 on 2019-09-02 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default=1, upload_to='files'),
            preserve_default=False,
        ),
    ]
