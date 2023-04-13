# Generated by Django 3.2.16 on 2023-04-13 10:18

from django.db import migrations, models

from assets.const import AllTypes


def migrate_automation_push_account_params(apps, schema_editor):
    platform_automation_model = apps.get_model('assets', 'PlatformAutomation')
    platform_automation_methods = AllTypes.get_automation_methods()
    methods_id_data_map = {
        i['id']: None if i['params_serializer'] is None else i['params_serializer']({}).data
        for i in platform_automation_methods
        if i['method'] == 'push_account'
    }
    automation_objs = []
    for automation in platform_automation_model.objects.all():
        push_account_method = automation.push_account_method
        if not push_account_method:
            continue
        value = methods_id_data_map.get(push_account_method)
        if value is None:
            continue
        automation.push_account_params = value
        automation_objs.append(automation)
    platform_automation_model.objects.bulk_update(automation_objs, ['push_account_params'])


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0113_auto_20230411_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseautomation',
            name='params',
            field=models.JSONField(default=dict, verbose_name='Params'),
        ),
        migrations.AddField(
            model_name='platformautomation',
            name='change_secret_params',
            field=models.JSONField(default=dict, verbose_name='Change secret params'),
        ),
        migrations.AddField(
            model_name='platformautomation',
            name='gather_accounts_params',
            field=models.JSONField(default=dict, verbose_name='Gather facts params'),
        ),
        migrations.AddField(
            model_name='platformautomation',
            name='gather_facts_params',
            field=models.JSONField(default=dict, verbose_name='Gather facts params'),
        ),
        migrations.AddField(
            model_name='platformautomation',
            name='ping_params',
            field=models.JSONField(default=dict, verbose_name='Ping params'),
        ),
        migrations.AddField(
            model_name='platformautomation',
            name='push_account_params',
            field=models.JSONField(default=dict, verbose_name='Push account params'),
        ),
        migrations.AddField(
            model_name='platformautomation',
            name='verify_account_params',
            field=models.JSONField(default=dict, verbose_name='Verify account params'),
        ),
        migrations.RunPython(migrate_automation_push_account_params),
    ]
