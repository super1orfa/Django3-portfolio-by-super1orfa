from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    date_created = models.DateTimeField(
        auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ ها"
