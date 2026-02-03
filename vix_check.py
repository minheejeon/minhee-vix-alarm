import os
import yfinance as yf
import requests

# 1. 정보를 가져오고 출력해보기 (로그 확인용)
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def get_investment_advice():
    # 토큰이 비어있는지 체크
    if not TOKEN or not CHAT_ID:
        print(f"❌ 에러: Secrets를 불러오지 못했습니다. TOKEN 존재여부: {bool(TOKEN)}, ID 존재여부: {bool(CHAT_ID)}")
        return

    vix = yf.Ticker("^VIX").history(period="1d")['Close'].iloc[-1]
    qqq = yf.Ticker("QQQ").history(period="1d")['Close'].iloc[-1]
    
    status = "😱 역대급 공포" if vix >= 30 else "😰 불안한 변동성" if vix >= 20 else "😊 평온한 상승"
    advice = "과감하게 매수!" if vix >= 30 else "정해진 금액만 사자." if vix >= 20 else "무리하지 말기!"

    message = f"🔔 민희의 투자 알람\n\n📊 나스닥: ${qqq:.2f}\n📉 공포지수: {vix:.2f}\n\n🚩 {status}\n💡 {advice}"
    
    # f-string 안에서 bot 글자 뒤에 토큰이 바로 붙는지 확인
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': message}
    
    response = requests.get(url, params=params)
    print(f"✅ 전송 시도! 결과 코드: {response.status_code}")

if __name__ == "__main__":
    get_investment_advice()
