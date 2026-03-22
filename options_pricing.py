import math

def black_scholes(S, K, T, r, sigma, option_type='call'):
    # S = stock price, K = strike price, T = time to expiry (in years)
    # r = risk-free rate (Treasurey CEY, decimal)
    # sigma = volatility (annualized standard deviation of returns, decimal)

    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    def norm_cdf(x):
        return (1.0 + math.erf(x / math.sqrt(2))) / 2

    if option_type == 'call':
        price = S * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    else:
        price = K * math.exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)

    return price

# Inputs hardcoded (default values from 3/20/2026 market close)
S = 648.57          # Current price (e.g., SPY closing price)
K = 648             # At or near-the-money strike
T = 4 / 365         # (DTE / 365) to convert to years
r = 0.0368          # Use treasury rate according to DTE (e.g. 4 DTE = 4 week tranche, CEY @ 3.68%)
sigma = 0.2827      # IV for contract

call = black_scholes(S, K, T, r, sigma, 'call')
put  = black_scholes(S, K, T, r, sigma, 'put')

print(f"Call price: ${call:.2f}")
print(f"Put price:  ${put:.2f}")