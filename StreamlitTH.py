import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import mannwhitneyu,ttest_ind,normaltest




def authenticate_gdrive():
   gauth = GoogleAuth()
   # Load client secrets from the provided path.
   gauth.LoadClientConfigFile(auth_user_credentials_path)

   # Use the following line for authentication in Google Colab
   gauth.CommandLineAuth()

   return GoogleDrive(gauth)


df_france_2010_2023 = pd.read_excel("Classeur1.xlsx")


st.sidebar.title("Sommaire")
pages=["Introduction", "Jeu de données", "Phase de Pré-traitement","Analyse et data visualisation", "Modèles ML et prédictions", "Analyses des résultats", "Conclusions et limites du projet"]
page=st.sidebar.radio("Aller vers", pages)

if page == pages[0] : 
    st.title("Introduction")

    st.header("Une Course Contre la Montre : Le Défi des Constructeurs Automobiles Européens en 2025 ")
    
    st.write("En septembre 2025, un vent d'inquiétude souffle sur les bureaux des plus grands constructeurs automobiles européens. En effet, 14 millards € de pénalités pourraient être infligées aux groupes automobiles en france selon Luca de Meo PDG de Renaul et président du lobby des constructeurs européens, l'ACEA. Face à l'ombre menaçante des nouvelles règles strictes de l'Union européenne sur les émissions de CO2, prévues initialement pour cette année-là, certains fabricants demandent désespérément un délai de deux ans. Mais pourquoi ? Quels sont les enjeux cachés derrière cette requête ? Sont-ils tous concernés ?")

    st.header("Un Projet Ambitieux pour Éclaircir l'Avenir")

    st.write("Nous avons décidé de plonger au cœur de cette problématique en réalisant une étude approfondie. Notre objectif ? Dévoiler les conséquences financières potentielles de ces pénalités pour les géants de l'automobile et identifier les gagnants et les perdants des nouvelles normes anti-pollution. Nous voulons également anticiper les mouvements stratégiques qui pourraient en découler.")

    st.header("Problématique")

    st.write("Les groupes automobiles sont -ils en capacité de respecter la règlementation sur les Emissions de CO2 des véhicules en France à partir de 2025 et d'éviter des pénalités de plusieurs milliards d'Euros ?")


    st.header("Présentation du Sommaire")

    st.write("Notre projet vise à éclaircir ces enjeux à travers une analyse approfondie des données disponibles, menée dans le cadre d'un rapport d'étude 2024-2025 en data analyse avec Datascientest. Ce travail s'articule autour de trois grandes phases. Chaque phase contribuera à mieux comprendre les défis et les opportunités liés à la mise en œuvre des nouvelles régulations sur les émissions de CO2.")

    st.write("I. Présentation du jeu de données et phase de pré-traitement")
    st.write("II. Analyse des données")
    st.write("III. Machine learning")

