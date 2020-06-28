
def create_user(sender, **kwargs):
    print('*'*32)
    print(f"app_config.label: {sender.label}\nkwargs: {kwargs}\nsender: {sender}")
    print('*'*32)