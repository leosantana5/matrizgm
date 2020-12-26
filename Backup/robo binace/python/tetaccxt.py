import ccxt
print('CCXT version:', ccxt.__version__)  # requires CCXT version > 1.20.31
exchange = ccxt.binance({
    'apiKey': '56OhgEi35UbkDYdvftOtst4641MxI5O6SiY4sB0ZagbdFc9XrqW0200TatbEpuFe',
    'secret': 'PLE3XYirbpNEzTTJ1tnXAoFmuFmcz160yBnfNA3zyDdnklZkU8IZ9O6I6NQ3OwF5',
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future',  # ←-------------- quotes and 'future'
    },
})

exchange.load_markets()

# exchange.verbose = True  # uncomment this line if it doesn't work

# your code here...