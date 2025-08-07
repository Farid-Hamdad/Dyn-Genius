<!-- docs/formalisme.md -->
# Formalisme Mathématique de DynG
> ⚠️ Ce fichier contient des formules mathématiques en LaTeX. Pour une meilleure lisibilité :
> - Ouvrir avec un lecteur Markdown compatible (Typora, Obsidian, VS Code + extension).
> - Ou consulter le fichier PDF joint.

## 1. Notation générale

| Symbole | Signification |
|---------|---------------|
| $n$ | nombre de concepts |
| $\mathbf{A}\in\mathbb{R}^n$ | vecteur des activations courantes |
| $\mathbf{G}\in\mathbb{R}^n$ | vecteur des objectifs (valeurs désirées) |
| $\boldsymbol{\pi}\in\mathbb{R}_{>0}^n$ | poids de priorité de chaque concept |
| $\mathbf{H}\in\mathbb{R}^{n\times n}$ | matrice hebbienne (connectivité synaptique) |
| $\mathbf{v}\in[-1,1]^n$ | vecteur de valence affective |
| $C\in\mathbb{R}_+$ | niveau global de conscience |
| $\eta,\lambda,\rho,\alpha,\varepsilon$ | hyper-paramètres |

## 2. Fonction de Lyapunov (énergie cognitive)

On définit l’énergie :
$$
E(\mathbf{A}) = \frac{1}{2}(\mathbf{A}-\mathbf{G})^\top \operatorname{diag}(\boldsymbol{\pi})(\mathbf{A}-\mathbf{G})
$$

La dérivée discrète est bornée par :
$$
\Delta E \le -\eta\;(\mathbf{A}-\mathbf{G})^\top\operatorname{diag}(\boldsymbol{\pi})^2(\mathbf{A}-\mathbf{G}) + \lambda\lVert\mathbf{A}-\mathbf{G}\rVert^2
$$
Sous la condition suffisante $\eta\,\pi_{\min}^2 > \lambda$, on garantit $\Delta E < 0$ (convergence exponentielle).

## 3. Mise à jour hebbienne

À chaque pas :
$$
\mathbf{H}_{t+1} = (1-\rho)\,\mathbf{H}_t + \alpha\,\mathbf{A}_t\mathbf{A}_t^\top
$$
- Diagonale mise à zéro : $\mathbf{H}_{ii}=0$  
- Élagage : $\mathbf{H}_{ij}=0$ si $|\mathbf{H}_{ij}| < \varepsilon$

## 4. Descente de gradient cognitive

Gradient par rapport à $\mathbf{A}$ :
$$
\nabla_{\!\mathbf{A}} = 2\,\bigl(\mathbf{A} + \operatorname{diag}(\boldsymbol{\pi})(\mathbf{A}-\mathbf{G})\bigr)
$$
Mise à jour :
$$
\mathbf{A}_{t+1} = \operatorname{clip}\!\Bigl(\mathbf{A}_t - \eta\nabla_{\!\mathbf{A}} + \lambda(\mathbf{A}_t-\mathbf{G}),\ -1,\ 1\Bigr)
$$

## 5. Règles logiques

Fonction `Logic` appliquée composante par composante :
$$
\operatorname{Logic}_i(\mathbf{A}) = \min\!\Bigl(1,\ \max\!\bigl(-1,\ A_i + \sum_{j\in\operatorname{cause}(i)}0.8\,A_j - \sum_{k\in\operatorname{contradiction}(i)}0.3\,A_k\bigr)\Bigr)
$$

## 6. Adaptation métacognitive (MetaModule)

Réglage en ligne :
$$
\eta_{t+1} \leftarrow \eta_t - 0.01\,\frac{\partial E}{\partial \eta},\qquad
\lambda_{t+1} \leftarrow \lambda_t - 0.01\,\frac{\partial E}{\partial \lambda}
$$
Bornes : $\eta\in[0.01,0.5]$, $\lambda\in[0.1,0.8]$.

## 7. Niveau de conscience global

$$
C_t = \boldsymbol{\pi}^\top |\mathbf{A}_t-\mathbf{G}| \odot (1+\mathbf{v})
$$
Une alerte est déclenchée sur le concept $i$ si :
$$
|A_{i,t}-G_i| > \theta(C_t) = 0.3 + 0.2\bigl(1-e^{-C_t}\bigr)
$$

## 8. Phase de rêve (placeholder publique)

État alternatif :
$$
\mathbf{A}_{\text{dream}} = \operatorname{tanh}\!\bigl(\mathbf{H}\,\mathbf{e}_k\bigr)^3
$$
où $\mathbf{e}_k$ est un one-hot aléatoire.

## 9. Conditions suffisantes de stabilité

| Paramètre | Intervalle recommandé | Rôle |
|-----------|-----------------------|------|
| $\eta$ | $0.01 \le \eta \le 0.5$ | taux d’apprentissage |
| $\lambda$ | $0.1 \le \lambda \le 0.8$ | élasticité objectif |
| $\rho$ | $0.01 \le \rho \le 0.1$ | oubli hebbien |
| $\alpha$ | $0.1 \le \alpha \le 0.5$ | force hebbienne |
| $\varepsilon$ | $10^{-4} \le \varepsilon \le 10^{-2}$ | élagage |

Sous ces bornes et avec $\eta\pi_{\min}^2 > \lambda$, DynG converge vers un équilibre unique.

## 10. Références
- Dehaene, S. *Consciousness and the Brain*, 2014  
- Hamdad, F. *DynG – Formal Stability Report*, 2025 
