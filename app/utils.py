def generate_risk_explanation(probability):

    if probability >= 0.75:
        return (
            "Very low engagement and behavioral signals indicate high churn risk."
        )

    elif probability >= 0.50:
        return (
            "Customer shows moderate churn indicators."
        )

    return (
        "Customer currently demonstrates healthy engagement."
    )


def get_risk_level(probability):

    if probability >= 0.75:
        return "high"

    elif probability >= 0.50:
        return "medium"

    return "low"
