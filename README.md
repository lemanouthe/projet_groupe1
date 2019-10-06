# projet_groupe1

Nous aurons 4 applications qui sont: configuration,~~statistique~~,contact et restaurant.

## pages a creer:
    contact.html

## configuration app


    
    #ce models nous contient les info sur le restaurant
    #text1 correspond a Fast Delivery dans le template dans le fichier index.html
    #text2 a Fresh Food dans le fichier index.html
    #texte3 a 24/7 Support dans le fichier index.html
    #text_accueil a We Love Delicious Foods!
# importation necessaire
```python
from django.utils.timezone import now
from datetime import datetime, date, time
import re
```
```python

    class Presentation(models.Model):
        """Model definition for Presentation."""

        nom = models.CharField(max_length=255)
        description = models.TextField()
        image = models.ImageField(upload_to='image_accueil', )
        text_accueil = models.TextField()
        lien_video = models.URLField(max_length=255)
        text1 = models.CharField(max_length=255)
        text2 = models.CharField(max_length=255)
        text3 = models.CharField(max_length=255)
        """
        a ajouter
        working_hour = models.ManyToManyField('WorkingHour',related_name='working_config')
        """
        license_site = models.CharField(max_length=255)
        active = models.BooleanField(default=False)
        date_add = models.DateTimeField(auto_now_add=True)
        date_udp =  models.DateTimeField(auto_now =True)
 """ A ajouter
        @property
        def open_hour(self):
            jour = now().strftime('%A')
            hour = ''
            for w in self.working_hour.all():
                if re.match(str(w.jour),str(jour),re.IGNORECASE):
                    hour = '{} - {}'.format(str(w.start_hour),str(w.end_hour))
            print(jour,' : ',hour)
            return '{} : {}'.format(jour,hour)
    """
        class Meta:
            """Meta definition for Presentation."""

            verbose_name = 'Presentation'
            verbose_name_plural = 'Presentations'

        def __str__(self):
            """Unicode representation of Presentation."""
            return self.nom


    #cette classe concerne tout ce qui est dans la partie about.html et qui se repete dans le home

    class About(models.Model):
        """Model definition for About."""

        nom = models.CharField(max_length=255)
        description = models.TextField()
        image = models.ImageField(upload_to='image_about', )
        active = models.BooleanField(default=False)
        date_add = models.DateTimeField(auto_now_add=True)
        date_udp =  models.DateTimeField(auto_now =True)

        class Meta:
            """Meta definition for About."""

            verbose_name = 'About'
            verbose_name_plural = 'Abouts'

        def __str__(self):
            """Unicode representation of About."""
            pass
    """
    model des reseau sociaux a jouter

    class Social(models.Model):
    # TODO: Define fields here
    choice=[('FB','facebook'),('TW','twitter'),('INS','instagram'),('GOO','google')]
    name = models.CharField(max_length=100,choices=choice)
    lien = models.URLField(max_length=200)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    @property
    def font(self):
        if self.name == 'FB':
            font = 'icon-facebook'
        elif self.name == 'TW':
            font ='icon-twitter'
        elif self.name == 'INS':
            font ='icon-instagram"'
        elif self.name == 'GOO':
            font ='icon-google-plus'
        return font
    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"

    def __str__(self):
        return '{}'.format(self.name)

    """

```
- [ ] class des horaires fausse tu ne peut pas geré sa comme sa c'est trois class pour faire les horaires
- [ ] besoin de creer le model jour 
- [ ] besoin de cree le model heure
- [ ] besoin de cree le model horaire
- [ ] model pour les reseau sociau
```python
    #cette classe concerne l horaire du resto dans le footer de la page
    class Horaire(models.Model):
        jours = models.CharField(max_length=50)
        heure = models.CharField(max_length=50)
        status = models.BooleanField(default=True)
        date_add = models.DateTimeField(auto_now_add=True)
        date_udp =  models.DateTimeField(auto_now =True)
        def __str__(self):
        return self.jours

        class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Horaire'
            verbose_name_plural = 'Horaires'
            
```

#### exemple des trois table
- notez la troisieme modification a ete faite dans le model presentation plus haut
```python
class Day(models.Model):
    # TODO: Define fields here
    jour = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Day"
        verbose_name_plural = "Days"

    def __str__(self):
        return '{}'.format(self.jour)

class WorkingHour(models.Model):
    # TODO: Define fields here
    jour = models.ForeignKey(Day,on_delete=models.CASCADE,related_name='day_working')
    start_hour = models.CharField(max_length=50)
    end_hour = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "WorkingHour"
        verbose_name_plural = "WorkingHours"

    def __str__(self):
        return '{}  {} - {}'.format(self.jour,self.start_hour,self.end_hour)

```

