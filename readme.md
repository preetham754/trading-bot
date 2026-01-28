# Binance Futures Testnet Trading Bot

A simple Python CLI application to place Market and Limit orders on Binance Futures Testnet.

## Setup

1. Create Binance Futures Testnet account  
2. Generate API Key and Secret  

Set environment variables:

Linux/Mac:
export BINANCE_API_KEY=your_key
export BINANCE_API_SECRET=your_secret

Windows:
set BINANCE_API_KEY=your_key
set BINANCE_API_SECRET=your_secret

## Install

pip install -r requirements.txt

## Run Examples

Market order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000

## Logs

All API requests and responses are logged in:

logs/bot.log
