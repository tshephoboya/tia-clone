# Generated by Django 3.0.6 on 2020-05-17 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.CharField(choices=[('Yes', 'yes'), ('No', 'no')], max_length=3)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogapp.Article')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]