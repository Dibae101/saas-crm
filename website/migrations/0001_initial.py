# Generated by Django 3.2.3 on 2021-06-28 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armedsecurity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='img/%y')),
                ('img2', models.ImageField(default='default.jpg', upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Commercialsecurity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='img/%y')),
                ('img2', models.ImageField(default='default.jpg', upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Contractsecurity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='img/%y')),
                ('img2', models.ImageField(default='default.jpg', upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Crossingguards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='img/%y')),
                ('img2', models.ImageField(default='default.jpg', upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Homesecuritysystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='img/%y')),
                ('img2', models.ImageField(default='default.jpg', upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Multifamilysolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='img/%y')),
                ('img2', models.ImageField(default='default.jpg', upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Professionalsecurity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='img/%y')),
                ('img2', models.ImageField(default='default.jpg', upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Securityforrenters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='img/%y')),
                ('img2', models.ImageField(default='default.jpg', upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Securitymonitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='img/%y')),
                ('img2', models.ImageField(default='default.jpg', upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='default.jpg', upload_to='img/teams/%y')),
                ('img2', models.ImageField(default='default.jpg', upload_to='img/teams/%y')),
                ('img3', models.ImageField(default='default.jpg', upload_to='img/teams/%y')),
                ('img4', models.ImageField(default='default.jpg', upload_to='img/teams/%y')),
            ],
        ),
    ]
