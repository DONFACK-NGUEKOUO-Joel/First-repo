import pulp

# Coefficients de l'objectif (profit)
c = [40, 30]

# Matrice des contraintes (temps machine)
A = [[2, 1],
     [1, 2]]

# Ressources disponibles
b = [100, 80]

# Variables de décision    / rang(2): defini le nbre de variable a creer
x = [pulp.LpVariable(f"x{i+1}", lowBound=0, cat='Continuous') for i in range(2)]

# Définir le problème (maximisation)
model = pulp.LpProblem("Maximisation_Profit", pulp.LpMaximize)

# Fonction objectif
model += pulp.lpSum([c[i]*x[i] for i in range(2)]), "Profit_total"

# Contraintes
for i in range(len(b)):
    model += pulp.lpSum([A[i][j]*x[j] for j in range(2)]) <= b[i], f"Contrainte_{i+1}"

# Résolution
model.solve()

# Résultats
print("Status:", pulp.LpStatus[model.status])
for i, var in enumerate(x):
    print(f"x{i+1} =", pulp.value(var))
print("Profit maximal =", pulp.value(model.objective))
