from pandas import read_csv
import json

df = read_csv("./src/modules/IA/dist/test.csv")

def getSample():
    sample = df.sample(1)
    return json.dumps(sample.drop(columns=['class_good', 'class_bad']).to_dict(orient='records')[0]), sample['class_good'].iloc[0]

if __name__ == "__main__":
    print("\n\nSample:\n")
    print(getSample()[0])
    print("\n\n\n\nTarget real:\n")
    print(getSample()[1])