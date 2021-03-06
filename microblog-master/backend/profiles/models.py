from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from PIL import Image
import os

def get_path_upload_avatar(instance,file):
    """
    make path of uploaded file shorter and return it
    in following format: (media)/profile_pics/user_1/myphoto_2018-12-2.png
    """
    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split('.')[-1]
    head = file.split('.')[0]
    if len(head) >10:
        head = head[:10]
    file_name =  head + '_' + time + '.' + end_extention
    return os.path.join('profile_pics','user_{0},{1}').format(instance.user.id,file_name)

class Profile(models.Model):
    """Модель профиля пользователя"""
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    nike = models.CharField("НикНейм", max_length=100, null=True, blank=True)
    avatar = models.ImageField("Аватар", upload_to=get_path_upload_avatar, null=True, blank=True)
    follower = models.ManyToManyField(
                        User,
                        verbose_name="Фолловер",
                        related_name='followers'
                        )
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return "{}".format(self.user)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > 50 or img.width > 50:
                output_size = (50,50)
                img.thumbnail(output_size)
                img.save(self.avatar.path)
    @property
    def get_avatar_url(self):
        if self.avatar:
            return '/media/{}'.format(self.avatar)
        else:
            return '/static/img/default.png/'
    @property
    def get_followers(self):
        if self.follower:
            return self.follower.all()
        else:
            return 'no followers yet'

    # def get_absolute_url(self):
    #     return reverse("profile",kwargs={'pk':self.id})

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
