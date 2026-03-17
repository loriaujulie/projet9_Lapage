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

    print('Affichage du nombre de doublons :')
    print('---------------------------------------------------------------------')
    print (df.duplicated().sum())
   
    print('\n---------------------------------------------------------------------')
    print('Affichage des 5 premières lignes :')
    print('---------------------------------------------------------------------')
    print(df.head())
    print('\n---------------------------------------------------------------------')

# créer une itération sur chaque colonne
    if df.shape[0] == df.nunique().sum() :
        print('Il n\'y a pas de doublons dans ce dataframe, cela peut constituer une PK ou FK')
    else : 
        print('Il y a des doublons dans ce dataframe, cela ne peut constituer une PK ou FK en l\'état')