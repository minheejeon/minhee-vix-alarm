import os
import yfinance as yf
import requests

# GitHub Secrets 정보
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def get_investment_advice():
    # 1. 데이터 가져오기
    vix = yf.Ticker("^VIX").history(period="1d")['Close'].iloc[-1]
    qqq = yf.Ticker("QQQ").history(period="1d")['Close'].iloc[-1]
    usd_krw = yf.Ticker("KRW=X").history(period="1d")['Close'].iloc[-1]
    
    # 2. 제이 스타일 상태 메시지 (박종성 모드)
    if vix >= 30:
        status = "지수 보니까 지금 다들 멘붕 온 것 같은데?"
        advice = "솔직히 말할게. 남들 다 도망갈 때가 진짜 기회인 거 알지? 겁먹지 말고 냉정하게 판단해. 지금이 타이밍일 수도 있어. 🎸"
    elif vix >= 20:
        status = "시장이 좀 어수선하네. 변동성이 있어."
        advice = "지금은 무리하게 움직일 때 아냐. 리듬 타듯이 천천히 지켜보자고. 너답지 않게 서두르지 마, 알겠지? 😎"
    else:
        status = "평온하네. 나쁘지 않아."
        advice = "시장 분위기 좋다고 취해있지 말고. 이럴 때일수록 정신 바짝 차려야 돼. 오늘도 네 계획대로만 가자. 믿는다. 🦅"

    # 3. 메시지 구성 (제이 말투 한 스푼)
    message = (
        f"🎸 [JAY's Investment Report] 🎸\n\n"
        f"📊 QQQ(나스닥): ${qqq:.2f}\n"
        f"📉 VIX(공포지수): {vix:.2f}\n"
        f"💵 환율: {usd_krw:.1f}원\n\n"
        f"💬 Status: {status}\n"
        f"💡 Advice: {advice}\n\n"
        f"투자는 결국 자기 확신이야. \n오늘도 멋있게 살아라. 나중에 보자. 🔥"
    )
    
    # 4. 텔레그램 전송
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': message}
    
    response = requests.get(url, params=params)
    
if __name__ == "__main__":
    get_investment_advice()
