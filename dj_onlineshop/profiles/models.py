from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name="Имя пользователя", 
        max_length=30,
        primary_key=True)
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
    group_user = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,)    
    country = models.CharField(
        verbose_name="Страна",
        max_length=30,
        null=True, 
        blank=True)
    city = models.CharField(
        verbose_name="Город",
        max_length=40,
        null=True, 
        blank=True)
    zip_code = models.PositiveSmallIntegerField(
        verbose_name="Индекс",
        null=True, 
        blank=True)
    address_first = models.CharField(
        verbose_name="Адрес1",
        max_length=100,
        null=True, 
        blank=True)
    address_second = models.CharField(
        verbose_name="Адрес2",
        max_length=100,
        null=True, 
        blank=True)
    info = models.TextField(
        verbose_name="Дополнительная информация",
        max_length=1000,
        null=True,
        blank=True)              

    def get_absolute_url(self):
        return reverse("user", kwargs={"pk": self.username.pk})
    

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиля'    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)

@receiver
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

