from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """
    Create custom manager
    """

    def _create_user(self, email, first_name, password, **extra_fields):
        """
        Create and save a user
        """

        if not first_name:
            raise ValueError('First name is required')

        if not email:
            raise ValueError('Email is required')


        user = self.model(first_name=first_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile_number, email, first_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_superuser(self, email, first_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, first_name, password, **extra_fields)
