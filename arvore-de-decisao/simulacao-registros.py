"""Aula 06 · Árvore de decisão · Ciência de Dados (UPE / dotLAB)
Gera os registros sintéticos usados na página interativa e no material de estudo,
compara árvores de profundidades diferentes e mostra a árvore de profundidade 3."""
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

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

treino = simular(1000, 11)
teste = simular(6000, 99)
X_treino, y_treino = treino.drop(columns="dengue"), treino["dengue"]
X_teste, y_teste = teste.drop(columns="dengue"), teste["dengue"]

for profundidade in [1, 3, 6, None]:
    arvore = DecisionTreeClassifier(
        criterion="entropy", max_depth=profundidade, random_state=42
    )
    arvore.fit(X_treino, y_treino)
    print(f"max_depth={str(profundidade):4}  "
          f"treino={arvore.score(X_treino, y_treino):.3f}  "
          f"teste={arvore.score(X_teste, y_teste):.3f}")

arvore = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42)
arvore.fit(X_treino, y_treino)
print(export_text(arvore, feature_names=list(X_treino.columns), show_weights=True))
nova = pd.DataFrame([{**{s: 0 for s in sinais}, "dor_retro": 1, "febre": 1}])
print(arvore.predict(nova), arvore.predict_proba(nova).round(2))
