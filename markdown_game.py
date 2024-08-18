import streamlit as st

# 마크다운 문법 데이터
markdown_lessons = [
    {
        "title": "제목 (Headers)",
        "description": "# 을 사용하여 제목을 만듭니다. #의 개수로 수준을 조절합니다.",
        "example": "# 제목 1\n## 제목 2\n### 제목 3",
        "task": "# 을 사용하여 '안녕하세요'를 1단계 제목으로 만들어보세요.",
        "solution": "# 안녕하세요"
    },
    {
        "title": "강조 (Emphasis)",
        "description": "*와 **를 사용하여 텍스트를 강조합니다.",
        "example": "*기울임*\n**굵게**\n***굵게 기울임***",
        "task": "'중요'라는 단어를 굵게 만들어보세요.",
        "solution": "**중요**"
    },
    {
        "title": "목록 (Lists)",
        "description": "- 또는 1. 을 사용하여 목록을 만듭니다.",
        "example": "- 항목 1\n- 항목 2\n1. 첫 번째\n2. 두 번째",
        "task": "- 를 사용하여 '사과'와 '바나나'를 목록으로 만들어보세요.",
        "solution": "- 사과\n- 바나나"
    },
    {
        "title": "링크 (Links)",
        "description": "[텍스트](URL) 형식으로 링크를 만듭니다.",
        "example": "[구글](https://www.google.com)",
        "task": "'네이버'라는 텍스트로 네이버(https://www.naver.com) 링크를 만들어보세요.",
        "solution": "[네이버](https://www.naver.com)"
    },
    {
        "title": "이미지 (Images)",
        "description": "![대체 텍스트](이미지 URL) 형식으로 이미지를 삽입합니다.",
        "example": "![고양이](https://example.com/cat.jpg)",
        "task": "'로고'라는 대체 텍스트로 https://example.com/logo.png 이미지를 삽입해보세요.",
        "solution": "![로고](https://example.com/logo.png)"
    },
    {
        "title": "인용 (Blockquotes)",
        "description": "> 를 사용하여 인용문을 만듭니다.",
        "example": "> 이것은 인용문입니다.",
        "task": "'지혜로운 말씀'이라는 문장을 인용문으로 만들어보세요.",
        "solution": "> 지혜로운 말씀"
    },
    {
        "title": "코드 (Code)",
        "description": "` 를 사용하여 인라인 코드를, ``` 를 사용하여 코드 블록을 만듭니다.",
        "example": "인라인 코드: `print('Hello')`\n```\ndef hello():\n    print('Hello, World!')\n```",
        "task": "'print(\"안녕하세요\")'를 인라인 코드로 만들어보세요.",
        "solution": "`print(\"안녕하세요\")`"
    },
    {
        "title": "수평선 (Horizontal Rules)",
        "description": "--- 또는 *** 를 사용하여 수평선을 그립니다.",
        "example": "---\n텍스트\n***",
        "task": "--- 를 사용하여 수평선을 그어보세요.",
        "solution": "---"
    },
    {
        "title": "표 (Tables)",
        "description": "| 와 - 를 사용하여 표를 만듭니다.",
        "example": "| 제목1 | 제목2 |\n|-------|-------|\n| 내용1 | 내용2 |",
        "task": "'이름'과 '나이'를 제목으로 하는 2x2 표를 만들어보세요.",
        "solution": "| 이름 | 나이 |\n|------|------|\n|      |      |"
    },
    {
        "title": "체크리스트 (Checklists)",
        "description": "- [ ] 와 - [x] 를 사용하여 체크리스트를 만듭니다.",
        "example": "- [ ] 할 일 1\n- [x] 완료된 일",
        "task": "'우유 사기'는 완료되지 않은 항목으로, '빵 사기'는 완료된 항목으로 체크리스트를 만들어보세요.",
        "solution": "- [ ] 우유 사기\n- [x] 빵 사기"
    }
]

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