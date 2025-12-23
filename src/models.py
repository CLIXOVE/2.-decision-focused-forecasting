from sklearn.linear_model import Ridge

def train_ridge(X, y, alpha=1.0):
    model = Ridge(alpha=alpha)
    model.fit(X, y)
    return model
