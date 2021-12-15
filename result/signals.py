from django.db.models.signals import post_save
from django.dispatch import receiver
from result.models import Teacher

@receiver(post_save, sender=Teacher)
def updateMarks(sender, **kwargs):
    print('sender-kwargs\t', '-'*50, **kwargs)

    
