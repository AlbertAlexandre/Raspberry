import mysql.connector as connecteur_mySQL
from LesRequetes_SQL import *
from tkinter import messagebox


class Donnees_SQL(LesRequetes_SQL):
    """Traiter des données d'une base de données (MySQL). 
    Le code SQL peut être fourni directement dans 'current_CodeSQL' ou on le trouve dans : LesRequetes_SQL """
    def __init__(self, ConnexionString = '' ,**kwargs):
        # initialisation du recueil des requêtes SQL...
        LesRequetes_SQL.__init__(self)
        self.__config  = ConnexionString  
        self.__rows = []
        self.__colsName = []
        self.__colsType = []
        self.__msg_Err = None

        return super().__init__(**kwargs)

    def messageErreur(self):
        """Return le message d'erreur MySQL..."""
        return self.__msg_Err

    def __traitementDesErreurs(self):
        """ on affiche le message d'erreur dans un messagbox """
        messagebox.showinfo('Message class : Donnees_SQL',self.__msg_Err )
 

    def leNomDesColonnes(self):
        """ return le nom de chaque colonne de la requête..."""
        return self.__colsName

    def leTypeDesColonnes(self):
        """ return le type de chaque colonne de la requête (LONG,DATE,VAR_STRING...)"""
        return self.__colsType

    def chargerLesDonnees_RequeteSQL(self):
        """ Ouvre la base execute la requete SQL et referme la base de donnees et retourne les enregistrements..."""
        try:
            conn =  connecteur_mySQL.connect(**self.__config)
            cursor = conn.cursor()
            cursor.execute(self.LeCodeSQLDeLaRequete()) 
            self.__rows = cursor.fetchall()
            conn.close()
            # instancie les tuples des noms et du type des colonnes de la requête
            self.__colsName = []
            self.__colsType = []
            for col in cursor.description: 
                self.__colsName.append(col[0])
                self.__colsType.append(connecteur_mySQL.FieldType.get_info(col[1]))
            self.__msg_Err = None
            return self.__rows             
        except connecteur_mySQL.Error as err :
            self.__msg_Err = err
            self.__traitementDesErreurs()
            return 0

    def executerlaRequeteSQL(self):
        """ Ouvre la base execute la requete SQL et referme la base de donnees..."""
        try:
            conn =  connecteur_mySQL.connect(**self.__config)
            cursor = conn.cursor()
            cursor.execute(self.LeCodeSQLDeLaRequete())
            conn.commit()
            conn.close()
            self.__msg_Err = None
            leRetour = cursor.lastrowid # si création d'un nouvel enregistrement, return de l'ID   
            # on retourne -1 car on ne veux pas retourner 0 dans le cas ou la procédure ne retourne rien
            if leRetour:
                return leRetour  
            else: 
                return -1   
        except connecteur_mySQL.Error as err :
            self.__msg_Err = err
            self.__traitementDesErreurs()
            return 0 

    def executerlaProcedureStockee(self):
        """ Ouvre la base execute la procédure, referme la base de donnees..."""
        try:
            leRetour = -1 # on initialise à -1 car on ne veux pas retourner 0 dans le cas ou la procédure ne retourne rien
            conn =  connecteur_mySQL.connect(**self.__config)
            cursor = conn.cursor()
            # le nom de la procédure stockée est en position [0] et suive les paramètres pour la procédure.
            cursor.callproc( self.LeCodeSQLDeLaRequete()[0] , self.LeCodeSQLDeLaRequete()[1] )  
            self.__msg_Err = None
            #print('cursor.fetchwarnings --->',cursor.fetchwarnings())
            #print('cursor.rowcount --->',cursor.rowcount)
            #print('cursor.statement --->',cursor.statement)
            #print('cursor.fetchone --->',cursor.fetchone())
            #print('cursor.getlastrowid --->',cursor.getlastrowid())
            #print('cursor.stored_results --->',cursor.stored_results())
            for result in cursor.stored_results():
                leRetour = result.fetchone()[0]
            conn.commit()
            conn.close()
            return leRetour     
        except connecteur_mySQL.Error as err :
            self.__msg_Err = err
            self.__traitementDesErreurs()
            return 0 
        
    def chargerLesDonnees_ProcedureStockee(self):
        """ Ouvre la base execute la Procedure Stockee SQL et referme la base de donnees et retourne les enregistrements..."""
        try:
            conn =  connecteur_mySQL.connect(**self.__config)
            cursor = conn.cursor()
            # le nom de la procédure stockée est en position [0] et suive les paramètres pour la procédure.
            cursor.callproc(self.LeCodeSQLDeLaRequete()[0],self.LeCodeSQLDeLaRequete()[1:])  
            for result in cursor.stored_results():
                self.__rows = result.fetchall()
            conn.close()
            # instancie les tuples des noms et du type des colonnes de la requête
            self.__colsName = []
            self.__colsType = []
            for col in cursor.description: 
                self.__colsName.append(col[0])
                self.__colsType.append(connecteur_mySQL.FieldType.get_info(col[1]))
            self.__msg_Err = None
            return self.__rows             
        except connecteur_mySQL.Error as err :
            self.__msg_Err = err
            self.__traitementDesErreurs()
            return 0