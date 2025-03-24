import matplotlib.pyplot as plt
import numpy as np
import os

# Créer le dossier figures s'il n'existe pas
if not os.path.exists('figures'):
    os.makedirs('figures')

# Simulation de l'évolution de l'erreur pendant l'entraînement
def generate_training_curve():
    epochs = np.arange(1, 101)
    
    # Erreur d'entraînement (diminue progressivement avec du bruit)
    train_error = 0.5 * np.exp(-0.03 * epochs) + 0.1 + 0.05 * np.random.randn(100)
    train_error = np.clip(train_error, 0.05, 1.0)
    
    # Erreur de validation (diminue puis remonte - overfitting)
    val_error = 0.45 * np.exp(-0.02 * epochs) + 0.2 + 0.02 * np.sin(epochs/5) + 0.05 * np.random.randn(100)
    val_error = np.clip(val_error, 0.15, 1.0)
    
    # Point d'arrêt optimal (early stopping)
    optimal_point = 55
    
    # Créer le graphique
    plt.figure(figsize=(10, 6))
    plt.plot(epochs, train_error, 'b-', linewidth=2, label="Erreur d'entraînement")
    plt.plot(epochs, val_error, 'r-', linewidth=2, label="Erreur de validation")
    plt.axvline(x=optimal_point, color='g', linestyle='--', label="Point d'arrêt optimal")
    
    plt.xlabel("Époques d'entraînement", fontsize=12)
    plt.ylabel("Erreur", fontsize=12)
    plt.title("Évolution de l'erreur pendant l'entraînement d'un modèle", fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    # Annoter les zones
    plt.annotate("Sous-apprentissage", xy=(10, 0.4), xytext=(5, 0.6),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
    
    plt.annotate("Sur-apprentissage\n(overfitting)", xy=(85, 0.3), xytext=(70, 0.5),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
    
    plt.tight_layout()
    plt.savefig('figures/training_curve.png', dpi=300)
    plt.close()

# Génération d'un schéma simple de modèle transformant une entrée en sortie
def generate_model_diagram():
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Cacher les axes
    ax.axis('off')
    
    # Dessiner les boîtes
    input_box = plt.Rectangle((0.1, 0.4), 0.2, 0.2, fill=True, color='lightblue', alpha=0.7)
    model_box = plt.Rectangle((0.4, 0.3), 0.2, 0.4, fill=True, color='lightcoral', alpha=0.7)
    output_box = plt.Rectangle((0.7, 0.4), 0.2, 0.2, fill=True, color='lightgreen', alpha=0.7)
    
    ax.add_patch(input_box)
    ax.add_patch(model_box)
    ax.add_patch(output_box)
    
    # Ajouter les flèches
    ax.arrow(0.3, 0.5, 0.09, 0, head_width=0.03, head_length=0.02, fc='black', ec='black')
    ax.arrow(0.6, 0.5, 0.09, 0, head_width=0.03, head_length=0.02, fc='black', ec='black')
    
    # Ajouter les étiquettes
    ax.text(0.2, 0.5, "Entrée", ha='center', va='center', fontsize=12)
    ax.text(0.5, 0.5, "Modèle", ha='center', va='center', fontsize=12)
    ax.text(0.8, 0.5, "Sortie", ha='center', va='center', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('figures/model_diagram.png', dpi=300)
    plt.close()

if __name__ == "__main__":
    generate_training_curve()
    generate_model_diagram()
    print("Images générées avec succès dans le dossier 'figures/'") 