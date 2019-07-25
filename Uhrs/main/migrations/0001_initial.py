# Generated by Django 2.1.3 on 2019-01-19 12:55

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('is_client', models.BooleanField(default=False)),
                ('is_hospo', models.BooleanField(default=False)),
                ('docto_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('name', models.CharField(default=0, max_length=50)),
                ('contact', models.CharField(default=0, max_length=50)),
                ('address', models.CharField(default=0, max_length=50)),
                ('city', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='city_clinic', to='main.City')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('name', models.CharField(default=0, max_length=50)),
                ('stype', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dentist', 'Dentist'), ('General_Physician', 'General Physician'), ('ENT_Specialist', 'ENT Specialist'), ('Obstetrics', 'Obstetrics')], max_length=100)),
                ('avalibility', models.BooleanField(default=True)),
                ('fees', models.CharField(default=0, max_length=50)),
                ('clinic', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Clinic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('reg_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(default=0, max_length=50)),
                ('fees', models.CharField(default=0, max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('doctor', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dentist', 'Dentist'), ('General_Physician', 'General Physician'), ('ENT_Specialist', 'ENT Specialist'), ('Obstetrics', 'Obstetrics')], max_length=100)),
                ('father_husband_name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('adhaar', models.CharField(max_length=12)),
                ('epic', models.CharField(max_length=20)),
                ('pin', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('city', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='city', to='main.City')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deleted at')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.State'),
        ),
    ]