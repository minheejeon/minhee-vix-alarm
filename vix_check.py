import yfinance as yf
import requests

# 1. 민희의 고유 정보 설정
TOKEN = "8273447953:AAHeFjOFMRItCviCYAuBcrmUiVuXt3M3Vak"
CHAT_ID = "8442620600"

def get_investment_advice():
    # 데이터 가져오기 (VIX: 공포지수, QQQ: 나스닥100 ETF)
    vix = yf.Ticker("^VIX").history(period="1d")['Close'].iloc[-1]
    qqq = yf.Ticker("QQQ").history(period="1d")['Close'].iloc[-1]
    
    # 지수 상태 판단 로직
    if vix >= 30:
        status = "😱 역대급 공포 구간 (매수 기회!)"
        advice = "시장이 패닉이야. 적립식 금액보다 조금 더 과감하게 사보는 건 어때?"
    elif vix >= 20:
        status = "😰 불안한 변동성 구간"
        advice = "시장이 출렁거려. 욕심부리지 말고 정해진 금액만 차분히 사자."
    else:
        status = "😊 평온한 상승 구간"
        advice = "다들 낙관적이야. 무리하게 추격 매수하지 말고 원래 계획대로만 해!"

    # 메시지 구성
    message = (
        f"🔔 민희의 모닝 투자 알람\n\n"
        f"📊 나스닥(QQQ): ${qqq:.2f}\n"
        f"📉 공포지수(VIX): {vix:.2f}\n\n"
        f"🚩 현재 상태: {status}\n"
        f"💡 조언: {advice}"
    )
    
    # 텔레그램으로 전송
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url)

# 실행
if __name__ == "__main__":
    get_investment_advice()