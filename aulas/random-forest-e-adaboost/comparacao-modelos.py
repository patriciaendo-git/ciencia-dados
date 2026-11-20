import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

# Mesma simulação da Aula 06

# Frequência de cada sinal entre casos de dengue e casos descartados
# (Tabela 6 de da Silva Neto et al., 2022)
sinais = {
    "febre":       (0.398, 0.378),
    "mialgia":     (0.370, 0.330),
    "cefaleia":    (0.374, 0.340),
    "exantema":    (0.108, 0.073),
    "vomito":      (0.102, 0.093),
    "nausea":      (0.160, 0.127),
    "dor_costas":  (0.127, 0.099),
    "conjuntivite":(0.015, 0.012),
    "artrite":     (0.050, 0.035),
    "artralgia":   (0.105, 0.088),
    "petequias":   (0.043, 0.028),
    "prova_laco":  (0.023, 0.011),
    "dor_retro":   (0.170, 0.110),
    "leucopenia":  (0.025, 0.013),
}

def simular(n, semente):
    """Sorteia n registros, metade de cada classe, cada sinal de forma independente."""
    rng = np.random.default_rng(semente)
    dengue = np.tile([1, 0], n // 2)          # amostra balanceada
    p_dengue = np.array([p for p, _ in sinais.values()])
    p_outro = np.array([q for _, q in sinais.values()])
    p = np.where(dengue[:, None] == 1, p_dengue, p_outro)
    registros = pd.DataFrame((rng.random((n, len(sinais))) < p).astype(int),
                             columns=list(sinais))
    registros["dengue"] = dengue
    return registros

treino = simular(4000, 11)
teste = simular(6000, 99)
X_treino, y_treino = treino.drop(columns="dengue"), treino["dengue"]
X_teste, y_teste = teste.drop(columns="dengue"), teste["dengue"]

modelos = {
    "árvore sem limite": DecisionTreeClassifier(random_state=42),
    "Random Forest":     RandomForestClassifier(
        n_estimators=200, max_features="sqrt", oob_score=True, random_state=42),
    "AdaBoost":          AdaBoostClassifier(n_estimators=200, random_state=42),
}
for nome, modelo in modelos.items():
    modelo.fit(X_treino, y_treino)
    print(f"{nome:18} treino={modelo.score(X_treino, y_treino):.3f}  "
          f"teste={modelo.score(X_teste, y_teste):.3f}")
print(f"Random Forest, acurácia out-of-bag: {modelos['Random Forest'].oob_score_:.3f}")
