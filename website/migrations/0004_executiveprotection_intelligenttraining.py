# Generated by Django 3.2.3 on 2021-08-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20210806_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executiveprotection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='img/%y')),
                ('img2', models.ImageField(default='default.jpg', upload_to='img/%y')),
            ],
            options={
                'verbose_name': 'Executiveprotection',
                'verbose_name_plural': 'Executiveprotection',
            },
        ),
        migrations.CreateModel(
            name='Intelligenttraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='img/%y')),
                ('img2', models.ImageField(default='default.jpg', upload_to='img/%y')),
            ],
            options={
                'verbose_name': 'Intelligenttraining',
                'verbose_name_plural': 'Intelligenttraining',
            },
        ),
    ]
