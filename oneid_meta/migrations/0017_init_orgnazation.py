from django.db import migrations, models
from django.conf import settings


def init_orgnazation(apps, schema_editor):
    if not settings.TESTING:
        Group = apps.get_model('oneid_meta', 'Group')
        root = Group.objects.get(uid='root')

        intra = Group.objects.filter(uid='intra').first()
        if not intra:
            intra = Group.objects.create(uid='intra', name='内部联系人-角色', parent=root)

        extern = Group.objects.filter(uid='extern').first()
        if not extern:
            extern = Group.objects.create(uid='extern', name='外部联系人-标签', parent=root)



class Migration(migrations.Migration):
    '''
    init orgnazation
    :note: db only
    '''

    dependencies = [
        ('oneid_meta', '0016_redesign_perm'),
    ]

    operations = [
        migrations.RunPython(init_orgnazation),
    ]
