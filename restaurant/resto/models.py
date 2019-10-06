from django.db import models
from configuration.models import Social
# Create your models here.

class Category(models.Model):
    nom =  models.CharField(max_length=255)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
        
    def __str__(self):
        return self.nom
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'


#dans cette classe on va lister tous les ingrediants du resto qu on
#utilisera pour affecter a chaque plat en fonction de la composition du plat

class Ingredient(models.Model):
    nom =  models.CharField(max_length=255)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
        
    def __str__(self):
        return self.nom
        
    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredient'
            
            
#le champ speciale concerne les plates speciale dont le resto veut faire la promo
#lle champ today s il est a true le plat sera afficher dans menu du jours
#status ici est utiliser pour dire si le plat sera afficher parmis les plats du resto ou non

class Plat(models.Model):
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="category_client")
    nom = models.CharField(max_length=160)
    prix = models.FloatField()
    ingredient = models.ManyToManyField(Ingredient,related_name="ingrediant_plat")
    image = models.ImageField(upload_to='restaurant/plat')
    speciale = models.BooleanField(default=False)
    today = models.BooleanField()
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
    def __str__(self):
        return self.nom

    class Meta:

        verbose_name = 'Plat'
        verbose_name_plural = 'Plats'
            
            

#cette classe concerne les postes de nos cuisinier ou chef 
class Poste(models.Model):
    nom = models.CharField(max_length=160)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
        
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Poste'
        verbose_name_plural = 'Postes'


class Personnel(models.Model):
    nom = models.CharField(max_length=160)
    prenom = models.CharField(max_length=160)
    photo = models.ImageField(upload_to='resto/personnel')
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE,related_name="poste_personnel")
    social = models.ManyToManyField(Social,related_name='social_personnel')
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
        
    def __str__(self):
        return self.nom+ " " + self.prenom

    class Meta:
        verbose_name = 'Personnel'
        verbose_name_plural = 'Personnels'


#cette classe va servir a dire si le visiteur veut reserver et qu il n ya pas de 
#de place disponible alors fais sa ou fais si.
#1place == 1personne
#le nbre de place s incremente en fonction du nombre de personne enregistrer
#dans la classe reservation

class Place(models.Model):
    """Model definition for Place."""

    nb_place_disponible = models.IntegerField()
    nb_place_total = models.IntegerField()
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    @property
    def nb_place_prise(self):
        return self.nb_place_total - nb_place_disponible
    class Meta:
        """Meta definition for Place."""

        verbose_name = 'Place'
        verbose_name_plural = 'Places'

