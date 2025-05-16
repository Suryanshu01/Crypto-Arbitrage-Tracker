# Crypto Arbitrage Tracker

**Crypto Arbitrage Tracker** is a Python-based tool that monitors cryptocurrency prices across centralized and decentralized exchanges to identify real-time arbitrage opportunities. It helps traders spot and act on price discrepancies across platforms.

## Features

* 🏦 **Multi-Exchange Integration**: Supports Binance, Coinbase, Bitfinex, Bybit, Bitvavo, DODO, DYDX, Balancer, and more.
* 📡 **Live Price Tracking**: Fetches and compares token prices from multiple sources.
* ⚡ **Arbitrage Opportunity Detection**: Calculates price spreads to find profitable arbitrage paths.
* 🤖 **Front-Running Simulation**: Includes a basic front-running bot logic for testing.
* 🔌 **Modular Codebase**: Easy to extend with new exchanges or algorithms.

## Getting Started

### Prerequisites

* Python 3.8 or higher
* Git (for cloning)
* Internet connection (for API calls)

### Installation

```bash
git clone https://github.com/Suryanshu01/Crypto-Arbitrage-Tracker.git
cd Crypto-Arbitrage-Tracker
python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate
pip install -r requirements.txt
```

### Usage

To run the arbitrage tracker:

```bash
python gamma_app.py
```

> This is the main entry point and uses all exchange modules to fetch live prices and display arbitrage opportunities.

## Project Structure

```
Crypto-Arbitrage-Tracker/
├── gamma_app.py              # Main runner script
├── FrontRunnigBot.py         # Front-running bot prototype
├── [exchange]_price.py       # Price fetchers for each exchange
├── contracts/                # Smart contract ABIs (Uniswap, ERC20)
├── arbitrage_data.csv        # Sample data file
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
└── ... (other utility files)
```

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add feature"`
4. Push and open a PR

## License

[MIT](LICENSE)

## Author

[Suryanshu01](https://github.com/Suryanshu01)

---

Let me know if you want badges (e.g., Python version, license), screenshots, or a sample terminal output added.

