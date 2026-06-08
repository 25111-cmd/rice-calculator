import streamlit as st
import math
import random
import plotly.express as px

# 앱 제목
st.title("다기능 웹앱")

# 사이드바 메뉴
menu = st.sidebar.selectbox("앱 선택", ["계산기", "확률 시뮬레이터"])

# ---------------- 계산기 ----------------
if menu == "계산기":
    st.header("🧮 계산기")

    num1 = st.number_input("첫 번째 숫자 입력", value=0.0)
    num2 = st.number_input("두 번째 숫자 입력", value=0.0)

    operation = st.selectbox(
        "연산 선택",
        ["덧셈", "뺄셈", "곱셈", "나눗셈", "모듈러", "지수", "로그"]
    )

    if operation == "덧셈":
        result = num1 + num2
    elif operation == "뺄셈":
        result = num1 - num2
    elif operation == "곱셈":
        result = num1 * num2
    elif operation == "나눗셈":
        result = num1 / num2 if num2 != 0 else "0으로 나눌 수 없습니다."
    elif operation == "모듈러":
        result = num1 % num2 if num2 != 0 else "0으로 나눌 수 없습니다."
    elif operation == "지수":
        result = num1 ** num2
    elif operation == "로그":
        if num1 > 0 and num2 > 0 and num2 != 1:
            result = math.log(num1, num2)
        else:
            result = "로그 연산은 양수 입력과 밑 ≠ 1 조건이 필요합니다."

    st.write("결과:", result)

# ---------------- 확률 시뮬레이터 ----------------
elif menu == "확률 시뮬레이터":
    st.header("🎲 확률 시뮬레이터")

    choice = st.radio("시뮬레이션 대상 선택", ["주사위", "동전"])
    trials = st.number_input("시행 횟수 입력", min_value=1, value=100)

    if st.button("시뮬레이션 실행"):
        results = []
        if choice == "주사위":
            results = [random.randint(1, 6) for _ in range(trials)]
            fig = px.histogram(results, nbins=6, title="주사위 결과 분포", labels={'value':'눈'})
        else:  # 동전
            results = [random.choice(["앞", "뒤"]) for _ in range(trials)]
            fig = px.histogram(results, title="동전 결과 분포", labels={'value':'면'})

        st.plotly_chart(fig)
