import pandas as pd


def find_best_sellers_list(
    df_actions: pd.DataFrame,
    df_cart: pd.DataFrame,
    experiment_name: str,
    brand: bool = False,
) -> list:
    """
    Function returns list of best sellers in decreasing order by buying rate.

    Args:
        df_actions (pandas.DataFrame): Filtered users actions DataFrame,
        df_cart (pandas.DataFrame): Filtered users cart DataFrame,
        experiment_name (str): String with experiment name.
        brand (bool): If True list of brands compile

    Returns:
        best_seller_order (list): list of product ids in decreasing order by buying rate
    """

    uids_buying = (
        df_actions[
            (df_actions["action"] == "reached")
            & (df_actions["page_type"] == "checkout")
            & (df_actions["experiment_name"] == experiment_name)
        ]
        .uid.unique()
        .tolist()
    )

    if brand:
        grouped_df = (
            df_cart[df_cart["uid"].isin(uids_buying)]
            .groupby(["brand"])
            .agg({"uid": "nunique"})
            .sort_values(by="uid", ascending=False)
        )

    else:
        grouped_df = (
            df_cart[df_cart["uid"].isin(uids_buying)]
            .groupby(["product_id"])
            .agg({"uid": "nunique"})
            .sort_values(by="uid", ascending=False)
        )

    return grouped_df.index.tolist()