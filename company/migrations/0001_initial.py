# Generated by Django 4.1.7 on 2023-05-23 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('pretest', models.BooleanField()),
                ('posttest', models.BooleanField()),
                ('is_id_required', models.BooleanField(default=False)),
                ('grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1, null=True)),
                ('languages', models.ManyToManyField(blank=True, to='company.company')),
            ],
        ),
    ]
