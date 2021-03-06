# Generated by Django 2.1.4 on 2018-12-14 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_news', models.TextField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('url', models.TextField()),
                ('url_ya', models.TextField()),
                ('text', models.TextField()),
                ('text_html', models.TextField()),
                ('date', models.DateTimeField()),
                ('choice_index', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.ChoiceIndex')),
                ('choice_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.ChoiceType')),
            ],
        ),
    ]
