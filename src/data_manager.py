# CREATION D'UNE FONCTION PERMETTANT D'INSPECTER LE DATAFRAME EN DRY

def inspection (df) : 
    print('\n---------------------------------------------------------------------')
    print('INSPECTION DU DATAFRAME')
    print('---------------------------------------------------------------------')

    print('\n---------------------------------------------------------------------')
    print('Affichage de la structure du df (colonnes, lignes):')
    print('---------------------------------------------------------------------')
    print('nombre de lignes :', df.shape[0])
    print('nombre de colonnes :', df.shape[1])

    print('\n---------------------------------------------------------------------')
    print('Noms des colonnes :')
    print('---------------------------------------------------------------------')
    print (df.columns) 

    print('\n---------------------------------------------------------------------')
    print('Affichage des principales informations statistiques des données du df :')
    print('---------------------------------------------------------------------')
    print(df.describe())

    print('\n---------------------------------------------------------------------')
    print('Types des données :')
    print('---------------------------------------------------------------------')
    print(df.dtypes)

    print('\n---------------------------------------------------------------------')
    print('Affichage du nombre de valeurs uniques (afin de définir ce qui pourrait représenter une PK / FK):')
    print('---------------------------------------------------------------------')
    print(df.nunique())

    print('\n---------------------------------------------------------------------')
    print('Affichage du nombre de valeurs manquantes :')
    print('---------------------------------------------------------------------')
    print(df.isnull().sum())

    print('\n---------------------------------------------------------------------')
    print('Affichage du nombre de doublons :')
    print('---------------------------------------------------------------------')
    print (df.duplicated().sum())

    print('\n---------------------------------------------------------------------')
    print('Affichage des 5 premières lignes :')
    print('---------------------------------------------------------------------')
    print(df.head())
    print('\n---------------------------------------------------------------------')

# créer une itération sur chaque colonne

    valeurs_uniques = df.nunique()
    pk_possible = [col for col in df.columns if valeurs_uniques[col] == df.shape[0]]

    if pk_possible:
        print("Colonnes pouvant constituer une clé primaire :", pk_possible)
    else:
        print("Aucune colonne ne peut constituer une clé primaire en l'état.")

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

import pandas as pd
def verification_df (df, col1, col2):
    if not isinstance (df, pd.DataFrame) :
        print('KO, ce n\'est pas un dataframe')
        return
    if col1 not in df.columns or col2 not in df.columns :
        print('KO, la/les colonne(s) n\'existe(nt) pas dans le dataframe')
        return
    if not pd.api.types.is_numeric_dtype(df['col1']) or not pd.api.types.is_numeric_dtype(['col2']) :
        print('KO, la/les colonne(s) n\'est pas au format entier')
        return
print('ok, étape suivante')

# Réponse à la recherche de réalisation de la 

def verification_donnees_utilisateur(df,var1,var2):
    
    resultats = {
        'type_df':type(df)._name_,
        'dtype_var1':df[var1].dtype if var1 in df.columns else None,
        'dtype_var2':df[var2].dtype if var2 in df.columns else None,
    }
    return resultats    
    
    # appel de la fonction 
verification_donnees_utilisateur(df=clients, var1='variable_choisie_1',var2='variable_choisie_2')

# Méthode SHAPIRO de scipy : test de shapiro-Wilk
from scipy.stats import shapiro

def verification_normalite (df,var):

    # verifie la normalité
    stat, p_shapiro = shapiro(df[var])

    # retour des résultats
    resultats = {
        'shapiro_stat': stat,
        'p_value': p_shapiro,
    }
    return resultats