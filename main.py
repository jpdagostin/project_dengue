import os
from src.data_loader import DataLoader
from src.processor import Preprocessor
from src.dengue_model import DengueModel

def main():
    # 1. Caminhos
    caminho_entrada = "data/arq_dengue_original.csv"
    caminho_saida = "data/arq_dengue_processado.csv"
    caminho_resultado = "resultado.txt"

    # 2. Carregar os dados
    df = DataLoader.load_data(caminho_entrada)
    if df is None:
        return

    # 3. Processar e salvar nova versão binarizada
    df_bin = Preprocessor.binarizar_sim_nao(df)
    df_bin.to_csv(caminho_saida, index=False)

    # 4. Separar variáveis
    X, y = Preprocessor.separar_variaveis(df_bin)

    # 5. Treinar e avaliar modelo
    matriz, acuracia = DengueModel.treinar_e_testar(X, y)

    # 6. Salvar resultados
    with open(caminho_resultado, "w", encoding="utf-8") as f:
        f.write("📊 Resultados do Modelo KNN para Diagnóstico de Dengue\n")
        f.write("=======================================================\n\n")
        
        f.write("🔹 Primeiros dados transformados (binarizados):\n")
        f.write(df_bin.head().to_string(index=False))
        f.write("\n\n")

        f.write("🔹 Matriz de Confusão:\n")
        for linha in matriz:
            f.write("  " + "  ".join(str(x) for x in linha) + "\n")
        f.write("\n")

        f.write(f"🔹 Acurácia do modelo: {acuracia:.2%}\n")

    print("✅ Processamento completo!")
    print(f"📄 Arquivo processado salvo em: {caminho_saida}")
    print(f"📝 Resultados salvos em: {caminho_resultado}")

if __name__ == "__main__":
    main()
