# Generated by Django 3.0.3 on 2020-03-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pages')),
                ('text', models.TextField(max_length=3000)),
                ('human1_text', models.TextField(max_length=3000)),
                ('human1_image', models.ImageField(upload_to='pages')),
                ('human2_text', models.TextField(max_length=3000)),
                ('human2_image', models.ImageField(upload_to='pages')),
                ('dog1_text', models.TextField(max_length=3000)),
                ('dog1_image', models.ImageField(upload_to='pages')),
                ('dog2_text', models.TextField(max_length=3000)),
                ('dog2_image', models.ImageField(upload_to='pages')),
                ('dog3_text', models.TextField(max_length=3000)),
                ('dog3_image', models.ImageField(upload_to='pages')),
            ],
        ),
    ]
