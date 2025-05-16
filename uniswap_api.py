from uniswap_testing import get_uniswap_price_v2
from uni_token_analysis import tokens5
from fastapi import FastAPI, Request, HTTPException


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "User"}


@app.get("/prices/{token_a}/{token_b}")
def get_prices(token_a: str, token_b: str):
    prices = get_uniswap_price_v2(None, tokens5[token_a.upper()], tokens5[token_b.upper()], None)
    if prices ==0:
        raise HTTPException(status_code=404)
    else:
        return prices