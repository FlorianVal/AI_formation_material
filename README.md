# Slides de Formation GenAI

Ce répertoire contient les fichiers nécessaires pour générer des slides de formation sur l'Intelligence Artificielle Générative.

## Structure du projet

- `src/LLM_intro.tex` : Fichier principal des slides en LaTeX (Beamer)
- `src/gen_figures.py` : Script Python pour générer les illustrations
- `figures/` : Dossier où sont stockées les illustrations générées

## Prérequis

- LaTeX avec Beamer
- Python 3.x
- Bibliothèques Python : matplotlib, numpy

## Installation des dépendances

```bash
pip install matplotlib numpy
```

## Génération des figures

Pour générer les illustrations utilisées dans les slides :

```bash
cd src
python gen_figures.py
```

Les figures seront créées dans le dossier `figures/`.

## Compilation des slides

Pour compiler les slides en PDF :

```bash
cd src
pdflatex LLM_intro.tex
```

Ou, si vous utilisez un éditeur LaTeX comme TeXstudio, ouvrez simplement le fichier `LLM_intro.tex` et utilisez la fonctionnalité de compilation.

## Contenu des slides

Les slides couvrent les concepts fondamentaux de l'IA générative :

1. Le concept de modèle en IA
2. La définition mathématique d'un modèle
3. Exemple avec un LLM (Large Language Model)
4. Génération de texte causale (autoregressive)
5. Le processus d'entraînement des modèles
6. Points clés à retenir

## Personnalisation

Vous pouvez facilement personnaliser les slides en modifiant le fichier `LLM_intro.tex`. Pour ajouter de nouvelles illustrations, modifiez le script `gen_figures.py` et régénérez les figures. 