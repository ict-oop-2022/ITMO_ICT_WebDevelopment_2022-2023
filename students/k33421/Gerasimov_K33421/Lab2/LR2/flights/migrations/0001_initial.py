# Generated by Django 4.1.3 on 2022-12-04 16:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AviaCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Авиакомпания',
                'verbose_name_plural': 'Авиакомпании',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255, unique=True, verbose_name='Номер рейса')),
                ('from_city', models.CharField(max_length=255, verbose_name='Город отлета')),
                ('to_city', models.CharField(max_length=255, verbose_name='Город прилета')),
                ('departure_time', models.DateTimeField(verbose_name='Время отлета')),
                ('arrival_time', models.DateTimeField(verbose_name='Время прилета')),
                ('type', models.IntegerField(choices=[(0, 'Отлет'), (1, 'Прилет')], verbose_name='Отлет/прилет')),
                ('gate', models.CharField(max_length=255, verbose_name='Номер гейта')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='flights.aviacompany', verbose_name='Авиакомпания')),
            ],
            options={
                'verbose_name': 'Рейс',
                'verbose_name_plural': 'Рейсы',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество')),
                ('review_text', models.TextField(default='', verbose_name='Отзыв')),
                ('review_number', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='flights.flight', verbose_name='Рейс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирования',
            },
        ),
    ]
