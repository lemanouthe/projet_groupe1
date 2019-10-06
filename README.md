# projet_groupe1

Nous aurons 6 applications qui sont: configuration,statistique,contact,menu,reservation,team.
## pages a creer:
    contact.html

## configuration app

    
        
        #ce models nous contient les info sur le restaurant
        #text1 correspond a Fast Delivery dans le template dans le fichier index.html
        #text2 a Fresh Food dans le fichier index.html
        #texte3 a 24/7 Support dans le fichier index.html
        #text_accueil a We Love Delicious Foods!
        ```
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
            license_site = models.CharField(max_length=255)
            active = models.BooleanField(default=False)
            date_add = models.DateTimeField(auto_now_add=True)
            date_udp =  models.DateTimeField(auto_now =True)

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


        #cette classe concerne l horaire du resto dans le footer de la page

        class Horaire(models.Model):
            jours = models.CharField(max_length=50)
            heure_start = models.CharField(max_length=255)
            heure_fin = models.CharField(max_length=255)
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

        class Icon(models.Model):
            """Model definition for Icon."""

            nom = models.CharField(max_length=255)
            date_add =  models.DateTimeField(auto_now_add=True)
            date_update =  models.DateTimeField(auto_now=True)
            status =  models.BooleanField(default=True)

            class Meta:
                """Meta definition for Icon."""

                verbose_name = 'Icon'
                verbose_name_plural = 'Icons'

            def __str__(self):
                """Unicode representation of Icon."""
                return self.nom
        
        class Temoignage(models.Model):
            nom_temoin = models.CharField(max_length=160)
            commentaire = models.TextField()
            image = models.ImageField(upload_to='image_temoin', )
            job_temoin = models.CharField(max_length=160)
            date_add =  models.DateTimeField(auto_now_add=True)
            date_update =  models.DateTimeField(auto_now=True)
            status =  models.BooleanField(default=True)
            
            def __str__(self):
                return self.nom

            class Meta:
                verbose_name = 'Temoignage'
                verbose_name_plural = 'Temoignages'
    
        class ReserveConfiguration(models.Model):
            """Model definition for ReserveConfiguration."""

            titre_formulaire = models.CharField(max_length=255)
            sous_titre_formulaire = models.CharField(max_length=255)
            image = models.ImageField(upload_to='resrvation_back')
            active = models.BooleanField(default=False)
            date_add = models.DateTimeField(auto_now_add=True)
            date_udp =  models.DateTimeField(auto_now =True)

            
            # TODO: Define fields here

            class Meta:
                """Meta definition for ReserveConfiguration."""

                verbose_name = 'ReserveConfiguration'
                verbose_name_plural = 'ReserveConfigurations'

        ```



## contact app

   

    #cette classe concerne la nouvelle page contact qui doit etre creer
    #elle nous permettra de contacter le resto 
    #si le message est lu dans la partie admin il coche simplement le champ status pour le mettre a true
    #dans la partie la partie admin ce champ sera rendu editable. Cette pour facilité la lecture de message

        ```
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
            description = models.CharField(max_length=255)
            status = models.BooleanField(default=True)
            date_add = models.DateTimeField(auto_now_add=True)
            date_upd = models.DateTimeField(auto_now=True)
            def __str__(self):
                return self.email

            class Meta:
                verbose_name = 'Newsletter'
                verbose_name_plural = 'Newsletters'
        
        
        ```

## menu app

        ```
            
        class Category(models.Model):
            nom_categorie =  models.CharField(max_length=255)
            date_add =  models.DateTimeField(auto_now_add=True)
            date_update =  models.DateTimeField(auto_now=True)
            status =  models.BooleanField(default=True)
            
            def __str__(self):
            return self.nom_categorie

            class Meta:
                verbose_name = 'Category'
                verbose_name_plural = 'Categorys'


        #dans cette classe on va lister tous les ingrediants du resto qu on
        #utilisera pour affecter a chaque plat en fonction de la composition du plat

        class Ingrediant(models.Model):
            nom_ingrediant =  models.CharField(max_length=255)
            date_add =  models.DateTimeField(auto_now_add=True)
            date_update =  models.DateTimeField(auto_now=True)
            status =  models.BooleanField(default=True)
            
            def __str__(self):
                return self.nom_ingrediant
            
            class Meta:
                verbose_name = 'Ingrediant'
                verbose_name_plural = 'Ingrediant'
                
                
        #le champ speciale concerne les plates speciale dont le resto veut faire la promo
        #lle champ today s il est a true le plat sera afficher dans menu du jours
        #status ici est utiliser pour dire si le plat sera afficher parmis les plats du resto ou non

        class Plat(models.Model):
            categorie_id = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="category_client")
            nom = models.CharField(max_length=160)
            prix = models.FloatField()
            ingrediant = models.ManyToManyField(Ingrediant,related_name="ingrediant_plat")
            image = models.ImageField(upload_to='image_plat')
            speciale = models.BooleanField()
            today = models.BooleanField()
            date_add =  models.DateTimeField(auto_now_add=True)
            date_update =  models.DateTimeField(auto_now=True)
            status =  models.BooleanField(default=True)
            def __str__(self):
                return self.nom

            class Meta:

                verbose_name = 'Plat'
                verbose_name_plural = 'Plats'
                
                
 

        
        ```

## statistique app

    ```
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

## team app

        ```
    #cette classe concerne les postes de nos cuisinier ou chef 
        class Poste(models.Model):
            nom_poste = models.CharField(max_length=160)
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
            date_add =  models.DateTimeField(auto_now_add=True)
            date_update =  models.DateTimeField(auto_now=True)
            status =  models.BooleanField(default=True)
            
            def __str__(self):
                return self.nom+ " " + self.prenom

            class Meta:
                verbose_name = 'Cuisinier'
                verbose_name_plural = 'Cuisiniers'
        ```
    
## reseration app
    
        ```
        #cette classe va servir a dire si le visiteur veut reserver et qu il n ya pas de 
        #de place disponible alors fais sa ou fais si.
        #1place == 1personne
        #le nbre de place s incremente en fonction du nombre de personne enregistrer
        #dans la classe reservation

        class Place(models.Model):
            """Model definition for Place."""

            nbre_place_disponible = models.IntegerField()
            nbre_place_total = models.IntegerField()
            date_add =  models.DateTimeField(auto_now_add=True)
            date_update =  models.DateTimeField(auto_now=True)

            class Meta:
                """Meta definition for Place."""

                verbose_name = 'Place'
                verbose_name_plural = 'Places'




        #cette classe concerne la reservation
        #quand on fait poste on doit trouver une fonctionnalite qui va dire si le nombrepersonne
        #est a ou b retirer ce nombre dans le nbre_place_disponible dans la classe place

        class Reservation(models.Model):
            nom = models.CharField(max_length=160)
            email = models.EmailField()
            numero = models.CharField(max_length=160)
            date = models.DateField()
            heure = models.TimeField()
            nombrepersonne = models.IntegerField()
            date_add =  models.DateTimeField(auto_now_add=True)
            date_update =  models.DateTimeField(auto_now=True)
            status =  models.BooleanField(default=True)
            
            def __str__(self):
            return self.nom

            class Meta:
                verbose_name = 'Reservation'
                verbose_name_plural = 'Reservations'
        ```