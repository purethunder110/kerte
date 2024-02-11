from django.contrib.auth.models import BaseUserManager

class base_user_manager(BaseUserManager):

    def create_user(self,email,first_name,last_name,username,password,Age,profile_pic=None,disabled=None):
        if not email:
            raise ValueError('the email field is empty')
        if not password:
            raise ValueError("their is no password")
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,Age=Age,profile_pic=profile_pic,disabled=disabled)
        user.set_password(password)
        user.save(using=self._db)
        return user