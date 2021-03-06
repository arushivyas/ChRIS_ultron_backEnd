# Generated by Django 2.1.4 on 2020-04-24 05:54

from django.db import migrations, models
import uploadedfiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadedfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadedfile',
            options={'ordering': ('-fname',)},
        ),
        migrations.RemoveField(
            model_name='uploadedfile',
            name='upload_path',
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='fname',
            field=models.FileField(max_length=512, unique=True, upload_to=uploadedfiles.models.uploaded_file_path),
        ),
    ]
