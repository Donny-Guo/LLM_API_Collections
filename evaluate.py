from sklearn.metrics import classification_report
import pandas as pd

def evaluate(filename):
    if '.csv' in filename:
        df = pd.read_csv(filename)
    elif '.json' in filename:
        df = pd.read_json(filename, orient='records')
    else:
        return "Format not supported in evaluation"
    
    y_pred = df['Model Output'].tolist()  # your predicted values
    y = df['Answer'].tolist()  # your true values
    target_names = ['class 0', 'class 1']
    print("Classification report: ")
    report = classification_report(y_true=y, y_pred=y_pred, target_names=target_names)
    print(report)
    return report

    

if __name__ == "__main__":
    evaluate("output/perplexity-llama-3.1-8b-result.csv")