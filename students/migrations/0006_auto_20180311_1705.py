# Generated by Django 2.0 on 2018-03-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20180310_1134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterField(
            model_name='course',
            name='no_of_students_enrolled',
            field=models.IntegerField(default=0),
        ),
    ]
