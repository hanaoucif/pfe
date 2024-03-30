from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# from django.db.models.signals import post_save


type_commission = (('1', 'CE'),('2', 'CPREG'),	)

poste_agent = (('1', 'President Directeur Générale'),
                    ('2', 'Directeur Générale'),
                    ('3', 'Assistant'),
                    ('4', 'Consultant')                                        
                    ,('7',  'Chef Stucture')
                    ,('8',  'Admin Projets') 
                    ,('9',  'Ingénieur D Etudes')
                    ,('10', 'Chargé D Etudes ')
                    ,('11', 'Exploitant ')
                    ,('12', 'Exécutant ')
                    ,('13', 'Chef Projet') 
                    ,('14', 'Chef Partie')
                    )
                                        
class specialite (models.Model):
    id   = models.AutoField(primary_key=True)
    lib  = models.CharField(max_length=30 ,verbose_name=u"Nom :")
   
    def __str__(self):
        return (self.lib )
    class Meta:
        verbose_name = "Spécialité" 
        verbose_name_plural = "Spécialité"                    
                    
class Commission (models.Model):
    id   = models.AutoField(primary_key=True)
    detail  = models.TextField(verbose_name=u"detail ")
    date=models.DateTimeField(verbose_name=u"DATE/Heure",null=True, blank=True)
    type = models.CharField(max_length=5,choices=type_commission ,verbose_name=u"Type",default='1', blank=True)
    projet= models.ForeignKey("Projet",null=True, blank=True,verbose_name=u"Projet",on_delete=models.CASCADE)
    partie= models.ForeignKey("Tache",null=True, blank=True,verbose_name=u"Partie Projet",on_delete=models.CASCADE)	
    def __str__(self):
        return str(self.type)
    class Meta:
        verbose_name = "Commission" 
        verbose_name_plural = "Commission"
        
    def clean(self):
        from django.core.exceptions import ValidationError        
       
        if (self.partie) and( self.projet):
            if(self.projet!= self.partie.projet):
                raise ValidationError('la partie et le projet ne correspondent pas')    
              
        
    def save(self, *args, **kwargs):
        if(self.partie and not self.projet):
             self.projet=self.partie.projet
        super(Commission, self).save(*args, **kwargs)    
        
class constructeur (models.Model):
    id   = models.AutoField(primary_key=True)
    lib  = models.CharField(max_length=30 ,verbose_name=u"Lib :")
   
    def __str__(self):
        return (self.lib )
    class Meta:
        verbose_name = "Contractant" 
        verbose_name_plural = "Contractants"
        
class marche (models.Model):
    id   = models.AutoField(primary_key=True)
    lib  = models.CharField(max_length=30 ,verbose_name=u"Num Marché:")
    details   = models.TextField(verbose_name=u"Details:")    
    def __str__(self):
        return (self.lib ) 
            
class mouvrage (models.Model):
    id_mo    = models.AutoField(primary_key=True)
    lib_mo   = models.CharField(max_length=30 ,verbose_name=u"Maitre ouvrage:")
    details   = models.TextField(verbose_name=u"Details:")    
    def __str__(self):
        return (self.lib_mo ) 
    class Meta:
        verbose_name = "Maitre ouvrage" 
        verbose_name_plural = "Maitre ouvrages"        
                      
class etat_emploiye (models.Model):
    id_etat    = models.AutoField(primary_key=True)
    lib_etat   = models.CharField(max_length=30 ,verbose_name=u"Etat employé:")				 
    def __str__(self):
        return (self.lib_etat )
    class Meta:
        verbose_name = "Etat employé" 
        verbose_name_plural = "Etat employé"    
               
class etat_projet (models.Model):
    id_etat    = models.AutoField(primary_key=True)
    lib_etat   = models.CharField(max_length=30 ,verbose_name=u"Etat projet:")				 
    def __str__(self):
        return (self.lib_etat ) 
    class Meta:
        verbose_name = "Etat projet" 
        verbose_name_plural = "Etat projet"    
        
class Direction (models.Model):
    id_dir    = models.AutoField(primary_key=True)
    lib_dir   = models.CharField(max_length=30 ,verbose_name=u"Lib")
    structure_per=models.ForeignKey('Direction',verbose_name=u"Structure parente",on_delete=models.CASCADE,null=True, blank=True)  
    reponsable=models.ForeignKey('Agent',verbose_name=u"Responsable",on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.lib_dir )
        
    class Meta:
        verbose_name = "Structure" 
        verbose_name_plural = "Structures"  

        
