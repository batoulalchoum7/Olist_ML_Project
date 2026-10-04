import pandas as pd
import great_expectations as gx

from src.gx_validation import create_expectation_suite


def test_gx_expectation_suite():
    df = pd.DataFrame([{
        "purchase_hour": 10,
        "purchase_day_of_week": 2,
        "purchase_month": 5,
        "purchase_year": 2018,
        "approval_delay_hours": 1.5,
        "estimated_delivery_days": 20,
    }])

    context = gx.get_context()
    suite = create_expectation_suite(context)

    datasource = context.data_sources.add_pandas("olist_data_source")
    asset = datasource.add_dataframe_asset("orders")
    batch_definition = asset.add_batch_definition_whole_dataframe("orders_batch")

    validation_definition = gx.ValidationDefinition(
        data=batch_definition,
        suite=suite,
        name="olist_validation"
    )

    context.validation_definitions.add(validation_definition)

    result = validation_definition.run(
        batch_parameters={"dataframe": df}
    )

    assert result.success