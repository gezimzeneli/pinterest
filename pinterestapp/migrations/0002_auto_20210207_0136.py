# Generated by Django 2.1 on 2021-02-07 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterestapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('imageID', models.IntegerField()),
                ('userID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_who_followes', models.IntegerField()),
                ('user_who_gets_followed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(default='', max_length=2083)),
                ('title', models.CharField(default='', max_length=255)),
                ('origin_url', models.CharField(default='', max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='ImageBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField()),
                ('title', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageID', models.IntegerField()),
                ('userID', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='familyname',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='image_url',
            field=models.CharField(default='', max_length=2083),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
    ]
