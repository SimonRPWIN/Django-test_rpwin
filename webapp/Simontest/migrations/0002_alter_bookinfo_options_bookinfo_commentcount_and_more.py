# Generated by Django 4.1.6 on 2023-02-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simontest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': '书籍管理'},
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='commentcount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='pub_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='readcount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], default=1),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterModelTable(
            name='bookinfo',
            table='bookinfo',
        ),
    ]
