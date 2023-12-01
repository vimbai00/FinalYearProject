# backends.py
from django.contrib.auth.backends import ModelBackend

class GroupRedirectBackend(ModelBackend):
    def get_user_group_redirect(self, user):
        if user.groups.filter(name='customer').exists():
            return '/customer-home/'  # Redirect customers to the customer-home page
        elif user.groups.filter(name='buyer').exists():
            return '/supply_chain_home/'  # Redirect buyers to the supply_chain_home page
        elif user.groups.filter(name='student').exists():
            return '/student-home/'  # Redirect students to the student-home page
        elif user.groups.filter(name='admin').exists():
            return '/admin-home/'  # Redirect admins to the admin-home page
        else:
            return '/'  # Default redirect for other users

    def get_user_redirect(self, user):
        if user.is_authenticated:
            return self.get_user_group_redirect(user)
        else:
            return '/login/'  # Redirect non-authenticated users to the login page
