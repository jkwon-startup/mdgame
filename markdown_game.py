import streamlit as st

# 마크다운 문법 데이터는 이전과 동일합니다.

def check_answer(user_input, solution):
    return user_input.strip() == solution.strip()

def update_lesson(i):
    st.session_state.current_lesson = i

def main():
    st.set_page_config(page_title="마크다운 학습 게임", layout="wide")
    
    st.title("마크다운 학습 게임")
    
    if "current_lesson" not in st.session_state:
        st.session_state.current_lesson = 0
    
    if "completed_lessons" not in st.session_state:
        st.session_state.completed_lessons = [False] * len(markdown_lessons)

    # 사이드바: 학습 단계 선택
    st.sidebar.title("학습 단계")
    for i, lesson in enumerate(markdown_lessons):
        if st.sidebar.button(f"{i+1}. {lesson['title']}", key=f"lesson_{i}", on_click=update_lesson, args=(i,)):
            pass

    # 메인 화면
    lesson = markdown_lessons[st.session_state.current_lesson]
    
    st.header(f"{st.session_state.current_lesson + 1}. {lesson['title']}")
    st.write(lesson['description'])
    
    st.subheader("예시:")
    st.code(lesson['example'])
    
    st.subheader("과제:")
    st.write(lesson['task'])
    
    user_input = st.text_area(
        "여기에 마크다운을 입력하세요:",
        height=100,
        key=f"user_input_{st.session_state.current_lesson}"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("입력한 마크다운:")
        st.code(user_input)
    
    with col2:
        st.subheader("미리보기:")
        st.markdown(user_input)
    
    if st.button("확인"):
        if check_answer(user_input, lesson['solution']):
            st.success("정답입니다!! 🎉🎉🎉")
            st.balloons()
            st.session_state.completed_lessons[st.session_state.current_lesson] = True
        else:
            st.error("틀렸습니다!! ㅜㅜ 다시 도전해봐요!!")
    
    # 진행 상황
    progress = sum(st.session_state.completed_lessons) / len(markdown_lessons)
    st.progress(progress)
    st.write(f"진행 상황: {sum(st.session_state.completed_lessons)}/{len(markdown_lessons)}")
    
    # 이전/다음 버튼
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.current_lesson > 0:
            if st.button("이전 단계", on_click=update_lesson, args=(st.session_state.current_lesson - 1,)):
                pass
    
    with col2:
        if st.session_state.current_lesson < len(markdown_lessons) - 1:
            if st.button("다음 단계", on_click=update_lesson, args=(st.session_state.current_lesson + 1,)):
                pass

if __name__ == "__main__":
    main()