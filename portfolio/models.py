from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.CharField(max_length=250, verbose_name='توضیح کوتاه')
    image = models.ImageField(
        upload_to='portfolio/images', verbose_name='عکس')
    url = models.URLField(blank=True, null=True, verbose_name="یو آر ال")

    def __str__(self):
        return self.title
    
    class Meta : 
        verbose_name = "پروژه"
        verbose_name_plural = "مدیریت پروژه ها"