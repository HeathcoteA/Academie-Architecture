import pandas
#librairie exterieure pour utiliser les classes pour la BD
from sqlalchemy.ext.declarative import declarative_base
#utiliser les fonctions associées à la librairie
from sqlalchemy import Column, Integer, String, Text, create_engine, MetaData
from sqlalchemy.orm import sessionmaker

Base=declarative_base()
metadata=MetaData()

#creation de la classe
#nom de l'institution et création des champs de la table
class academie(Base):
    __tablename__='bibliotheque'
    fix_id= Column(Integer, primary_key=True)
    fix_auteur= Column(String(200), nullable=False)
    fix_titre=Column(String(400), nullable=False)
    fix_publisher=Column(String(200), nullable=False)
    fix_annee=Column(Text, nullable=False)
    fix_localisation=Column(String(200), nullable=False)

    #creation de la base et connexion au server: remplacer user et pwd !
engine=create_engine('mysql://user:pwd@localhost/academie')

#creation de la table
Base.metadata.create_all(engine)

#creation d'une session pour la base de données
session=sessionmaker()
session.configure(bind=engine)
s=session()

#importation des données avec librairie Pandas
file = pandas.read_csv('corpus_test.csv',';')
file.to_sql(con=engine, name="bibliotheque", if_exists='replace')
