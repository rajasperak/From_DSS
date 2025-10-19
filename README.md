# From_DSS

Titre du Projet

Pipeline d'Analyse Marketing avec Dataiku DSS

Description

Ce projet contient un pipeline Dataiku DSS conçu pour l'analyse marketing dans le secteur de la distribution. Le pipeline permet de préparer les données, de calculer des indicateurs clés (KPI), de réaliser des analyses historiques et de segmenter les clients à l'aide de techniques de clustering.

Structure du Pipeline

- Étapes du Pipeline

ÉtapeDescription:

- AGGREG_ZONE : Zone d'agrégation des données brutes.
- RFM_PIPE_SNAPSHOT : Capture instantanée des données RFM (Récence, Fréquence, Montant).
- RFM_CLUSTERS : Segmentation des clients en clusters basés sur les indicateurs RFM.
- KPI : Calcul des indicateurs clés de performance (KPI) pour le suivi marketing.
- RFM_PIPE_HISTORIC : Archivage et analyse des données historiques.

![pipeline](https://github.com/user-attachments/assets/9a4cf4e0-bed8-4ad2-84dd-12e1f9832ed2)

Pour visualiser les résultats sur Tableau Public :

https://public.tableau.com/app/profile/tantsoa.rajaspera/viz/Business_analyse_entreprises_paraisiennes_hyper/Histoire1

![tableau](https://github.com/user-attachments/assets/4babb1c6-87ad-406e-9b6a-230fa70c4344)

---

## Ajouts et documentation complémentaire

Les sections ci-dessous ont été ajoutées en complément du README original pour faciliter l'utilisation hors Dataiku. Le contenu original est conservé.

### Scripts ajoutés

- `scripts/rfm_kmeans.py` : script extrait du notebook `df_RFM_clustering_kmeans.ipynb`. Expose la fonction `compute_rfm_clusters(df, n_clusters=5)` qui renvoie le DataFrame avec une colonne `cluster`. Un CLI permet de travailler avec des fichiers CSV.

### Tests

- `tests/test_rfm_kmeans.py` : tests unitaires pytest (happy path + gestion des colonnes manquantes).

### Dépendances

- `requirements.txt` contient les dépendances principales : `pandas`, `numpy`, `scikit-learn`, `pytest`.

Installez-les avec :

```bash
python3 -m pip install -r requirements.txt
```

Note : le package `dataiku` est optionnel et uniquement nécessaire si vous exécutez les scripts depuis Dataiku DSS.

### Utilisation rapide

En Python :

```python
from scripts.rfm_kmeans import compute_rfm_clusters
import pandas as pd

# Charger vos données
df = pd.read_csv('data/input.csv')
# Calculer les clusters
df_with_clusters = compute_rfm_clusters(df, n_clusters=5)
# Sauvegarder
df_with_clusters.to_csv('data/output_with_clusters.csv', index=False)
```

En ligne de commande :

```bash
python3 scripts/rfm_kmeans.py --input data/input.csv --output data/output.csv --n-clusters 5
```

Options disponibles :
- `--input` : chemin vers le CSV d'entrée (obligatoire)
- `--output` : chemin vers le CSV de sortie (obligatoire)
- `--n-clusters` : nombre de clusters (par défaut 5)

### Tests unitaires

Les tests utilisent `pytest`.

Exécuter les tests depuis la racine du dépôt :

```bash
PYTHONPATH=. pytest -q
```

### Structure du dépôt (vue simplifiée)

```
From_DSS/
├─ scripts/
│  └─ rfm_kmeans.py
├─ tests/
│  └─ test_rfm_kmeans.py
├─ df_RFM_clustering_kmeans.ipynb
├─ requirements.txt
└─ README.md
```

### Notes Dataiku

- Le code original provient d'une recette Dataiku. Le script `scripts/rfm_kmeans.py` est écrit pour fonctionner hors Dataiku (pandas, scikit-learn), mais peut être adapté pour utiliser l'API Dataiku si nécessaire.

### Contribution

PRs bienvenues. Pour les changements majeurs : ouvrez d'abord une issue décrivant la proposition.

Checklist avant PR

- Lint et tests locaux passés
- Ajout de tests pour toute nouvelle fonctionnalité

---

Si vous souhaitez que j'ajoute :
- une GitHub Action CI pour lancer pytest automatiquement,
- un `pyproject.toml` pour installer `scripts` comme package,
- ou l'extraction d'autres notebooks en scripts,

répondez et je m'en occupe.
