import pickle
from pandas import DataFrame

class PredictService:
    def __init__(self, model_path = "./src/modules/IA/dist/model.pkl"):
        self.model = pickle.load(open(model_path, 'rb'))

    def predict(self, observation) -> dict:
        df = DataFrame(observation, index=[0])
        return self.model.predict(df).tolist()[0]
