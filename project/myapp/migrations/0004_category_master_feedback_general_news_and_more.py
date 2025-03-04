# Generated by Django 4.0 on 2025-01-14 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_user_details_kcno'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('msg', models.CharField(max_length=250)),
                ('dt', models.CharField(max_length=15)),
                ('tm', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='general_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('subject', models.CharField(max_length=150)),
                ('news', models.CharField(max_length=1500)),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='location_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_name', models.CharField(max_length=150)),
                ('addr1', models.CharField(max_length=150)),
                ('addr2', models.CharField(max_length=150)),
                ('addr3', models.CharField(max_length=150)),
                ('pin', models.CharField(max_length=50)),
                ('lat', models.CharField(max_length=50)),
                ('lng', models.CharField(max_length=50)),
                ('radius', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='pic_pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_path', models.CharField(max_length=150)),
                ('category_master_id', models.IntegerField()),
                ('location_master_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user_search_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('pic_path', models.CharField(max_length=150)),
                ('result', models.CharField(max_length=150)),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
