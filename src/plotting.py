import matplotlib.pyplot as plt


def plot_reliability_signal(df, date_col, signal_col, threshold=None):
    """
    Plot rolling reliability signal with optional threshold.
    """
    plt.figure(figsize=(14, 4))
    plt.plot(df[date_col], df[signal_col], label=signal_col)

    if threshold is not None:
        plt.axhline(
            threshold,
            linestyle="--",
            linewidth=1.5,
            label="Guardrail threshold"
        )

    plt.xlabel("Date")
    plt.ylabel("Error")
    plt.title("Rolling Reliability Signal")
    plt.legend()
    plt.tight_layout()


def plot_guardrail_switching(df, date_col, actual_col, primary_col, final_col):
    """
    Plot actual vs forecast with guardrail activation highlighted.
    """
    plt.figure(figsize=(14, 4))

    plt.plot(df[date_col], df[actual_col], label="Actual", linewidth=2)
    plt.plot(df[date_col], df[primary_col], label="Champion", alpha=0.7)
    plt.plot(df[date_col], df[final_col], label="Final (Guardrail)", linewidth=2)

    # Shade guardrail-on periods
    active = df["guardrail_on"].fillna(False).values
    dates = df[date_col].values

    start = None
    for i, on in enumerate(active):
        if on and start is None:
            start = dates[i]
        if (not on or i == len(active) - 1) and start is not None:
            end = dates[i]
            plt.axvspan(start, end, alpha=0.15)
            start = None

    plt.xlabel("Date")
    plt.ylabel("MW")
    plt.title("Guardrail Switching Behaviour")
    plt.legend(ncol=2)
    plt.tight_layout()
