from django.db import models
from django.contrib.auth.models import User

class InputItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_numbers = models.CharField(null=False, blank= False, max_length=200)
    input_timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-input_timestamp'] #so that newer instances would appear at the top

    def __str__(self):
        return self.input_numbers
