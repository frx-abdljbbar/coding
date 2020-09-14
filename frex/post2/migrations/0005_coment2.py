# Generated by Django 3.1 on 2020-09-03 23:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post2', '0004_remove_post2_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coment2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment', models.CharField(max_length=500)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post2.post2')),
            ],
        ),
    ]
