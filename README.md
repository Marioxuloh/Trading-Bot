# TRADING-BOT

Este repositorio contiene el codigo de un bot de trading que da consejos de operaciones basandose en los datos de yfinance y de un periodo de tiempo que tu quieras darle.

## Archivos Principales

- **launcher.py**: Launcher de la aplicacion, donde se obtienen los datos y posteriormente se llamara a los otros modulos para su analisis.

- **financial_analysis.py**: analisis financiero basico de avg volume, current daily returns y daily returns.

- **moving_averages.py**: analisis financiero basico sobre EMA, SMA y golden&death crosses.

- **trading_bot.py**: bot que analiza toda la informacion anteriormente procesada y da un consejo sobre una posible operacion a realizar sobre cada asset.

- **scope.txt**: una lista de nombres sobre los diferentes assets que quieras analizar.