if page == pages[1] : 
  st.title("Présentation du jeu de données")

  st.markdown("Nous avons eu accès à deux types de sources concernant les données à utiliser pour notre problématique ,d'une part des sources Nationales et d'autre part des sources Européennes ;nous avons 15 fichiers ( un par année de 2001 à 2015 ) sur le site data.gouv.fr .Sur le site eea.europa.eu nous avons des fichiers allant de 2010 à 2023 .On voit donc le chevauchement évident de données de 2010 à 2015 ,nous reviendrons sur ce point .")

  st.markdown("A/ Présentation générales des données")  
  
  st.write("Pour la présentation générale des données, nous développerons succéssivement, les points suivants: ")

  st.write("       L'état des lieux de la règlementation")  
  st.write("       La phase de pré-traitement")


  st.write("Nous traiterons des principes généraux, nécessaires à la compréhension du sujet, à travers la règlementation Européenne, les pénalités financières et la périmètre d'analyse des émissions de co2.")
  
  st.markdown("1.Règlementation Européenne: normes EURO et CAFE")
  
  st.write("L'Union Européenne s'est fixé pour objectif de réduire d'au-moins 30 % ses émissions de CO2 d'ici 2030, par rapport à 2005. Tous les secteurs sont concernés et particulièrement le secteur automobile qui représente près de 15% des emissions.. Afin de rentrer sur le marché, les véhicules doivent se soumettre à une batterie de tests qui évaluent la consommation de carburant, les émissions de CO2 et les autres émissions polluantes, sur des cycles de conduite spécifiques.")

  st.write("Normes Euro Les normes Euro sont des réglementations de l'Union européenne visant à réduire les émissions de polluants des véhicules1 . Instaurées en 1988, elles s'appliquent aux véhicules lourds, puis aux voitures particulières et utilitaires2 . Les normes Euro ont évolué au fil des ans, passant de Euro 1 à Euro 7, avec des seuils d'émissions de CO2 de plus en plus stricts3 . Par exemple, Euro 6 impose des limites de 95 g/km pour les voitures et 147 g/km pour les véhicules utilitaires.")

  st.write("Les normes Euro et CAFE s'appliquent bien en France et en Europe. Les normes Euro sont spécifiques à l'Union européenne, tandis que les normes CAFE sont principalement américaines, mais leur influence s'étend aussi en Europe par le biais de réglementations similaires sur les émissions de CO2 des véhicules.")

  st.write("Normes CAFE Les normes CAFE (Corporate Average Fuel Economy) sont des réglementations américaines visant à améliorer l'efficacité énergétique des véhicules neufs4 . Mises en place en 1975, elles obligent les constructeurs à atteindre une moyenne d'émissions de CO2 par kilomètre pour l'ensemble de leur gamme de véhicules4 . À partir de 2025, les constructeurs européens devront respecter une limite de 93,6 g/km, contre 95 g/km actuellement. ")

  st.write("Ces normes visent toutes deux à réduire l'empreinte carbone des véhicules et à lutter contre le changement climatique.") 

   
  st.markdown("2.Pénalités financières importantes")

  st.write("C'est en 2025 que commence réellement l’application d’amendes CO2 pour les constructeurs qui ne respectent pas la reglementation en vigueur. Selon le patron de Renault et également président de l’ACEA (Association des constructeurs automùobiles européens), Luca de MeoCes, ces amendes pourraient atteindre 15 milliards d’euros dès l’année prochaine.")

  st.write("Prenons un exemple pour mieux se rendre compte de l'ampleur des pénalités. Imaginons qu'un constructeur automobile ait produit 500 000 véhicules avec une moyenne d'émissions de 100 g/km. Selon les normes, chaque véhicule dépasse la limite de 81 g/km de 19 grammes.")

  st.write("La pénalité par véhicule sera de 1805€ (19 g/km x 95 € ). donc avec une flotte de 500 000 véhicules, la pénalité totale serait de 902,5 Millions € (1805 € x 500 000).")

  st.write("Il est donc urgent que les constructeurs prennent la mesure d'un tel risque financier.")

  st.markdown("3.Périmètre d'analyse")

  st.write("La catégorisation des émissions de gaz à effet de serre (GES) anthropiques en 3 scopes 1,2 et 3 :")

  st.write("Le scope 1: Inclut toutes les émissions directes de gaz à effet de serre de l'entreprise oou, en l'occurence, les émissions des véhicules. Les véhicules éléctrique de produisent pas de CO2 lors de leur fonctionnement.")

  st.write("Le scope 2 : Il s'agit des émissions indirectes liées à la consommation d'énergie (électricité, vapeur, chaleur, froid, air comprimé, etc.) lors de la production du véhicule.")

  st.write("Les emissions de CO2 des véhicules éléctriques ne viennent pas de son utilisation mais plutôt leur production.")

  st.write("Le scope 3 :Il s'agit de toutes les autres émissions indirectes.")

  st.write("Selon le rapport de Martin Kment, la réglementation sur les émissions de CO2 d'un véhicule ne sont prises en compte qu'à l' échappement. Selon Elmar Kühn (directeur général de l'Uniti), cette méthode « entraîne immédiatement une préférence réglementaire unilatérale pour les véhicules électriques à batterie ». Cette dernière dite de l'échappement devrait être remplacée afin de prendre en compte le cycle de vie complet du véhicule. Ceci devrait être le cas à partir de 2030 dans le cadre du Green Deal. Cette nouvelle approche serait plus globale et permettrait d'être efficace pour l'environnement.")

  st.write("Dans cette étude, nous ne traiterons que des émissions directes des véhicules ( scope 1).")


