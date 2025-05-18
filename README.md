# Crypto Arbitrage Tracker

**Crypto Arbitrage Tracker** is a powerful Python-based tool that monitors **real-time price data of 69 ERC-20 tokens** across **9 centralized and decentralized exchanges**. It analyzes price discrepancies and helps uncover **arbitrage opportunities** in the crypto markets. The project is modular, scalable, and has the **potential to integrate Flash Loans and Flash Swaps** for fully automated arbitrage execution.

---

## ⚙️ Key Features

* 🔄 **69 ERC-20 Tokens** supported
* 🌐 **Multi-Exchange Integration**:

  * **Centralized Exchanges**:

    * Binance
    * Bitfinex
    * Bitvavo
    * Coinbase
    * LBank
  * **Decentralized Exchanges**:

    * PancakeSwap
    * Uniswap
    * SushiSwap
    * DODO
    * dYdX
* ⚖️ **Arbitrage Opportunity Detection**:

  * Compares live token prices across all exchanges
  * Shows best arbitrage opportunities and profit spreads
* 🧠 **Modular Design**:

  * Each exchange handled via separate script
  * Easy to add new tokens or exchanges
* 🚀 **Flash Loan/Swap Ready (Future Scope)**:

  * Can be extended to execute trades automatically using:

    * Aave Flash Loans
    * Uniswap Flash Swaps

---

## 📂 Project Structure

```
Crypto-Arbitrage-Tracker/
├── gamma_app.py                # Main script to run arbitrage tracker
├── FrontRunnigBot.py           # Prototype front-running bot (simulated)
├── [exchange]_price.py         # Individual scripts for each exchange
│   ├── binance_price.py
│   ├── coinbase_price.py
│   ├── bitvavo_price.py
│   ├── bitfinex_price.py
│   ├── bybit_price.py
│   ├── pancake_price.py
│   ├── sushiswap_price.py
│   ├── dodo_price.py
│   └── dydx_price.py
├── contracts/
│   ├── ERC20Abi.json
│   └── UniswapAbi.json
├── arbitrage_data.csv          # Sample data log
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 🧰 Prerequisites

* Python 3.8 or later
* Git
* Internet access (for live exchange APIs)

### 🔧 Installation

```bash
git clone https://github.com/Suryanshu01/Crypto-Arbitrage-Tracker.git
cd Crypto-Arbitrage-Tracker
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Usage

To run the arbitrage tracker:

```bash
python gamma_app.py
```

This will:

* Fetch prices of 69 ERC-20 tokens from all integrated exchanges
* Compare them for arbitrage opportunities
* Display the most profitable arbitrage path (if any)

---

## 🔮 Future Enhancements

* 💰 **Flash Loan / Flash Swap Integration** for:

  * Zero upfront capital arbitrage
  * Atomic execution of multi-hop trades
* 📉 **Real-time Graphs & Dashboard** using Plotly or Dash
* 📦 **Export Arbitrage Logs to JSON / CSV**
* 🛠️ **CLI Tool** to generate Merkle Proofs for token sets

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit: `git commit -m "Add feature"`
4. Push: `git push origin feature/my-feature`
5. Submit a PR

---

## 📜 License

[MIT License](LICENSE)

---

## 👨‍💻 Author

[Suryanshu01](https://github.com/Suryanshu01)
