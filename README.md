### Limitations/Assumptions

This implementation of Black-Schoels assumes: European-style exercise, constant volatility, and no dividends (unless explicitly adjusted). 

This model is not intended to perfectly replicate market prices, and can misprice short-dated options where event risk is significant. 

Observed option prices reflect several factors not caputred by Black-Scholes:
- Supply/demand dynamics
- Volatility skew (strike-dependent IV)
- Term structure of volatility across maturities
- Liquidity conditions in the options market

# About

Finds theoretical put-call pricing based on 5 assumptions for a stock:
- S: spot price
- K: strike price
- T: time to expiry (in years)
- r: risk-free rate
- sigma: expected volatility

Used [Barchart](https://www.barchart.com/) for "S", "K", "T", "sigma", [treasury.gov](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates&field_tdr_date_value=2026) for "r".

The Coupon Equivalent Yield (CEY), also known as the Bond Equivalent Yield (BEY), is the annualized return for discount or short-term, non-interest-bearing bonds. This is your "r".

For this model (version 1), I used the closest strike relative to SPY's price as of 3/20/26 as an example. Going forward for future projects, I would find a delta 0.50 strike to use "true" ATM.

### Parameters
<img width="416" height="184" alt="Screenshot 2026-03-25 at 4 13 30 AM" src="https://github.com/user-attachments/assets/b28d1a54-6414-47e6-a501-7fc7d9e86cd3" />

The difference between a 4-week and 6-month rate is usually small enough that it barely moves output. You can instead opt to use the 3-month T-Bill rate found here: https://fred.stlouisfed.org/series/DGS3MO.

Much of the options flow is comprised of short-dated (30-90 days) contracts. Liquidity matters, and so in practice, most people use the 3-Month T-Bill.

If you are pricing LEAPS, swap the 3-month for the appropriate maturity.

### Why Use T-Bills/Notes as "r"?

Backed by full faith and credit of the U.S. government, there is virtually zero default or credit risk.

So why didn't I use T-Bonds?

The Black-Scholes discounts future cash flows back to PV using e^(-rT). The rate *needs* to reflect what you could theoretically earn risk-free over the same period as your contract expiration (i.e., a 30-day contract should use a 30-day rate, not a 30 year rate).

### The Math
![ezgif-89ccf0feb6f98d9d](https://github.com/user-attachments/assets/187b24bc-271b-4d3a-884d-607ad83dfecb)

BS uses continuous compounding. n = the number of compounding periods.  When taken to the limit, (1+r/n)^n as n → ∞, it converges to e^r.

