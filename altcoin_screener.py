import requests

def fetch_top_altcoins(limit=10):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "percent_change_24h.desc",
        "per_page": limit,
        "page": 1,
        "sparkline": "false"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        coins = response.json()

        print(f"\n🚀 Топ {limit} альткойнов по росту за 24ч:\n")
        for i, coin in enumerate(coins, start=1):
            name = coin['name']
            symbol = coin['symbol'].upper()
            price = coin['current_price']
            change = coin['price_change_percentage_24h']
            volume = coin['total_volume']

            print(f"{i}. {name} ({symbol})")
            print(f"   💰 Цена: ${price:,.4f}")
            print(f"   📈 Изменение (24ч): {change:.2f}%")
            print(f"   🔊 Объём: ${volume:,.0f}\n")

    except Exception as e:
        print(f"❌ Ошибка при получении данных: {e}")

if __name__ == "__main__":
    fetch_top_altcoins(limit=10)