if page == pages[2] : 
  st.title("Phase de Pré-traitement")

  st.markdown("LES GRANDES PHASES DE PRE-TRAITEMENT")

  st.write("Avant de procéder à l'analyse, il est essentiel de préparer les données. Cette phase inclut le nettoyage des données, la gestion des valeurs manquantes, et la normalisation des informations. Ces étapes sont cruciales pour assurer la qualité et la fiabilité des analyses futures.")

  st.markdown("1.Importation de librairie + connexion au Drive")

  st.write("Cette partie est parfaitement détaillée dans le Notebook ,nous ne nous n'y attarderons point .")


  st.markdown("2.Nettoyage, concordance et fusion (données gouv et Europe)")

  st.write("Afin de nous assurer de la continuité des données de 2010 à 2023, nous devons vérifier la concordance des données entre les données gouv et les données européennes .")
  
  st.write("A cette fin ,nous partons des deux fichiers suivants :un fichier nommé france_eu_2010_2015 qui reprend les fichiers européen de 2010 à 2015 ainsi que le fichiers france_gouv_2010_2015 qui est la synthèse des données provenant de la source gouvernementale sur la même plage .")

  st.image("Fusion des données Gouv et Européeenes.jpg")

  st.markdown("La concordance des données se réalisera en trois grandes étapes:")

  st.markdown("1.Uniformisation des données")
  st.markdown("2.Réalisation des tests statistiques")
  st.markdown("3.Conclusion sur la concordance")

  france_eu_2010_2015 = pd.read_csv('france_eu_2010_2015.csv')
  france_gouv_2010_2015 = pd.read_csv('df2.csv')

  st.write("Affichage des premières ligne de france_gouv_2010_2015 et des infos sur les deux fichiers") 
  st.dataframe(france_gouv_2010_2015.head())

  st.image("Infos_france_gouv_2010_2015.PNG")

  st.dataframe(france_eu_2010_2015.head())

  st.image("Infos_france_eu_2010_2015.PNG")


  




  st.write("Uniformisation des données des deux jeux ;nous allons successivement :")
  st.write("      *Uniformiser les marques")
  st.write("      *Uniformiser les types d'énergie")


  st.write("En effet il y a une très grande diversité de marques ( 57 dans le fichier gouv et 124 dans le fichier européen ) et certaines sont quasi anonymes ;il apparaît donc nécessaire de faire un nettoyage et un mapping au niveau de celles-ci d'une part ;d'autre part nous constatons également des différence de nommage au niveau des carburants entre les deux sources .")
  
  st.write("Afin de procéder à une comparaison de ces années de chevauchement ,il nous a aussi fallu harmoniser les noms des colonnes pour aboutir à quelque chose qui nous permettent de comparer les fichiers sur la période 2010-2015")

  st.markdown("3.Réalisation des tests statistiques")

  st.markdown("Pour nous assurer de pouvoir faire coincider les deux sources de données et ainsi avoir une continuité sur le temps long pour une analyse cohérente il nous faut faire des tests statistiques pour les deux fichiers surs la période 2010-2015 ")
  st.write("Réalisation de 4 test statistiques afin valider ou pas la concordance des données .")

  st.write("TEST1 / un test sur les médianes des émissions de CO2/MARQUE")
  st.write("TEST2 / un test sur les moyennes des émissions de CO2/MARQUE")
  st.write("TEST3 / un test sur les médianes la consommation/marque")
  st.write("TEST4 / un test sur les moyennes la consommation/marque")


  st.write("Les Hypothèses communes aux 4 tests :")

  st.write("Choix du test")

  st.write("Les hypothèses de travail")

  st.write("Hypothèse nulle (H0) : Il n'y a pas de différence significative entre les deux groupes=> les données des 2 DF sont similaires. Hypothèse alternative (H1) : Il existe une différence significative entre les deux jeux de données => les données son incompatibles .")

  st.write("Niveau de signification: 5% (seuil normatif) .")

  st.write("Conclusion")

  st.write("Y a-t-il concordance statistique entre les jeux de données (gouv et Europe) ?")

  st.write("Les données ne suivant pas une loi Normale ( voir les -Q plots ) ,nous sommes amenés à réaliser des tests non paramétriques ici celui de Mann_Whitney.")

  st.write("Pour visualiser le comportement des données nous avons tracés des Q_Q Plots sur les moyennes et médianes de certaines variables (CO2 ,Puisances réelles) pour les deux sources .")

  st.image("QQPlot.PNG")

  st.write("En conclusion de ces différents test ,il nous apparait qu'il n'y a pas de différence entre les jeux de données .gouv et .eu ,en consequence de quoi nous pouvons donc les mixer afin de produire le jeu qui nous sert finalement de base de départ .Ce jeu couvrira la période 2010 à 2023 ,ayant fait le choix de nous affranchir de la partie .gouv allant de 2001 à 2009 car contenant trop peu de données (82892 lignes) d'une part mais aussi peu fournie en caractéristiques ( masses absentes par exemple ) et avec beaucoup de Nan . ")

  st.write("Chemin faisant nous avons nettoyé ce fichier qui reprend les données de 2010 à 2023 sur l'ensemble des jeux ,nous y avons procédé a des nettoyages ,des suppressions de colonnes inutiles à notre sens mais surtout nous l'avons épuré des données extra nationales .En effet la volumetrie en terme de millions de lignes et les limitations de nos machines nous conduisent à privilégier un fichier de données franco française qui sera la base de la suite de nos travaux")












































































