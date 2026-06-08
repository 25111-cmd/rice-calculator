import streamlit as st
import math

# 앱 제목
st.title("다기능 계산기 웹앱")

# 사용자 입력
num1 = st.number_input("첫 번째 숫자 입력", value=0.0)
num2 = st.number_input("두 번째 숫자 입력", value=0.0)

# 연산 선택
operation = st.selectbox(
    "연산 선택",
    ["덧셈", "뺄셈", "곱셈", "나눗셈", "모듈러", "지수", "로그"]
)

# 결과 계산
if operation == "덧셈":
    result = num1 + num2
elif operation == "뺄셈":
    result = num1 - num2
elif operation == "곱셈":
    result = num1 * num2
elif operation == "나눗셈":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "0으로 나눌 수 없습니다."
elif operation == "모듈러":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "0으로 나눌 수 없습니다."
elif operation == "지수":
    result = num1 ** num2
elif operation == "로그":
    if num1 > 0 and num2 > 0 and num2 != 1:
        result = math.log(num1, num2)
    else:
        result = "로그 연산은 양수 입력과 밑 ≠ 1 조건이 필요합니다."

# 결과 출력
st.write("결과:", result)

