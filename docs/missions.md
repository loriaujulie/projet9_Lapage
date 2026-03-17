P9_Lapage/
├── README.md                 # Description, instructions
├── requirements.txt          # Dépendances Python
├── .gitignore                # Fichiers à ignorer
├── .github/
│   └── workflows/
│       └── ci.yml           # Pipeline CI
├── data/
│   ├── raw/                 # Données brutes
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   └── transactions.csv
│   └── processed/           # Données transformées
│       └── .gitkeep
├── Notebooks/               # Phase 1 - Analyses
│   ├── 01_explorations.ipynb
│   ├── 02_analyses_annabelle.ipynb
│   ├── 03_analyses_julie.ipynb
│   └── exports/             # HTML exports
│       └── .gitkeep
├── Reports/                 # Phase 1 - Présentations
│   ├── présentation.pptx
│   └── figures/
│       └── .gitkeep
├── dashboard/               # Phase 2 - Streamlit
│   ├── app.py
│   ├── pages/
│   │   └── .gitkeep
│   └── components/
│       └── .gitkeep
├── src/                     # Code réutilisable
│   ├── __init__.py
│   ├── data_loader.py
│   ├── analysis.py
│   ├── visualization.py
│   └── statistics.py
├── tests/                   # Phase 3
│   ├── __init__.py
│   └── .gitkeep
├── api/                     # Phase 4 - FastAPI
│   └── .gitkeep
├── models/                  # Phase 5 - ML
│   └── .gitkeep
└── docs/
    ├── specifications.md
    └── .gitkeep
