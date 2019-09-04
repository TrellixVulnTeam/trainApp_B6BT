# Generated by Django 2.2.4 on 2019-09-04 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.DecimalField(decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='fullname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('activity', models.CharField(choices=[('S', 'Sedentary'), ('A', 'Active'), ('VA', 'Very active'), ('EA', 'Extremely active')], max_length=2, null=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='train.Profile')),
            ],
        ),
    ]