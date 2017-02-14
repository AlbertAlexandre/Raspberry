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


    def SQL_loadListedesJoueurs(self, commencant= None):
        """Return la requête SQL pour charger la liste des noms  des joueurs sépcial Combobox (un paramètre optionels : 'commencant') ... """
        laRequete = """SELECT c10_id as Id, CONCAT_WS(' ',c10_prenom , c10_nom , '(',c10_alias_nom, ')') as joueur FROM t10_individus """
        if commencant != None :
            laRequete += " where CONCAT_WS(' ',c10_prenom , c10_nom ,c10_alias_nom) like '%{}%' ".format(commencant)
        laRequete += " order by c10_prenom , c10_nom "
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_loadUnIndividu(self, Id_individu = 0):
        """Return la requête SQL pour charger les renseignements sur un individu (un paramètre obligatoire : Id_individu) ... Return également la liste des colonnes"""
        laRequete = """select c10_id as Id
        , c10_nom as nom
        , c10_prenom as prenom
        , c10_date_naissance as dateNaissance
        , c10_mail as mail
        , c10_alias_nom as alias
        , c10_c20_id as Id_Image
        , c20_blob as avatar
        , c10_password as password
         from v10_individus  where c10_id = {} limit 1 """.format(Id_individu)
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_insertUnIndividu(self, Individu):
        """Return la requête SQL pour insérer un enregistrement dans la table t10_individus """
        laRequete = " INSERT INTO t10_individus (c10_nom , c10_prenom , c10_date_naissance , c10_mail , c10_alias_nom , c10_c20_id , c10_password) VALUES ( "
        if Individu[1] : laRequete += "  '{}'".format(Individu[1])
        else : laRequete += "  null"
        if Individu[2] : laRequete += ", '{}'".format(Individu[2])
        else : laRequete += ", null"
        if Individu[3] : laRequete += ", '{}'".format(Individu[3])
        else : laRequete += ", null"
        if Individu[4] : laRequete += ", '{}'".format(Individu[4])
        else : laRequete += ", null"
        if Individu[5] : laRequete += ", '{}'".format(Individu[5])
        else : laRequete += ", null"
        if Individu[6] : laRequete += ", '{}'".format(Individu[6])
        else : laRequete += ", null"
        if Individu[7] : laRequete += ", '{}'".format(Individu[7])
        else : laRequete += ", null"
        laRequete += " )"
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_UpdateUnIndividu(self, Individu):
        """Return la requête SQL pour faire des updates sur un enregistrement dans la table t10_individus """
        v = "" # pour insérer une virgule ...
        laRequete = " UPDATE t10_individus SET "
        if Individu[1] :
            laRequete += v + "  c10_nom = '{}' ".format(Individu[1])
            v = ","
        if Individu[2] :
            laRequete += v + "  c10_prenom = '{}' ".format(Individu[2])
            v = ","
        if Individu[3] :
            laRequete += v + "  c10_date_naissance = '{}' ".format(Individu[3])
            v = ","
        if Individu[4] :
            laRequete += v + "  c10_mail = '{}' ".format(Individu[4])
            v = ","
        if Individu[5] :
            laRequete += v + "  c10_alias_nom = '{}' ".format(Individu[5])
            v = ","
        if Individu[6] :
            laRequete += v + "  c10_c20_id = '{}' ".format(Individu[6])
            v = ","
        if Individu[7] :
            laRequete += v + "  c10_password = '{}' ".format(Individu[7])
        else:
            laRequete += v + "  c10_password = null "

        laRequete += " WHERE c10_id = {} ".format(Individu[0])
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_DeleteUnIndividu(self, Id_Individu = 0):
        """Return la requête SQL pour supprimer un enregistrement dans la table t10_individus """
        v = "" # pour insérer une virgule ...
        laRequete = " DELETE FROM t10_individus WHERE c10_id = {} ".format(Id_Individu)
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_loadLaListeDes_IdImages(self):
        """Return la requête pour faire la liste les Id existant des images de la table t20_images """
        laRequete = """ SELECT distinct c20_id as id_image FROM t20_images order by c20_desc,c20_id """
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_loadUneImage(self, Id_Image = -1):
        """Return la requête pour loader une image et ses infos la table t20_images
        avec le nombre de fois ou l'image est utilisée dans la table : t10_individus """
        laRequete = " SELECT c20_id as id "
        laRequete += " , c20_nom as nom "
        laRequete += " , c20_taille as taille "
        laRequete += " , c20_type as type "
        laRequete += " , c20_desc as descption "
        laRequete += " , c20_blob as image "
        laRequete += " , (select count(*) from t10_individus where c10_c20_id = c20_id ) as nb_use "
        laRequete += " FROM t20_images "
        laRequete += " where c20_id = {} ".format(Id_Image)
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_loadUneImageCarte(self, IdCarte = -1):
        """Return la requête pour loader une image de la carte """
        laRequete = " SELECT c22_nom as nom , c22_image as image FROM t22_images_cartes where c22_id = {} ".format(IdCarte)
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_listeDesTablesDeBeloteDisponibles(self):
        """Return la liste des tables de belote en préparation (c14_etat = 'PREPA') """
        laRequete = " SELECT c14_id as Id_Table "
        laRequete += " , c14_table_name as NomDeTable "
        laRequete += " , date_format(c14_date, '%d/%m/%Y %Hh%i') as laDate "
        laRequete += " , timestampdiff(minute,c14_date,now()) as creation "
        laRequete += " FROM t14_les_parties t14 "
        laRequete += " inner join t12_le_jeux t12 on t12.c12_id = t14.c14_c12_id "
        laRequete += " where t12.c12_nomDuJeux = 'Belote' "
        laRequete += " and t14.c14_etat = 'PREPA' "
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_InfoSurLesTablesDeBeloteDisponibles(self , idTable = -1 , etat = 'PREPA'):
        """Return les informations sur les tables (ou une table précise) de belote disponible """
        laRequete = " SELECT idTable,tableName,valeur,TypeComptage,nord,sud,est,ouest FROM v_tables_en_cours "
        laRequete += " where etat = '{}' ".format(etat)
        if idTable != -1:
            laRequete += " and idTable = {} ".format(idTable)
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_creerUneNouvelleTableDeBelote(self , laTable=[]):
        """Création d'une nouvelle table de Belote """
        laRequete = " INSERT INTO t14_les_parties "
        laRequete += "(c14_c12_id,c14_etat,c14_date,c14_lieu "
        laRequete += " ,c14_table_name,c14_jeux_aux_tours,c14_jeux_aux_points "
        laRequete += " , c14_joueur_N , c14_joueur_S , c14_joueur_E , c14_joueur_W ) VALUES "
        laRequete += "( 10 , 'PREPA' , now() , 'reseau' "
        laRequete += ", '{}'".format(laTable[0])
        if laTable[1] : laRequete += ", {}".format(laTable[1])
        else:  laRequete += ", NULL "
        if laTable[2] : laRequete += ", {} ".format(laTable[2])
        else:  laRequete += ", NULL "
        if laTable[3] == 'NORD' : laRequete += ", {} ".format(laTable[4])
        else:  laRequete += ", NULL "
        if laTable[3] == 'SUD' : laRequete += ", {} ".format(laTable[4])
        else:  laRequete += ", NULL "
        if laTable[3] == 'EST' : laRequete += ", {} ".format(laTable[4])
        else:  laRequete += ", NULL "
        if laTable[3] == 'OUEST' : laRequete += ", {} )".format(laTable[4])
        else:  laRequete += ", NULL )"
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_leJoueurEstDejaInscritAUneTable(self, IdUser = -1):
        """Return la requête pour vérifier que l'utilisateur n'est pas déjà inscrit à une table """
        laRequete = " SELECT c14_id,c14_table_name FROM v_joueurs_presents where etat = 'PREPA' and xJoueur = {} ".format(IdUser)
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_leJoueurATIlEteDeconnecteDUneTable(self, IdUser = -1):
        """Return la requête pour vérifier que l'utilisateur n'a pas été déconnecté d'une table de belote"""
        laRequete = " SELECT c14_id,c14_table_name FROM v_joueurs_presents where etat = 'ENCOURS' and xJoueur = {} ".format(IdUser)
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_estCeAMoiDeJouer(self, IdUser = -1 , IdTable = -1):
        """Return 0 si ce n'est pas au joueur courant de jouer si non retouren l' IdUser """
        laRequete =  "SELECT DISTINCT CASE WHEN NOT EXISTS ( "
        laRequete += " SELECT c14_id FROM t14_les_parties WHERE c14_etat = 'ENCOURS' AND c14_id = {} AND c14_qui_doit_jouer = {} ".format(IdTable,IdUser)
        laRequete += " ) THEN 0 ELSE {} END AS OuiNon ".format(IdUser)
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_quiDoitJouer(self, IdTable = -1):
        """Return 0 si la partie n'est pas commencée si non retourne l'IdUser du joueur qui doit jouer """
        __select = " ( SELECT c14_qui_doit_jouer FROM t14_les_parties WHERE c14_etat = 'ENCOURS' AND c14_id = {} ) ".format(IdTable)
        laRequete =  "SELECT DISTINCT CASE WHEN NOT EXISTS " + __select + " THEN 0 ELSE " + __select + " END AS qui "
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_inscrireUnNouveauJoueur(self, IdUser = -1 , IdTable = -1 , laPlace = 'xxx' , nbInscrit = -1):
        """Inscrire un nouveau joueur à une table """
        laRequete = " UPDATE t14_les_parties SET c14_date = now() "
        if laPlace == 'NORD' : laRequete += ' , c14_joueur_N = {} '.format(IdUser)
        if laPlace == 'SUD' : laRequete += ' , c14_joueur_S = {} '.format(IdUser)
        if laPlace == 'EST' : laRequete += ' , c14_joueur_E = {} '.format(IdUser)
        if laPlace == 'OUEST' : laRequete += ' , c14_joueur_W = {} '.format(IdUser)
        laRequete += ' WHERE c14_id = {} '.format(IdTable)

        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQL_commencerLaPartie(self, IdTable = -1 , qui = 1):
        """La table est complete, passer l'état 'ENCOURS' """
        laRequete = " UPDATE t14_les_parties SET c14_etat = 'ENCOURS' "
        if qui == 1 : laRequete += " , c14_qui_doit_jouer = c14_joueur_N "
        if qui == 2 : laRequete += " , c14_qui_doit_jouer = c14_joueur_S "
        if qui == 3 : laRequete += " , c14_qui_doit_jouer = c14_joueur_E "
        if qui == 4 : laRequete += " , c14_qui_doit_jouer = c14_joueur_O "
        laRequete += ' WHERE c14_id = {} '.format(IdTable)

        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQLPS_supprimerInscriptionAUneTable(self, IdTable =-1 , IdUser = -1):
        """Supprimer l'inscription d'un joueur à une table """
        laRequete = "ps_SupprimerInscriptionAUneTable" , ( IdTable , IdUser )
        # on renseigne la requête SQL
        self.__LaRequete = laRequete

    def SQLPS_supprimerLesTablesDeBeloteObsolete(self, x_Minutes = 180):
        """Supprimer les tables de belote en préparation ancienne (+180 minutes par defaut) """
        laRequete = "ps_SupprimerLesPartiesObsoletes" , ( x_Minutes , ) #il faut retourner un tuple pour les paramètres
        # on renseigne la requête SQL
        self.__LaRequete = laRequete
