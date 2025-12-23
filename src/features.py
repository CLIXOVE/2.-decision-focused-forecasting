def add_lags(df, target_col="demand", lags=(1, 7)):
    d = df.copy()
    for l in lags:
        d[f"lag_{l}"] = d[target_col].shift(l)
    return d.dropna().reset_index(drop=True)
