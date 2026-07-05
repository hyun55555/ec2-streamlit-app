import streamlit as st

# 1. 간단한 설명 문구
st.title("지능형 비용 관리 솔루션 (데모)")
st.write("AWS EC2 배포 및 터미널 로그 확인을 위한 테스트 앱입니다.")

# 2. 텍스트 입력창
expense_input = st.text_input("청구할 영수증 금액을 입력하세요 (예: 15000):")

# 3. 버튼 및 4. 간단한 결과 출력
if st.button("비용 승인 요청"):
    if expense_input:
        st.success(f"입력된 금액 {expense_input}원이 성공적으로 시스템에 접수되었습니다!")
        # EC2 터미널 화면에 보여주기 위한 로그 출력
        print(f"[LOG] 사용자 입력 감지 - 비용 승인 요청 금액: {expense_input}원") 
    else:
        st.warning("금액을 먼저 입력해주세요.")