lestype = (
     ('1', 'Matériel de Transport'),
     ('2', 'Matériel pour le Diagnostic'),
     ('3', 'Matériel pour le Mesure'),
     ('4', 'Matériel de Nettoyage'), 
     ('5', 'Matériel pour gros oeuvre'),
     ('6', 'Matériel pour second oeuvre'),
     ('7', 'Matériel pour Espace verts'),
     ('8', 'Matériel pour Industrie'),   
     ('9', 'Matériel de Manutention'),
     ('10','Matériel de Signalisation'),
     ('11','Matériel portatif'),
     ('12','Engins de Terrasement'),
     ('13','Machines à Projete'),
     ('14','Electricité sur chantiers'),
     ('15','Autre'),
     
     ) 
lesdispo = (
        ('1', 'Disponible'),
        ('2', 'En Panne'),
        ('3', 'Louer'),
     )
lesetat = (
        ('1', 'Bonne Etat '),
        ('2', 'Endomagé'),
        ('3', 'En Panne'),
     )
lesetat_traitement = (
        ('1', 'En Cour'),
        ('2', 'Cloturé'),
        ('3', 'Probleme'),
        ('4', 'Annulé'),
     ) 
titre = (
        ('1', 'Chef Projet'),
        ('2', 'Ingénieur études'),
        ('3', 'Chargé études'),
        ('4', 'Annulé'),
     )       

 
class Type_doc (models.Model):
    id    = models.AutoField(primary_key=True)
    lib   = models.CharField(max_length=50,verbose_name=u"lib")	   
    def __str__(self):
        return str(self.lib ) 
        
    class Meta:
        verbose_name = "Table Gestion des doc" 
        verbose_name_plural = "Table Gestion des doc"    
 
class Ressource (models.Model):
    id_Ress    = models.AutoField(primary_key=True)
    type= models.CharField(max_length=2 ,choices=lestype ,verbose_name=u"TYPE")
    lib= models.CharField(max_length=25,verbose_name=u"Nom")	
    nom= models.CharField(max_length=25,verbose_name=u"MARQUE / MODEL")	
    code= models.CharField(max_length=25,verbose_name=u"CODE BARRES / MATRICUL")
    dispo= models.CharField(max_length=1 ,choices=lesdispo ,verbose_name=u"DISPONIBILITE")
    etat= models.CharField(max_length=1 ,choices=lesetat ,verbose_name=u"ETAT")
    def __str__(self):
        return (self.lib ) +"|" + unicode(self.nom )

class Agent(models.Model):
     Id_agent= models.AutoField(primary_key=True)
     login=models.OneToOneField(User,on_delete=models.CASCADE)
     Nom_agent= models.CharField(max_length=25,verbose_name=u"Nom employé",null=True, blank=True)
     Poste= models.CharField(max_length=3,choices=poste_agent,verbose_name=u"Titre",null=True, blank=True)
     specia=models.ForeignKey(specialite,verbose_name=u"Specialite",on_delete=models.CASCADE,null=True, blank=True)
     Mat_agent= models.CharField(max_length=10,verbose_name=u"MAT",null=True, blank=True)  
     Bureau= models.CharField(max_length=10,verbose_name=u"Bureau",null=True, blank=True) 
     Direction= models.ForeignKey(Direction,null=True, blank=True,verbose_name=u"Structure",on_delete=models.CASCADE)	
     etatag=models.ForeignKey(etat_emploiye,verbose_name=u"Etat employé",on_delete=models.CASCADE)                   
     tel= models.CharField(max_length=25,verbose_name=u"Tel")
     def __str__(self):
        return (self.Nom_agent)
     class Meta:
        verbose_name = "Employé" 
        verbose_name_plural = "Employés"
                        
