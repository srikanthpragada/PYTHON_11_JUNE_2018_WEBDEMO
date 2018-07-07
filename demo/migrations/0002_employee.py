# Generated by Django 2.0.5 on 2018-07-07 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('department', models.ForeignKey(on_delete='cascade', to='demo.Department')),
            ],
            options={
                'db_table': 'Employees',
            },
        ),
    ]