# Generated by Django 4.0.3 on 2022-04-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arzaizm_istorizm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_Arxaizm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('files', models.FileField(blank=True, upload_to='files')),
            ],
        ),
    ]
