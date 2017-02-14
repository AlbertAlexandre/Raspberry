class LesRequetes_SQL(object):
    """class recuil les requêtes SQL utilisées dans la programme"""
    def __init__(self, **kwargs):
        self.__LaRequete = ''

        return super().__init__(**kwargs)

    def LeCodeSQLDeLaRequete(self):
        """Retourne le code SQL de la requête demandée..."""
        return self.__LaRequete

    def LeCodeSQL_Directement(self, laRequete):
        """ on utilise cette fonction quand on veut passer une requête SQL directement dans le code (il faut donc renseigner le paramètre)"""
        self.__LaRequete = laRequete

    def SQL_projetEnCours(self):
        """Return la requête pour vérifier si il y a des projet en cours..."""
        fichier_adr = open("/sys/class/net/eth0/address", "r")
        adr_mac = fichier_adr.read()
        adr_mac = adr_mac.rstrip()
        laRequete = " SELECT c10_Numero FROM t10_raspberry WHERE c10_Addresse_MAC = '" + adr_mac + "'"
        # on renseigne la requête SQL
        self.__LaRequete = laRequete


    def SQL_loadListedesModes(self):
        
        laRequete = "SELECT c11_Nom FROM t11_Configuration WHERE 1 ORDER BY c11_Nom"	
        # on renseigne la requête SQL
        self.__LaRequete = laRequete
        
    def SQL_loadLeMode(self, unNom):
        laRequete = " SELECT * FROM t11_Configuration WHERE c11_Nom = '" + unNom + "'"
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

        
    def SQL_insertUneCommande(self, Configuration):
        print(Configuration)
        laRequete = " INSERT INTO t11_Configuration (c11_Nom , c11_Preview , c11_Nettete , c11_Contraste , c11_Luminosite, c11_Saturation, c11_Sensibilite_ISO, c11_Compensation_EV, c11_Exposition, c11_AWB, c11_AWBGR, c11_AWBGB, c11_Resolution, c11_Qualite, c11_Metadonnee) VALUES ( "
        laRequete += " '{}'".format(Configuration[0])
        laRequete += ", '{}'".format(Configuration[1])
        laRequete += ", '{}'".format(Configuration[2])
        laRequete += ", '{}'".format(Configuration[3])
        laRequete += ", '{}'".format(Configuration[4])
        laRequete += ", '{}'".format(Configuration[5])
        laRequete += ", '{}'".format(Configuration[6])
        laRequete += ", '{}'".format(Configuration[7])
        laRequete += ", '{}'".format(Configuration[8])
        laRequete += ", '{}'".format(Configuration[9])
        laRequete += ", '{}'".format(Configuration[10])
        laRequete += ", '{}'".format(Configuration[11])
        laRequete += ", '{}'".format(Configuration[12])
        laRequete += ", '{}'".format(Configuration[13])
        laRequete += ", '{}'".format(Configuration[14])
        laRequete += " )"
        self.__LaRequete = laRequete