if page == pages[3] : 
  st.title("Analyse et data visualisation")

  st.header("A.Présentation du jeu de données")

  # Aperçu général
  st.dataframe(df_france_2010_2023.head())


  st.subheader("Statistiques descriptives")
  st.dataframe(df_france_2010_2023.describe())

  sns.set()

  #1er graphique
  fig = plt.figure(figsize=(10,6))
  sns.countplot(x = "ANNEE", data = df_france_2010_2023)
  plt.title("Nombre total de véhicule par année")
  plt.xlabel('Année')
  plt.ylabel('Nombre de véhicules')
  plt.ylim(0,2500000)

  st.pyplot(fig)

  st.write("Nous constatons une grande différence dans le nombre de véhicules avant et après 2016. Après vérification sur divers sites, nous validons le fait qu'il y ait si peu de données sur les années antérieures 2017. L'analyse descriptive prendra en compte l'ensemble de la période tandis que le machine learning se portera sur les données à compter de 2017.")


  st.header("B.Emission de Co2 par groupe automobile")
  #2ème graphique
  # Calculer les médianes de 'CO2(g/km)' par groupe automobile
  medians = df_france_2010_2023.groupby('Groupe_auto')['CO2(g/km)'].median().sort_values(ascending=False)

  # Calculer les médianes de 'CO2(g/km)' par groupe automobile
  medians = df_france_2010_2023.groupby('Groupe_auto')['CO2(g/km)'].median().sort_values(ascending=False)

  # Réorganiser les groupes automobiles par médiane décroissante
  df_france_2010_2023['Groupe_auto'] = pd.Categorical(df_france_2010_2023['Groupe_auto'], categories=medians.index, ordered=True)

  # Tracer le boxplot
  fig = plt.figure(figsize=(15, 7))
  sns.boxplot(x='Groupe_auto', y='CO2(g/km)', data=df_france_2010_2023, palette='viridis')

  # Ajuster les étiquettes de l'axe des x pour une meilleure lisibilité
  plt.xticks(rotation=90)

  # Titre et étiquettes des axes
  plt.title('Distribution de CO2 (g/km) par Groupe Automobile', fontsize=15)
  plt.xlabel('Groupe Automobile', fontsize=12)
  plt.ylabel('CO2 (g/km)', fontsize=12)

  # Afficher le graphique
  st.pyplot(fig)

  st.write("On perçoit 3 grandes catégories de marque:")
  st.write("Les grands emetteurs de CO2 (violet) représentés par des marques de voiture de sport :Aston Martin, Ferrari, Subaru, Mc Laren etc..")
  st.write("Les marques généralistes (en vert) avec beaucoup d'outliers. Cependant, ces derniers restent inférieurs à 600g/gm.")
  st.write("les voitures éléctrique (dont les emissions sont à 0)")


  #3ème graphique
  # Calcul des quartiles et de l'IQR
  Q1 = df_france_2010_2023['CO2(g/km)'].quantile(0.25)
  Q3 = df_france_2010_2023['CO2(g/km)'].quantile(0.75)
  IQR = Q3 - Q1

  # Détection des valeurs aberrantes
  borne_inferieure = Q1 - 1.5 * IQR
  borne_superieure = Q3 + 1.5 * IQR

  # Séparation des valeurs aberrantes en fonction des bornes
  valeurs_aberrantes_inferieures = df_france_2010_2023[df_france_2010_2023['CO2(g/km)'] < borne_inferieure]
  valeurs_aberrantes_superieures = df_france_2010_2023[df_france_2010_2023['CO2(g/km)'] > borne_superieure]
  valeurs_normales = df_france_2010_2023[(df_france_2010_2023['CO2(g/km)'] >= borne_inferieure) & (df_france_2010_2023['CO2(g/km)'] <= borne_superieure)]

  fig = plt.figure(figsize=(12, 6))

  # Histogramme pour les valeurs normales
  sns.histplot(valeurs_normales['CO2(g/km)'], color='blue', label='Valeurs normales', bins=30)

  # Histogramme pour les valeurs aberrantes inférieures
  if not valeurs_aberrantes_inferieures.empty:
    sns.histplot(valeurs_aberrantes_inferieures['CO2(g/km)'], color='red', label='Valeurs aberrantes inférieures', bins=30)

  # Histogramme pour les valeurs aberrantes supérieures
  if not valeurs_aberrantes_superieures.empty:
    sns.histplot(valeurs_aberrantes_superieures['CO2(g/km)'], color='green', label='Valeurs aberrantes supérieures', bins=30)

  # Ajouter des lignes pour les bornes
  plt.axvline(borne_inferieure, color='r', linestyle='--', label='Borne inférieure')
  plt.axvline(borne_superieure, color='g', linestyle='--', label='Borne supérieure')

  plt.title('Histogramme des émissions de CO2 (g/km)')
  plt.xlabel('CO2 (g/km)')
  plt.ylabel('Fréquence')
  plt.legend()
  st.pyplot(fig)

  st.write("L'analyse des valeurs extrêmes montre l'importance du nombre de valeurs extrêmes au-dessus et en dessous des bornes. Cependant, pour les valeurs extrêmes au-dessus, leur visualisation montre une certaine tenue en dessous de 600g/km pour l'ensemble des groupes. Aussi, nous decidons de conserver ces valeurs et les considérons comme les véhicules les plus emetteurs de CO2. S'agissant des valeurs en dessous de la borne basse, il s'agit des meilleurs véhicules. Les valeurs à 0 correspondent aux véhicules principalement électriques.")

  st.header("C.Emissions par typologie d'énergie")






 
 



  
  
  

 
  



  





















