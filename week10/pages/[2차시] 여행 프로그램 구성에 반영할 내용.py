import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib import rc
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import black, gray

rc('font', family='Malgun Gothic')  # Windows: "맑은 고딕 사용"

plt.rcParams['axes.unicode_minus'] = False


st.title('📝 여행 프로그램 구성에 반영할 내용을 정리해보자')

st.markdown("---")

st.write("1️⃣ [1차시]에서 정리한 내용을 확인하여봅시다.")
st.caption("※ 아래 버튼을 클릭하여 [1차시]에서 작성한 내용을 불러와봅시다.")

# 저장된 데이터 파일 경로
temp_file = "temp/[2차시] 여행 프로그램 구성에 반영할 내용_input.txt"

# 저장된 데이터 읽기
if st.button("1차시에서 입력한 내용 불러오기", key="load_button"):
    try:
        with open(temp_file, "r", encoding="utf-8") as f:
            saved_data = f.read()
        st.write("저장된 데이터:")
        st.write(saved_data)
    except FileNotFoundError:
        st.error("데이터가 저장된 파일을 찾을 수 없습니다.")


st.caption("※ 입력한 내용을 삭제하고 싶다면 아래 버튼을 클릭하세요.")
# 입력한 데이터 삭제
if st.button("입력한 데이터 삭제하기", key="delete_button"):
    try:
        os.remove(temp_file)
        st.success("데이터가 성공적으로 삭제되었습니다. [1차시]로 돌아가서 '잠재 방한 여행객 주요 특성'을 다시 살펴보고, 분석 내용을 입력해주세요.")
    except FileNotFoundError:
        st.error("삭제할 데이터를 찾을 수 없습니다.")
    except Exception as e:
        st.error(f"데이터 삭제 중 오류가 발생했습니다: {e}")

st.markdown("---")

st.write("2️⃣ 잠재 방한 여행객을 대상으로 한 홍보물 계획서를 작성하여봅시다.")
st.caption("※ 위의 내용을 참고하여 아래의 질문에 답해봅시다. 입력한 내용은 홍보물 계획서 형태(PDF)로 저장됩니다.")

st.markdown("<hr style='border: 1px dashed #ccc;'>", unsafe_allow_html=True)

# 질문 목록
questions = [
    "1. 👨‍🎓👩‍🎓 번호와 이름을 적어주세요. (예시 : 1번 홍길동)",
    "2. 💡 여행 프로그램의 제목은 무엇인가요? 왜 그렇게 생각하였나요?",
    "3. 💡 여행 프로그램의 테마를 무엇으로 할 것인가요? 왜 그렇게 생각하였나요?",
    "4. 💡 여행 프로그램에 어떤 내용을 포함할 것인가요? 왜 그렇게 생각하였나요?",
    "5. 💡 여행 프로그램의 기간은 얼마로 할 것인가요? 왜 그렇게 생각하였나요?",
    "6. 💡 여행 프로그램의 비용은 얼마로 할 것인가요? 왜 그렇게 생각하였나요?",
    "7. 💡 여행 프로그램의 비용은 어떤 통화로 나타낼 것인가요? 왜 그렇게 생각하였나요?",
    "8. 💡 여행 프로그램의 기념품으로 무엇을 줄 것인가요? 왜 그렇게 생각하였나요?",
    "9. 💡 여행 프로그램 홍보물을 어디에 게시할 것인가요? 왜 그렇게 생각하였나요?",
]

# 사용자 입력 저장
answers = {}

# 질문 출력 및 사용자 입력받기

st.subheader("📍 잠재 방한 여행객을 대상으로 한 홍보물 계획서")
st.markdown("")

for question in questions:
    answers[question] = st.text_area(question, "")

# PDF 파일 생성 함수
def save_to_pdf(questions_and_answers, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    margin = 50
    y = height - 50  # 시작 위치


 # 한글 폰트 설정
    pdfmetrics.registerFont(TTFont('MalgunGothic', 'C:/Windows/Fonts/malgun.ttf'))  # 폰트 경로 확인 필요
    c.setFont('MalgunGothic', 12)  # 폰트 설정

    # 외곽 박스를 그리기 위해 회색 설정
    c.setStrokeColor(gray)  # 외곽선 색상 설정
    c.rect(margin, margin, width - 2 * margin, height - 2 * margin, fill=False, stroke=True)

    # 글자 색을 검정색으로 설정
    c.setFillColor(black)
    c.drawString(100, y, "잠재 방한 여행객을 대상으로 한 홍보물 계획서")
    y -= 30  # 간격 조정

    for question, answer in questions_and_answers.items():
        c.drawString(100, y, f"Q: {question}")
        y -= 15
        answer_lines = answer.split('\n')
        for line in answer_lines:
            c.drawString(120, y, f"A: {line}")
            y -= 15
        y -= 10  # 질문 간 간격

    c.save()

# "PDF 저장" 버튼
if st.button("PDF 저장"):
    # 첫 번째 질문의 답변을 가져와 파일 이름에 사용
    first_answer = answers[questions[0]].split('\n')[0]  # 첫 번째 질문에 대한 답변의 첫 줄만 사용
    pdf_filename = f"({first_answer}) 잠재 방한 여행객 홍보물.pdf"
    path = os.path.join("output", pdf_filename)

    # 디렉토리 생성
    os.makedirs("output", exist_ok=True)

    save_to_pdf(answers, path)
    st.success(f"PDF 파일이 '{pdf_filename}'로 저장되었습니다.")

    # PDF 다운로드 링크 제공
    with open(path, "rb") as f:
        st.download_button(
            label="PDF 다운로드",
            data=f,
            file_name=pdf_filename,
            mime="application/pdf"
        )

st.markdown("---")

st.write("3️⃣ 저장한 PDF파일은 패들릿에 업로드해주세요.")
st.caption("※ 해당 내용은 포트폴리오에 해당되며, 추후 평가에 참고할 예정입니다.")


# 완료 버튼
if st.button("완료"):
    # 경고 메시지 출력
    st.warning(" 🧡 2차시 수업 완료를 축하합니다! 3차시 수업은 CANVA로 진행될 예정입니다! 🧡")