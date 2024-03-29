# Generated by Django 5.0 on 2024-01-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_client_user'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.RemoveField(
            model_name='client',
            name='numero_tlfn',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.RemoveField(
            model_name='client',
            name='username',
        ),
        migrations.AddField(
            model_name='client',
            name='first_name',
            field=models.CharField(default='', max_length=240),
        ),
        migrations.AddField(
            model_name='client',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='client',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='client',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='client',
            name='mobile',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
