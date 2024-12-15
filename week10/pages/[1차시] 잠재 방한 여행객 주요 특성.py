import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib import rc

rc('font', family='Malgun Gothic')  # Windows: "맑은 고딕 사용"

plt.rcParams['axes.unicode_minus'] = False



excel_file = '24-2 목요일 과제 데이터.xlsx'
xls = pd.ExcelFile(excel_file)


sheet_names = xls.sheet_names


st.title('📈 잠재 방한 여행객의 주요 특성을 알아보자')

st.markdown("---")

st.write("1️⃣ 잠재 방한 여행객의 주요 특성을 알아봅시다.")
selected_sheet = st.selectbox("아래 버튼을 클릭하여 알고 싶은 특성을 선택하세요:", sheet_names)

df = pd.read_excel(xls, sheet_name=selected_sheet)

# B 열 데이터를 숫자로 변환
df['%'] = pd.to_numeric(df['%'], errors='coerce')  # 'B'는 B 열의 실제 이름으로 변경해야 합니다.




st.markdown("<hr style='border: 1px dashed #ccc;'>", unsafe_allow_html=True)


st.write("📍 위 내용에 대한 잠재 방한 여행객의 특성은 다음과 같습니다.")
st.dataframe(df)
st.caption("※ 결과값은 소숫점 첫째자리까지 나타내었습니다.")

try:
    # 비율 데이터를 기준으로 원형 그래프 생성
    categories = df.iloc[:, 0]  # 첫 번째 열을 카테고리로 사용
    values = df['%']  # '비율' 열을 숫자로 변환한 값을 사용

    # 원형 그래프 생성
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title(selected_sheet)

    # Streamlit에 차트 표시
    st.pyplot(fig)
except Exception as e:
    st.error(f"그래프를 생성하는 중 오류가 발생했습니다: {e}")




st.markdown("---")
    

st.write("2️⃣ 표와 그래프를 살펴보고, 1~9에 해당하는 데이터를 분석하여 '여행 프로그램 제작 시 고려할 내용'을 생각하여 봅시다.")
input_text = st.text_area("	💬 아래의 빈 칸에 1~9번을 분석한 내용을 모두 작성한 후 전송 버튼을 눌러주세요.")
st.caption("※ 여러번 전송 버튼을 누르면, 마지막에 입력한 내용만 저장됩니다.")


# "전송" 버튼
if st.button("전송"):
    # 입력한 데이터를 임시 저장할 파일 경로
    temp_file = os.path.join("temp", "[2차시] 여행 프로그램 구성에 반영할 내용_input.txt")
    os.makedirs("temp", exist_ok=True)  # temp 디렉토리가 없으면 생성

  # 입력 데이터를 파일로 저장
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(input_text)
    
    st.success("내용이 저장되었습니다. 해당 내용은 '[2차시] 여행 프로그램 구성에 반영할 내용'에서 확인할 수 있습니다.")

st.markdown("---")

st.write("📍 모든 과정을 마친 학생은 완료 버튼을 눌러주세요.")



# 완료 버튼
if st.button("완료"):
    # 경고 메시지 출력
    st.warning(" 🧡 1차시 수업 완료를 축하합니다! '[2차시] 여행 프로그램 구성에 반영할 내용'버튼을 눌러 학습을 시작해봅시다 🧡")
