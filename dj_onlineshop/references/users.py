from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name="Имя пользователя", 
        max_length=30,
        primary_key=True)
    avatar = models.ImageField(
        verbose_name="Аватар",
        upload_to = "profile/",
        null=True, 
        blank=True)
    first_name = models.CharField(
        verbose_name="Фамилия",
        max_length=30,
        null=True, 
        blank=True)
    last_name = models.CharField(
        verbose_name="Имя",
        max_length=30,
        null=True, 
        blank=True)    
    email = models.EmailField(
        max_length=100, 
        help_text='Enter a valid email addres')
    password1 = models.CharField(
        max_length=30)
    password2 = models.CharField(
        max_length=30)       
   
    def get_absolute_url(self):
        return reverse("user", kwargs={"pk": self.username.pk})
    

    def __str__(self):
        return f'{self.username}'

