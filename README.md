# About

Finds theoretical put-call pricing based on 5 assumptions for a stock:
- S: spot price
- K: strike price
- T: time to expiry (in years)
- r: risk-free rate
- sigma: expected volatility

Used [Barchart](https://www.barchart.com/) for "S", "K", "T", "sigma", [treasury.gov](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates&field_tdr_date_value=2026) for "r".

The Coupon Equivalent Yield (CEY), also known as the Bond Equivalent Yield (BEY), is the annualized return for discount or short-term, non-interest-bearing bonds. This is your "r".

### Parameters
<img width="388" height="156" alt="Screenshot 2026-03-21 at 10 04 31 PM" src="https://github.com/user-attachments/assets/fedde0dc-e1f5-4f1e-8efd-09e1b43005b5" />

The difference between a 4-week and 6-month rate is usually small enough that it barely moves output. You can instead opt to use the 3-month T-Bill rate found here: https://fred.stlouisfed.org/series/DGS3MO.

Much of the options flow is comprised of short-dated (30-90 days) contracts. Liquidity matters, and so in practice, most people use the 3-Month T-Bill.

If you are pricing LEAPS, swap the 3-month for the apporpriate maturity.

### Why use T-Bills/Notes as "r"?

Backed by full faith and credit of the U.S. government, there is virtually zero default or credit risk.

So why not T-Bonds?

The Black-Scholes discounts future cash flows back to PV using e^(-rT). The rate NEEDS to reflect what you could theoretically earn risk-free over the same period as your contract expiration (i.e., a 30-day call should use a 30-day rate, not a 30 year rate).
