from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  # Store images in 'projects' folder
    url = models.URLField(blank=True)  # Link to live project
    date_completed = models.DateField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True) # Allow projects to have tags

    def get_slug(self):
        """Génère le slug à partir du titre."""
        return self.title.lower().replace(' ', '-')

    def save(self, *args, **kwargs):
        """Met à jour le slug avant de sauvegarder."""
        if not self.slug:
            self.slug = self.get_slug()
        super().save(*args, **kwargs)

    slug = models.SlugField(unique= True, blank= True)


    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
    db_table = 'projects'

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
    db_table = 'tags'


class ContactMessage(models.Model): 
    name = models.CharField(max_length=100, verbose_name="Nom") 
    email = models.EmailField(verbose_name="Email") 
    subject = models.CharField(max_length=200, verbose_name="Sujet") 
    message = models.TextField(verbose_name="Message") 
    is_read = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi") 
     
    class Meta: 
        verbose_name = "Message de contact" 
        verbose_name_plural = "Messages de contact" 
     
    def __str__(self): 
        return f"{self.name} - {self.subject}" 