class Projet(models.Model):
     id_projet= models.AutoField(primary_key=True)
     Lib= models.CharField(max_length=50,verbose_name=u"PROJET")
     ismaquette= models.ForeignKey("self",null=True, blank=True,related_name="maquetteProjet",verbose_name=u"Modele",on_delete=models.CASCADE)
     details= models.TextField(verbose_name=u"DETAILS")
     Chef_PROJET= models.ForeignKey(Agent,verbose_name=u"CHEF PROJET",null=True, blank=True,on_delete=models.CASCADE)
     maitreouvrage= models.ForeignKey(mouvrage,verbose_name=u"MAITRE OUVRAGE",null=True, blank=True,on_delete=models.CASCADE)
     #direction= models.ForeignKey(Direction)
     #progress=models.FloatField(Float_places=2,max_digits=4,verbose_name=u"PROGRESSION (%)")
     date_deb=models.DateField(verbose_name=u"DATE Debut Contractuele",null=True, blank=True)
     date_fin=models.DateField(verbose_name=u"DATE Mise en vigueur",null=True, blank=True)
     etat=models.ForeignKey(etat_projet,verbose_name=u"ETAT DU PROJET",on_delete=models.CASCADE)
     chart=models.BooleanField(verbose_name=u"Afficher sur Dashbord",default=True)
     archiv=models.BooleanField(verbose_name=u"ARCHIVE",default=True)
     maquette= models.BooleanField(verbose_name=u"C'est un projet modele")
     def __str__(self):
        return (self.Lib)
        
     @property
     def progression(self):
         v=0
         for x in self.tache_set.all() :
             try:         
                 v=v+((x.progress* x.pourcentage)/100)
             except:
                 pass             
         return v     
        		
class tache_Ressource (models.Model):
    id_pr    = models.AutoField(primary_key=True)
    Projet= models.ForeignKey('Tache',on_delete=models.CASCADE)
    Ressource= models.ForeignKey(Ressource,on_delete=models.CASCADE)
    date_deb=models.DateField(verbose_name=u"Date Debut",null=True, blank=True)
    date_fin=models.DateField(verbose_name=u"Date Fin",null=True, blank=True)
    def __str__(self):
        return (self.Projet )+ "  -  " +unicode(self.Ressource )

class tache_Agent (models.Model):
    id_pa    = models.AutoField(primary_key=True)
    tache= models.ForeignKey('Tache',verbose_name=u"Tache/Projet",on_delete=models.CASCADE,null=True, blank=True)
    Projet= models.ForeignKey('Projet',verbose_name=u"Tache/Projet",on_delete=models.CASCADE,null=True, blank=True)
    Agent= models.ForeignKey(Agent,on_delete=models.CASCADE)
    post= models.CharField(max_length=2,choices=poste_agent ,verbose_name=u"Role",null=True, blank=True)
    date_deb=models.DateField(verbose_name=u"Date Debut",null=True, blank=True)
    date_fin=models.DateField(verbose_name=u"Date Fin",null=True, blank=True)
    
    def __str__(self):
        return str(self.Projet) + "  -  " + str(self.Agent)
        
    class Meta:
        verbose_name = "Affectation" 
        verbose_name_plural = "Affectations"    
        				
class Tache(models.Model):
     id_tache= models.AutoField(primary_key=True)
     Lib= models.CharField(max_length=50,verbose_name=u"Titre")
     Chef_PROJET= models.ForeignKey(Agent,verbose_name=u"Responsable",null=True, blank=True,on_delete=models.CASCADE)
     tache= models.ForeignKey("self",null=True, blank=True,related_name="Tacheper",verbose_name=u"Partie Reference",on_delete=models.CASCADE)   
     projet= models.ForeignKey(Projet,null=True, blank=True,on_delete=models.CASCADE)
     delais=models.IntegerField(verbose_name=u"Durée (Semaine)",null=True, blank=True)
     date_deb_tot=models.DateField(verbose_name=u"Date Debut au plus tot",null=True, blank=True)
     date_deb_tard=models.DateField(verbose_name=u"Date Debut au plus tard",null=True, blank=True)
     date_deb=models.DateField(verbose_name=u"Date Debut réel",null=True, blank=True)
     date_fin=models.DateField(verbose_name=u"Date Fin",null=True, blank=True)
     pourcentage=models.FloatField(default=0,verbose_name=u"Pourcentage du projet (%)")
     progress=models.FloatField(default=0,verbose_name=u"PROGRESSION (%) ")
     Tache_presedent = models.ManyToManyField("self",null=True, blank=True)
     Listtache = models.TextField(null=True, blank=True)
     def __str__(self):
        return (self.Lib)

     class Meta:
        verbose_name = "Partie" 
        verbose_name_plural = "Parties"
        
     def clean(self):
        from django.core.exceptions import ValidationError        
       
        if (self.projet is None) and( self.tache is None):
            raise ValidationError('Veuillez choisir le projet ou bien la tache réference')    
        
     def save(self, *args, **kwargs):
        #jsonDec = json.decoder.JSONDecoder() 
        if(self.tache and not self.pk):
            
            if(self.tache.Listtache):
                
                 #ll=jsonDec.decode(self.tache.Listtache)
                 #ll.insert(0,self.tache.pk)                     
                 #self.Listtache = json.dumps(ll)
                 self.Listtache =str(self.tache.Listtache)+str(self.tache.pk)+"-"
                 
                 
            else:
                 #self.Listtache = json.dumps([self.tache.pk])
                 self.Listtache ="-"+str(self.tache.pk)+"-"
                 
        super(Tache, self).save(*args, **kwargs)
        
