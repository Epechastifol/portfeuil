from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length= 200, verbose_name= 'Titre')
    content = models.TextField(verbose_name= "Contenu de l'article")
    image = models.ImageField(upload_to='articles/', blank= True, null= True, verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add= True, verbose_name= 'Date')

    def __str__(self):
        return f"{self.title} le {self.created_at}"

    class Meta:
        verbose_name = "Article publié"
        verbose_name_plural = "Articles publiés"
