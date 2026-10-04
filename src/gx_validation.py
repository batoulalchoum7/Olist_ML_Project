import great_expectations as gx


def create_expectation_suite(context):
    suite = gx.ExpectationSuite(
        name="olist_order_validation"
    )

    # Add the suite to the Data Context first
    context.suites.add(suite)

    expectations = [
        gx.expectations.ExpectColumnToExist(
            column="purchase_hour"
        ),
        gx.expectations.ExpectColumnToExist(
            column="purchase_day_of_week"
        ),
        gx.expectations.ExpectColumnToExist(
            column="purchase_month"
        ),
        gx.expectations.ExpectColumnToExist(
            column="purchase_year"
        ),
        gx.expectations.ExpectColumnToExist(
            column="approval_delay_hours"
        ),
        gx.expectations.ExpectColumnToExist(
            column="estimated_delivery_days"
        ),
        gx.expectations.ExpectColumnValuesToNotBeNull(
            column="purchase_hour"
        ),
        gx.expectations.ExpectColumnValuesToBeBetween(
            column="purchase_hour",
            min_value=0,
            max_value=23
        ),
        gx.expectations.ExpectColumnValuesToBeBetween(
            column="purchase_day_of_week",
            min_value=0,
            max_value=6
        ),
        gx.expectations.ExpectColumnValuesToBeBetween(
            column="purchase_month",
            min_value=1,
            max_value=12
        ),
        gx.expectations.ExpectColumnValuesToBeBetween(
            column="purchase_year",
            min_value=2017,
            max_value=2030
        ),
        gx.expectations.ExpectColumnValuesToBeBetween(
            column="approval_delay_hours",
            min_value=0
        ),
        gx.expectations.ExpectColumnValuesToBeBetween(
            column="estimated_delivery_days",
            min_value=0
        ),
    ]

    for expectation in expectations:
        suite.add_expectation(expectation)

    return suite
