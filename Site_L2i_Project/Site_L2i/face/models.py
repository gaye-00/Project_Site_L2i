from django.db import models
import os
from django.core.exceptions import ValidationError
def est_une_extension_autorise(value):
    ext=os.path.splitext(value.name)[1]
    valid_extensions=['.pdf','.doc','.docx']
    if not ext in valid_extensions:
        raise ValidationError(u'Je ne veux pas de ce genre de fichier alors svp respecter les types(pdf,doc,docx)')


class cours(models.Model):
    titre=models.CharField(verbose_name="Titre du cours" ,null=False,max_length=50)    
    matiere=models.CharField(verbose_name="Domaine du cours" ,null=False,max_length=100)
    auteur=models.CharField(verbose_name="Auteur du cours" ,null=False,max_length=50)
    doc=models.FileField(null=True,blank=True,upload_to="pdf",validators=[est_une_extension_autorise])
    cover=models.ImageField(null=True,blank=False,upload_to="image/",default='image/default.jpg',verbose_name='Veuiller mettre une image pour embellir le cours')
    niveau=models.CharField(verbose_name="Niveau" ,null=False, max_length=50)
    desc=models.TextField(null=True)
    coef=models.IntegerField(null=True,verbose_name='Coeffcient de la matiere')
    # pub=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titre+''+self.matiere
    