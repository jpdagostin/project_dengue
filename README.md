# 🤖 Projeto de Classificação de Casos de Dengue com KNN

Este projeto implementa um pipeline completo de **Mineração de Dados** para **diagnóstico de dengue** usando o algoritmo `KNeighborsClassifier` (KNN). A base contém sintomas e diagnósticos, e é processada para treinar um modelo de machine learning.

---

## 📁 Estrutura do Projeto

```
projeto_dengue/
├── main.py
├── requirements.txt
├── README.md
├── resultado.txt
│
├── data/
│   ├── arq_dengue_original.csv      ← base original (não é alterada)
│   └── arq_dengue_processado.csv    ← gerado automaticamente
│
└── src/
    ├── __init__.py
    ├── data_loader.py
    ├── processor.py
    └── dengue_model.py
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório (ou copie os arquivos)

```bash
git clone https://github.com/seuusuario/projeto_dengue.git
cd projeto_dengue
```

### 2. Crie o ambiente virtual

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

No Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Adicione a base de dados

Salve sua base original como:

```
data/arq_dengue_original.csv
```

> Formato esperado:
> Colunas: `paciente`, `febre`, `dor_muscular`, `falta_apetite`, `manchas_verme`, `dengue`  
> Valores: `sim` ou `nao` para sintomas e diagnóstico.

---

## ▶️ Como rodar o projeto

```bash
python main.py
```

---

## 📦 O que será gerado

- `data/arq_dengue_processado.csv`: versão binarizada da base (`sim` → 1, `nao` → 0)
- `resultado.txt`: arquivo com:
  - Primeiros dados transformados
  - Matriz de confusão
  - Acurácia do modelo

---

## 🧠 Explicação do código

### `main.py`

Controla todo o fluxo:

1. Lê o arquivo original
2. Binariza os dados
3. Salva uma cópia nova da base
4. Separa os dados em `X` e `y`
5. Treina e avalia o modelo
6. Salva os resultados no arquivo `resultado.txt`

---

### `src/data_loader.py`

```python
class DataLoader:
    @staticmethod
    def load_data(filepath)
```

- Carrega o arquivo CSV original.
- Se não encontrar o arquivo, retorna `None`.

---

### `src/processor.py`

```python
class Preprocessor:
    @staticmethod
    def binarizar_sim_nao(df)
    @staticmethod
    def separar_variaveis(df)
```

- Converte os valores `sim`/`nao` para `1`/`0`.
- Separa as variáveis independentes (`X`) e o alvo (`y`).

---

### `src/dengue_model.py`

```python
class DengueModel:
    @staticmethod
    def treinar_e_testar(X, y)
```

- Usa o algoritmo KNN (`KNeighborsClassifier`).
- Divide os dados em treino/teste.
- Retorna a matriz de confusão e a acurácia do modelo.

---

## 📚 Requisitos

- Python 3.8+
- `pandas`
- `scikit-learn`
- `numpy`

Instalados automaticamente via `requirements.txt`.

---

## 📬 Dúvidas?

Abra uma issue ou envie uma mensagem!

---
