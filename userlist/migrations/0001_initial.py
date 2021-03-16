# Generated by Django 3.1.5 on 2021-03-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.TextField(default='')),
                ('status', models.CharField(choices=[('1', 'Done'), ('2', 'Pending')], default='2', max_length=20)),
                ('user', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
