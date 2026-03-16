# Projet 9 de la formation Data Analyst OpenClassrooms - GRETA
# Produisez une étude de marché avec Python (Lapage)

**Auteur :** Julie LORIAU SENSENBRENNER  
**Date :** Mars 2026  
**Repository :** [loriaujulie/projet9_Lapage](https://github.com/loriaujulie/projet9_Lapage)

## 📖 Contexte et mission
**Contexte**
Je viens d'arriver en tant que Data Analyst au sein de l'entreprise Lapage, une librairie physique mais également en ligne (depuis 2 ans). 
L'équipe se compose de :
- Annabelle : Responsable Marketing
- Julie : Business Intelligence Analyst 

Le projet sera présenté au CODIR avec Sylvain, le nouveau responsable commercial.

Il s'agit de faire un point global sur les différents indicateurs et chiffres clés de l'entreprise Lapage.

**Objectifs**
- Explorer les données (clients, produits, transactions).
- Analyser les ventes pour identifier points forts/faibles, profils clients et recommandations (offres, prix).
- Réaliser des analyses descriptives, KPI, tests statistiques.
- Segmenter les clients (RFM, clustering K-means, ACP).
- Produire un dashboard -> rapport et visualisations pour équipe (Annabelle, Julie).

## Données

- customers.csv : Profils clients (âge, genre, etc.).
- products.csv : Catalogue des produits.
- transactions.csv : Ventes (dates, montants, IDs).

Je divise l'organisation de mon projet en plusieurs sous-dossiers
- Csv bruts dans `data/raw/`
- Csv traités dans `data/processed/`. 
--> Respect RGPD simulé.

## 🛠️ Structure du projet

P9_Lapage/
├── README.md                   # Ce fichier
├── requirements.txt            # Dépendances
├── data/
│ ├── raw/                      # Données brutes
│ └── processed/                # Données traitées
├── Notebooks/                  # Analyses Jupyter
│ ├── 01_explorations.ipynb
│ ├── 02_analyses_annabelle.ipynb
│ ├── 03_analyses_julie.ipynb
│ └── exports/
├── Reports/
│ ├── présentation.pptx         # Rapport final
│ └── figures/
└── .github/workflows/ci.yml    # Tests CI