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

    # 먼저 연산 종류를 선택
    operation = st.selectbox(
        "연산 선택",
        ["덧셈", "뺄셈", "곱셈", "나눗셈", "모듈러", "지수", "로그"]
    )

    # 연산에 따라 동적으로 입력 필드 생성
    if operation == "덧셈":
        st.info("두 숫자를 더합니다")
        num1 = st.number_input("첫 번째 숫자", value=0.0, key="add1")
        num2 = st.number_input("두 번째 숫자", value=0.0, key="add2")
        result = num1 + num2
        
    elif operation == "뺄셈":
        st.info("첫 번째 숫자에서 두 번째 숫자를 뺍니다")
        num1 = st.number_input("첫 번째 숫자 (피제수)", value=0.0, key="sub1")
        num2 = st.number_input("두 번째 숫자 (제수)", value=0.0, key="sub2")
        result = num1 - num2
        
    elif operation == "곱셈":
        st.info("두 숫자를 곱합니다")
        num1 = st.number_input("첫 번째 숫자", value=0.0, key="mul1")
        num2 = st.number_input("두 번째 숫자", value=0.0, key="mul2")
        result = num1 * num2
        
    elif operation == "나눗셈":
        st.info("첫 번째 숫자를 두 번째 숫자로 나눕니다")
        num1 = st.number_input("피제수 (분자)", value=0.0, key="div1")
        num2 = st.number_input("제수 (분모) - 0이 아닌 수", value=1.0, key="div2")
        result = num1 / num2 if num2 != 0 else "오류: 0으로 나눌 수 없습니다"
        
    elif operation == "모듈러":
        st.info("첫 번째 숫자를 두 번째 숫자로 나눈 나머지를 구합니다")
        num1 = st.number_input("피제수", value=0.0, key="mod1")
        num2 = st.number_input("제수 - 0이 아닌 수", value=1.0, key="mod2")
        result = num1 % num2 if num2 != 0 else "오류: 0으로 나눌 수 없습니다"
        
    elif operation == "지수":
        st.info("첫 번째 숫자를 두 번째 숫자 제곱합니다 (num1 ^ num2)")
        num1 = st.number_input("밑(base)", value=2.0, key="exp1")
        num2 = st.number_input("지수(exponent)", value=3.0, key="exp2")
        result = num1 ** num2
        
    elif operation == "로그":
        st.info("로그를 계산합니다 (밑이 두 번째 숫자인 첫 번째 숫자의 로그)")
        num1 = st.number_input("진수 (0보다 큰 수)", value=10.0, key="log1")
        num2 = st.number_input("밑 (0보다 크고 1이 아닌 수)", value=10.0, key="log2")
        if num1 > 0 and num2 > 0 and num2 != 1:
            result = math.log(num1, num2)
        else:
            result = "오류: 로그는 양수 입력과 밑 ≠ 1 조건이 필요합니다"

    st.write("**결과:**", result)

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
