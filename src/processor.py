class Preprocessor:
    @staticmethod
    def binarizar_sim_nao(df):
        return df.replace({'sim': 1, 'nao': 0})

    @staticmethod
    def separar_variaveis(df):
        X = df[['febre', 'dor_muscular', 'falta_apetite', 'manchas_vermelhas']]
        y = df['dengue']
        return X, y
