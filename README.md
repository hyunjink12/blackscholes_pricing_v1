# About

Finds theoretical put-call pricing based on 5 assumptions for a stock:
- S: spot price
- K: strike price
- T: time to expiry (in years)
- r: risk-free rate
- sigma: expected volatility

Used [Barchart](https://www.barchart.com/) for "S, K, T, sigma".
Used [treasury.gov](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates&field_tdr_date_value=2026) for "r".

# Parameters

### EXPIRATION            MATURITY TRANCHE
0-4 weeks             4 week T-Bill
1-3 months            3-month T-Bill
3-6 months            6-month T-Bill
6-12 months           1-year T-Bill
1-2 years             2-year T-Note
2+ years (LEAPS)      5 or 10 year T-Note
