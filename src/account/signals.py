
def create_admin(sender, *args, **kwargs):
    if sender.models['user'].objects.count() == 0:
        sender.models['user'].objects.create_superuser(
            username='admin', email='admin@123.sky', password='as')
        print('admin, as')
    else:
        pass
