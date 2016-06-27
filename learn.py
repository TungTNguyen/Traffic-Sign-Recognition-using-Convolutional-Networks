from sklearn import *
from features import *

def learn (train_data, test_data, features, model):
    train_feats = extract_features(train_data[0], features, verbose=True)
    train_labels = train_data[1]
    test_feats = extract_features(test_data[0], features, verbose=True)
    test_labels = test_data[1]
    model.fit(train_feats, train_labels)
    acc = model.score(test_feats, test_labels)
    print("Score is: %f: " % acc)
    return acc, model