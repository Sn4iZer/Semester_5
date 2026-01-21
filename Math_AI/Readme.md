# Chapitre 3 – Algorithmes Évolutionnaires

Ce document présente une explication claire et détaillée des principaux algorithmes évolutionnaires étudiés en cours, à savoir :
- l’algorithme génétique,
- l’algorithme de colonie de fourmis,
- l’algorithme des abeilles,
- l’algorithme des loups gris.

Chaque algorithme est expliqué **étape par étape**, avec des **exemples simples** pour faciliter la compréhension.

---

## 1. Algorithme Génétique (Genetic Algorithm – GA)

L’algorithme génétique est un algorithme d’optimisation inspiré de la **sélection naturelle** et de l’**évolution biologique**. Il repose sur la reproduction, le croisement et la mutation des solutions.

### Étapes de l’algorithme génétique

#### 1. Initialisation
Une population initiale de solutions (individus) est générée aléatoirement.  
Chaque individu est représenté par un chromosome.

**Exemple :**

```bash
      10101, 01011, 11100, 00110
```

---

#### 2. Évaluation (Fitness)
Chaque individu est évalué à l’aide d’une fonction fitness qui mesure la qualité de la solution.

**Exemple :**
Pour f(x) = x²  
``` bash
x = 21 → f(21) = 441
```

---

#### 3. Sélection
Les individus les plus performants sont sélectionnés pour se reproduire.

**Exemple :**
Les individus avec la meilleure fitness sont choisis comme parents.

---

#### 4. Croisement (Crossover)
Deux parents échangent une partie de leurs chromosomes pour créer de nouveaux individus.

**Exemple :**
``` bash
      Parent 1 : 111|00
      Parent 2 : 101|01
      Enfants : 11101, 10100
```

---

#### 5. Mutation
Une modification aléatoire est appliquée sur un chromosome afin de maintenir la diversité.

**Exemple :**

```bash
      Avant : 11101
      Après : 11001
```

---

#### 6. Remplacement
La nouvelle génération remplace l’ancienne population.

---

#### 7. Critère d’arrêt
L’algorithme s’arrête après un nombre maximal de générations ou lorsque la solution optimale est trouvée.

---

## 2. Algorithme de Colonie de Fourmis (Ant Colony Optimization – ACO)

L’algorithme de colonie de fourmis est inspiré du comportement réel des fourmis pour trouver le **chemin le plus court** entre leur nid et une source de nourriture.

### Étapes de l’algorithme ACO

#### 1. Initialisation
Les fourmis sont placées aléatoirement et les phéromones sont initialisées.

---

#### 2. Construction des solutions
Chaque fourmi construit un chemin en fonction :
- de la quantité de phéromones,
- de la distance entre les nœuds.

---

#### 3. Évaluation
La longueur totale du chemin parcouru par chaque fourmi est calculée.

---

#### 4. Mise à jour des phéromones
- Évaporation des anciennes phéromones.
- Renforcement des chemins les plus courts.

---

#### 5. Répétition
Les étapes sont répétées jusqu’à trouver le meilleur chemin.

---

## 3. Algorithmes des Abeilles et des Loups

### 3.1 Algorithme des Abeilles (Artificial Bee Colony – ABC)

Cet algorithme est inspiré du comportement collectif des abeilles dans la recherche de nourriture.

#### Types d’abeilles
- Abeilles employées
- Abeilles observatrices
- Abeilles éclaireuses

---

### Étapes de l’algorithme ABC

#### 1. Initialisation
Génération aléatoire des sources de nourriture (solutions).

---

#### 2. Abeilles employées
Chaque abeille explore une solution voisine.

---

#### 3. Abeilles observatrices
Elles choisissent les meilleures solutions selon la fitness.

---

#### 4. Abeilles éclaireuses
Les solutions non performantes sont abandonnées et remplacées.

---

#### 5. Arrêt
Lorsque la solution optimale est atteinte ou après un nombre fixé d’itérations.

---

### 3.2 Algorithme des Loups Gris (Grey Wolf Optimizer – GWO)

Inspiré de la hiérarchie sociale et de la stratégie de chasse des loups gris.

#### Hiérarchie
- Alpha (α) : meilleure solution
- Beta (β)
- Delta (δ)
- Omega (ω)

---

### Étapes du GWO

#### 1. Initialisation
Positions aléatoires des loups dans l’espace de recherche.

---

#### 2. Identification des leaders
Sélection des loups α, β et δ.

---

#### 3. Encerclement
Les loups mettent à jour leurs positions en fonction des leaders.

---

#### 4. Attaque
Les solutions convergent progressivement vers l’optimum.

---

#### 5. Critère d’arrêt
Arrêt après convergence ou nombre maximal d’itérations.

---

## Conclusion

Les algorithmes évolutionnaires sont des méthodes puissantes pour résoudre des problèmes complexes d’optimisation.  
Ils sont largement utilisés en intelligence artificielle, en optimisation et en science des données.