class Document(models.Model):
     id_attache= models.AutoField(primary_key=True)
     date      = models.DateTimeField(verbose_name=u"Date arrivé",null=True, blank=True)
     titre   = models.CharField(max_length=20,verbose_name=u"Objet")
     type= models.ForeignKey(Type_doc,on_delete=models.CASCADE)
     doc     = models.FileField(upload_to='MyUpload/projets',verbose_name=u"Fichier",null=True, blank=True)
     rapport     = models.TextField(verbose_name=u"Detail")
     projet= models.ForeignKey(Projet,on_delete=models.CASCADE)
     Tache= models.ForeignKey(Tache,verbose_name=u"Partie",null=True, blank=True,on_delete=models.CASCADE)
     
     def file_link(self):
        if self.doc :
            return "<a  href='%s'>'%s'</a>" % (self.doc.url,self.doc.name[9:])
        else:
            return "No attachment"
     file_link.allow_tags = True     # c nesecaire pour quil marche    
     def __str__(self):
        return (self.titre)	

     class Meta:
        verbose_name = "Document" 
        verbose_name_plural = "Documents"
        
     def clean(self):
        from django.core.exceptions import ValidationError        
       
        if (self.Tache) and( self.projet):
            if(self.projet!= self.Tache.projet):
                raise ValidationError('la partie et le projet ne correspondent pas')    
              
        
     def save(self, *args, **kwargs):
        if(self.Tache and not self.projet):
             self.projet=self.Tache.projet
        super(Document, self).save(*args, **kwargs)     
                                        
class incident (models.Model):
    id               = models.AutoField(primary_key=True)
    date             = models.DateTimeField(verbose_name=u"Date")
    detail           = models.TextField()
    projet           = models.ForeignKey(Projet,on_delete=models.CASCADE,null=True, blank=True)
    Tache            = models.ForeignKey(Tache,null=True, blank=True,on_delete=models.SET_NULL) 
    agent_decl       = models.ForeignKey(Agent,verbose_name=u"Agent Déclencheur",null=True, blank=True,on_delete=models.SET_NULL)
    def __str__(self):
        return (self.id )
        
    def clean(self):
        from django.core.exceptions import ValidationError        
       
        if (self.Tache) and( self.projet):
            if(self.projet!= self.Tache.projet):
                raise ValidationError('la partie et le projet ne correspondent pas')    
              
        
    def save(self, *args, **kwargs):
        if(self.Tache and not self.projet):
             self.projet=self.Tache.projet
        super(incident, self).save(*args, **kwargs)

class traitement (models.Model):
    id               = models.AutoField(primary_key=True)
    date             = models.DateTimeField(verbose_name=u"Date",auto_now_add=True)
    Echiance         = models.DateTimeField(verbose_name=u"Echiance",null=True, blank=True)
    procedu          = models.ForeignKey('procedure',verbose_name=u"procedure",on_delete=models.CASCADE,null=True, blank=True)
    detail           = models.TextField() 
    doc              = models.FileField(upload_to='MyUpload/traitement',verbose_name=u"Pice joint",null=True, blank=True)         
    demandeur        = models.ForeignKey(Agent,related_name="agent_demandeur",verbose_name=u"Demandeur",on_delete=models.CASCADE)
    executant        = models.ForeignKey(Agent,verbose_name=u"executant",on_delete=models.CASCADE)
    projet           = models.ForeignKey(Projet,on_delete=models.CASCADE,null=True, blank=True)
    Tache            = models.ForeignKey(Tache,null=True, blank=True,on_delete=models.SET_NULL) 
    etat             = models.CharField(max_length=1 ,choices=lesetat_traitement ,verbose_name=u"ETAT")
    
    def __str__(self):
        return str(self.id )  
    class Meta:
        verbose_name = "Travail" 
        verbose_name_plural = "Travaux"
        
    def clean(self):
        from django.core.exceptions import ValidationError        
       
        if (self.Tache) and( self.projet):
            if(self.projet!= self.Tache.projet):
                raise ValidationError('la partie et le projet ne correspondent pas')    
              
        
    def save(self, *args, **kwargs):
        if(self.Tache and not self.projet):
             self.projet=self.Tache.projet
        super(traitement, self).save(*args, **kwargs)    
                               
