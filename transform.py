import pandas as pd
import numpy as np
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """


    # Assigning Unique IDs
    
    data.insert(0,'ID', range(1000, 1000 + len(data)))
    data.insert(6,'stat_ID', range(5252, 5252 + len(data)))


    # Filtering below AverageCost

    data = data[data['AverageCost']<1000]


    # Fact dimension modelling

    stats = data[['stat_ID','ID','zomato_reviews','zomato_ratings','Delivery Reviews','AverageCost']]
    restaurant_dimension = data[['ID','Name','Veg','KnownFor','Dining','Full_Address','Area']]

    fact_table = pd.merge(stats, restaurant_dimension, on = 'ID')


    return {'restaurant_dimension':restaurant_dimension.to_dict(orient='dict'),'stats':stats.to_dict(orient='dict')}

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
