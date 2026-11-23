import numpy as np
from scipy.stats import loguniform
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, StratifiedKFold

def gerar(n, semente, ruido=0.1):
    """Pontos nos quatro quadrantes, com uma fração de rótulos trocados."""
    rng = np.random.default_rng(semente)
    X = rng.uniform(-3, 3, (n, 2))
    y = np.where(X[:, 0] * X[:, 1] > 0, 1, -1)
    y[rng.random(n) < ruido] *= -1
    return X, y

X, y = gerar(200, 3)                 # treinamento
X_teste, y_teste = gerar(2000, 4)    # teste, usado uma única vez
cv = StratifiedKFold(5, shuffle=True, random_state=42)

grade = GridSearchCV(SVC(), {"C": [0.01, 0.1, 1, 10, 100, 1000],
                             "gamma": [0.001, 0.01, 0.1, 1, 10, 100]}, cv=cv)
grade.fit(X, y)
print("grade:", grade.best_params_, round(grade.best_score_, 3))

aleat = RandomizedSearchCV(SVC(), {"C": loguniform(1e-2, 1e3),
                                   "gamma": loguniform(1e-3, 1e2)},
                           n_iter=20, cv=cv, random_state=7)
aleat.fit(X, y)
print("aleatória:", {k: round(float(v), 2) for k, v in aleat.best_params_.items()},
      round(aleat.best_score_, 3))
print("teste:", round(grade.score(X_teste, y_teste), 3),
      round(aleat.score(X_teste, y_teste), 3))