class suiv_traitement (models.Model):
    id               = models.AutoField(primary_key=True)
    acteur        = models.ForeignKey(Agent,verbose_name=u"Auteur",on_delete=models.CASCADE,null=True, blank=True)
    traitement          = models.ForeignKey('traitement',verbose_name=u"procedure",on_delete=models.CASCADE,null=True, blank=True)    
    date             = models.DateTimeField(verbose_name=u"Date",auto_now_add=True)      
    detail           = models.TextField() 
    doc              = models.FileField(upload_to='MyUpload/traitement',verbose_name=u"Pice joint",null=True, blank=True)         
       
    def __str__(self):
        return str(self.id )  
    class Meta:
        verbose_name = "Reponse Travail" 
        verbose_name_plural = "Reponse Travaux" 
                      
class procedure (models.Model):
    id               = models.AutoField(primary_key=True)
    titre            = models.CharField(max_length=1, verbose_name=u"Titre")   
    detail           = models.TextField(verbose_name=u"Detail") 
    
    def __str__(self):
        return (self.id )  
    class Meta:
        verbose_name = "Procedure" 
        verbose_name_plural = "Procedure"
         
class suivi_notification (models.Model):
    id               = models.AutoField(primary_key=True)
    date             = models.DateTimeField(verbose_name=u"Date",auto_now_add=True)
    detail           = models.TextField()   
    incident           = models.ForeignKey("notification",on_delete=models.CASCADE,null=True, blank=True)
    agent       = models.ForeignKey(Agent,null=True, blank=True,on_delete=models.SET_NULL)
    def __str__(self):
        return (self.id )        
                
class date_document (models.Model):
    id_po     = models.AutoField(primary_key=True)
    date      = models.DateTimeField(verbose_name=u"Date",auto_now_add=True)
    lib       =models.CharField(max_length=40)
    Document  = models.ForeignKey(Document,on_delete=models.CASCADE)
    def __str__(self):
        return (self.lib)        
        
class sig_document (models.Model):
    id     = models.AutoField(primary_key=True)
    signatair=models.ForeignKey(Agent,verbose_name=u"signatair",on_delete=models.CASCADE) 
    Document  = models.ForeignKey(Document,on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return (self.id)   

class act_document (models.Model):
    id         = models.AutoField(primary_key=True)
    traitement = models.ForeignKey(traitement,verbose_name=u"traitement a faire",on_delete=models.CASCADE) 
    Document   = models.ForeignKey(Document,on_delete=models.CASCADE,null=True, blank=True)
    
    
    def __str__(self):
        return (self.id)        
                               
class pointage (models.Model):
    id_po     = models.AutoField(primary_key=True)
    date_po   =models.DateTimeField(verbose_name=u"Date",auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    latitude= models.FloatField(verbose_name=u"latitude",null=True, blank=True)
    longitude= models.FloatField(verbose_name=u"longitude",null=True, blank=True)
    def __str__(self):
        return (self.user )
                
lesalert = (
        ('1', 'information '),
        ('2', 'Avertissement'),
        ('3', 'Probleme'),
     ) 
     
class notification(models.Model):

    id_al     = models.AutoField(primary_key=True)
    titre= models.CharField(max_length=50,verbose_name=u"Titre")
    type= models.CharField(max_length=1 ,choices=lesalert ,verbose_name=u"Type")
    date_al   =models.DateTimeField(verbose_name=u"Date",auto_now_add=True)
    details= models.TextField(verbose_name=u"Details")
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True) 
    projet= models.ForeignKey(Projet,on_delete=models.CASCADE,null=True)
    Tache= models.ForeignKey(Tache,null=True, blank=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return (self.titre) 

    def clean(self):
        from django.core.exceptions import ValidationError        
       
        if (self.Tache) and( self.projet):
            if(self.projet!= self.Tache.projet):
                raise ValidationError('la partie et le projet ne correspondent pas')    
              
        
    def save(self, *args, **kwargs):
        if(self.Tache and not self.projet):
             self.projet=self.Tache.projet
        super(notification, self).save(*args, **kwargs)
  




  
        