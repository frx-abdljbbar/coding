# Generated by Django 3.1 on 2020-09-03 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post2',
            name='link',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
