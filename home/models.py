from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        abstract = True


class LeaveMessage(BaseModel):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField(region='CN')
    message = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.message[:50]}{'...' if len(self.message) > 50 else ''}"

    class Meta:
        ordering = ['-last_modified']
        verbose_name = "网站留言"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
