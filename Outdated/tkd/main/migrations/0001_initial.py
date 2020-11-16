# Generated by Django 3.1 on 2020-08-23 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pinned', models.BooleanField(default=False, help_text='Pin Announcement')),
                ('title', models.CharField(max_length=500)),
                ('title_link', models.URLField(blank=True, help_text='(optional) Redirect URL for title', max_length=3000, null=True)),
                ('description', models.CharField(max_length=10000)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, help_text='(optional)', null=True, upload_to='announcement')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('location', models.CharField(max_length=500)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=500)),
                ('details', models.CharField(max_length=10000)),
                ('button_url', models.URLField(blank=True, help_text='(optional) URL to direct to', max_length=3000, null=True)),
                ('button_label', models.CharField(blank=True, help_text='(optional) Text on link button', max_length=100, null=True)),
            ],
            options={
                'ordering': ['start'],
            },
        ),
        migrations.CreateModel(
            name='Exec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('position', models.CharField(max_length=500)),
                ('detail', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(upload_to='profile')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=5000)),
                ('answer', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.URLField(max_length=3000)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('position', models.CharField(blank=True, max_length=500, null=True)),
                ('detail', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(upload_to='profile')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Photo', max_length=500)),
                ('date_taken', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='gallery')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
