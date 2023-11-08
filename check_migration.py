from migration_script import app, InvestmentFund, db

# Create an application context
with app.app_context():
    # Check if the data is present in the database
    funds = InvestmentFund.query.all()

    for fund in funds:
        # print(fund)
        # print(
        #         fund.id,
        #         fund.fund_id,
        #         fund.fund_name,
        #         fund.fund_manager,
        #         fund.description,
        #         fund.nav,
        #         fund.creation_date,
        #         fund.performance,
        # )
        print(f"ID: {fund.id}, Fund ID: {fund.fund_id}, Name: {fund.fund_name}")
