import streamlit as st

# 예시 환율 (실제 데이터는 최신 환율을 사용해야 합니다)
exchange_rates = {
    '중국': 6.5,    # 위안 (CNY)
    '일본': 110.0,  # 엔 (JPY)
    '러시아': 74.0, # 루블 (RUB)
    '대만': 28.0,   # 대만 달러 (TWD)
    '한국': 1400.0  # 원 (KRW)
}

# 나라 이름과 통화 코드 매핑
currency_names = {
    '중국': 'CNY',
    '일본': 'JPY',
    '러시아': 'RUB',
    '대만': 'TWD',
    '한국': 'KRW'
}

# Streamlit 제목
st.title("💱 환율 계산기")

# USD 입력 (1 단위로 증가/감소)
usd_amount = st.number_input("USD로 가격을 입력하세요:", min_value=0.0, step=1.0)

# 나라 선택
selected_country = st.selectbox("환전할 나라를 선택하세요:", list(exchange_rates.keys()))

# 환율 계산
if st.button("계산"):
    if selected_country in exchange_rates:
        converted_amount = usd_amount * exchange_rates[selected_country]
        currency_code = currency_names[selected_country]
        st.success(f"{usd_amount} USD는 {converted_amount:.2f} {currency_code}입니다.")