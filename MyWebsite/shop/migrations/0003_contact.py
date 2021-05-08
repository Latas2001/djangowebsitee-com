# Generated by Django 3.1.3 on 2021-03-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210319_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
