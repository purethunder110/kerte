from django.contrib.auth.models import BaseUserManager

class base_user_manager(BaseUserManager):

    def create_user(self,email,first_name,last_name,username,password,Age,profile_pic=None,disabled=False,**extra_fields):
        if not email:
            raise ValueError('the email field is empty')
        if not password:
            raise ValueError("their is no password")
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,Age=Age,profile_pic=profile_pic,disabled=disabled,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,first_name,last_name,username,password,Age,profile_pic=None,disabled=False, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email,first_name,last_name,username,password,Age,profile_pic=None,disabled=disabled,**extra_fields)