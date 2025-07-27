from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler

class DengueModel:
    @staticmethod
    def treinar_e_testar(X, y):
        # Normalização
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        # Divisão treino/teste
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # KNN com parâmetros otimizados
        modelo = KNeighborsClassifier(
            n_neighbors=3,
            weights='distance',
            metric='manhattan'
        )
        modelo.fit(X_train, y_train)
        y_pred = modelo.predict(X_test)

        matriz = confusion_matrix(y_test, y_pred)
        acuracia = accuracy_score(y_test, y_pred)

        return matriz, acuracia