## contact app

   

#cette classe concerne la nouvelle page contact qui doit etre creer
#elle nous permettra de contacter le resto 
#si le message est lu dans la partie admin il coche simplement le champ status pour le mettre a true
#dans la partie la partie admin ce champ sera rendu editable. Cette pour facilité la lecture de message

```python
    class Message(models.Model):
        """Model definition for Message."""
        nom = models.CharField(max_length=250)
        sujet = models.CharField(max_length=250)
        email = models.EmailField()
        message = models.TextField()
        status = models.BooleanField(default=False)
        date_add = models.DateTimeField(auto_now_add=True)
        date_upd = models.DateTimeField(auto_now=True)


        # TODO: Define fields here

        class Meta:
            """Meta definition for Message."""

            verbose_name = 'Message'
            verbose_name_plural = 'Messages'
            

#cette classe est un systeme d abonnement au news du resto

    class Newsletter(models.Model):
        email = models.EmailField()
        status = models.BooleanField(default=True)
        date_add = models.DateTimeField(auto_now_add=True)
        date_upd = models.DateTimeField(auto_now=True)
        def __str__(self):
            return self.email

        class Meta:
            verbose_name = 'Newsletter'
            verbose_name_plural = 'Newsletters'
    
    
```

## restaurant app

```python
        
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
            return self.nom_poste

        class Meta:
            verbose_name = 'Poste'
            verbose_name_plural = 'Postes'


    class Cuisinier(models.Model):
        nom = models.CharField(max_length=160)
        prenom = models.CharField(max_length=160)
        photo = models.ImageField(upload_to='photo_cuisinier')
        poste = models.ForeignKey(Poste, on_delete=models.CASCADE,related_name="poste_cuisinier")
        """
        a ajouter social
        social = models.ManyToManyField('Social',related_name='social_chef')
        """
        date_add =  models.DateTimeField(auto_now_add=True)
        date_update =  models.DateTimeField(auto_now=True)
        status =  models.BooleanField(default=True)
        
        def __str__(self):
            return self.nom+ " " + self.prenom

        class Meta:
            verbose_name = 'Cuisinier'
            verbose_name_plural = 'Cuisiniers'


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
        """
        optionel a ajouter

        @property
        def nb_place_prise(self):
            return self.nb_place_total - nb_place_disponible
        """
        class Meta:
            """Meta definition for Place."""

            verbose_name = 'Place'
            verbose_name_plural = 'Places'



```
# application clientele
```python
    #cette classe concerne la reservation
    #quand on fait poste on doit trouver une fonctionnalite qui va dire si le nombrepersonne
    #est a ou b retirer ce nombre dans le nbre_place_disponible dans la classe place

    class Reservation(models.Model):
        nom = models.CharField(max_length=160)
        email = models.EmailField()
        numero = models.CharField(max_length=160)
        date = models.DateField()
        heure = models.TimeField()
        personne = models.IntegerField()
        date_add =  models.DateTimeField(auto_now_add=True)
        date_update =  models.DateTimeField(auto_now=True)
        status =  models.BooleanField(default=True)
        
        def __str__(self):
        return self.nom

        class Meta:
            verbose_name = 'Reservation'
            verbose_name_plural = 'Reservations'
            
    #ici le champs par defaut comme metier des temoins est client 

    class Temoignage(models.Model):
        nom = models.CharField(max_length=160)
        commentaire = models.TextField()
        image = models.ImageField(upload_to='client/testimonial')
        job = models.CharField(max_length=255)
        social = ManyToManyField(Social,related_name='social_testimonial')#cette ligne depend du model de testimonial choisie
        date_add =  models.DateTimeField(auto_now_add=True)
        date_update =  models.DateTimeField(auto_now=True)
        status =  models.BooleanField(default=True)
        
        def __str__(self):
            return self.nom

        class Meta:
            verbose_name = 'Temoignage'
            verbose_name_plural = 'Temoignages'
```

## ~~statistique app~~

```python
    class InfoUser(models.Model):
    """Model definition for InfoUser."""

    page_visiter = models.CharField(max_length=255)
    ip_adresse = models.IPAddressField()
    localisation = models.CharField(max_length=255)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)

    class Meta:
        """Meta definition for InfoUser."""

        verbose_name = 'InfoUser'
        verbose_name_plural = 'InfoUsers'

    def __str__(self):
        """Unicode representation of InfoUser."""
        pass

```