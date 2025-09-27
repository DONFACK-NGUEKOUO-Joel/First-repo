import pulp

# 1. Définir le problème (maximisation)
model = pulp.LpProblem("Maximisation_Z", pulp.LpMaximize)

# 2. Définir les variables de décision
x1 = pulp.LpVariable("x2", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("x2", lowBound=0, cat='Integer')

# 3. Fonction objectif
model += x1 + 3 * x2, "Z"

# 4. Contraintes
model += x1 + x2 <= 7
model += -2 * x1 + 3 * x2 <= 6
model += 2 *x1 - x2 <= 6

# 5. Résolution
model.solve()

# 6. Affichage des résultats
print("Status:", pulp.LpStatus[model.status])
print("x1 =", pulp.value(x))
print("x2 =", pulp.value(y))
print("Z =", pulp.value(model.objective))
