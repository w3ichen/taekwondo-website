# Generated by Django 3.1 on 2020-08-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=500)),
                ('url', models.URLField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='MainPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Home page photo', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(help_text='Link to register', max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.DecimalField(decimal_places=0, help_text='Order to display (0 is displayed first)', max_digits=2)),
                ('day', models.CharField(help_text='Weekday', max_length=15)),
                ('start', models.CharField(help_text='Start Time (Format: 00:00am)', max_length=7)),
                ('end', models.CharField(help_text='Start Time (Format: 00:00pm)', max_length=7)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='PracticeTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(help_text='Location of practices', max_length=500)),
                ('times', models.ManyToManyField(related_name='times', to='other.Time')),
            ],
        ),
    ]