# Generated manually for migration order fix

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('invoices', '0002_customuser_company_invoice_invoicedetail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(
                blank=True,
                help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                related_name='user_set',
                related_query_name='user',
                to='auth.group',
                verbose_name='groups'
            ),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(
                blank=True,
                help_text='Specific permissions for this user.',
                related_name='user_set',
                related_query_name='user',
                to='auth.permission',
                verbose_name='user permissions'
            ),
        ),
    ]
