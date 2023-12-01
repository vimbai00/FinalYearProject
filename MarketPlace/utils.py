# utils.py
def is_customer(user):
    return user.groups.filter(name='customer').exists()
