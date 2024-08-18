import streamlit as st
import difflib

# 마크다운 문법 데이터 (20개)
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
    },
    {
        "title": "취소선 (Strikethrough)",
        "description": "~~ 를 사용하여 취소선을 만듭니다.",
        "example": "~~취소된 텍스트~~",
        "task": "'오래된 정보'라는 텍스트에 취소선을 적용해보세요.",
        "solution": "~~오래된 정보~~"
    },
    {
        "title": "작은 제목 (Small Headers)",
        "description": "##### 또는 ###### 를 사용하여 작은 제목을 만듭니다.",
        "example": "##### 작은 제목\n###### 더 작은 제목",
        "task": "'부제목'이라는 텍스트를 5단계 제목으로 만들어보세요.",
        "solution": "##### 부제목"
    },
    {
        "title": "굵은 기울임 텍스트",
        "description": "***를 사용하여 텍스트를 굵게 기울입니다.",
        "example": "이것은 ***굵은 기울임*** 텍스트입니다.",
        "task": "'중요한 강조'라는 텍스트를 굵은 기울임체로 만들어보세요.",
        "solution": "***중요한 강조***"
    },
    {
        "title": "이스케이프 문자",
        "description": "\\ 를 사용하여 마크다운 문법을 무시하고 문자 그대로 표시합니다.",
        "example": "\\*이것은 기울임체가 아닙니다\\*",
        "task": "*강조*라는 텍스트를 마크다운 문법이 적용되지 않도록 이스케이프 처리해보세요.",
        "solution": "\\*강조\\*"
    },
    {
        "title": "각주 (Footnotes)",
        "description": "[^1] 형식으로 각주를 만들고, [^1]: 로 각주 내용을 정의합니다.",
        "example": "여기에 각주[^1]가 있습니다.\n\n[^1]: 이것이 각주 내용입니다.",
        "task": "'중요한 정보'라는 텍스트에 '상세 설명은 문서 하단 참조'라는 내용의 각주를 추가해보세요.",
        "solution": "중요한 정보[^1]\n\n[^1]: 상세 설명은 문서 하단 참조"
    },
    {
        "title": "정의 목록 (Definition Lists)",
        "description": "용어와 정의를 구분하여 목록을 만듭니다.",
        "example": "용어\n: 정의",
        "task": "'마크다운'이라는 용어와 그 정의 '텍스트 기반의 마크업 언어'를 정의 목록으로 만들어보세요.",
        "solution": "마크다운\n: 텍스트 기반의 마크업 언어"
    },
    {
        "title": "작업 목록 (Task Lists)",
        "description": "- [ ]와 - [x]를 사용하여 완료/미완료 작업 목록을 만듭니다.",
        "example": "- [ ] 할 일 1\n- [x] 완료된 일",
        "task": "'운동하기'는 미완료, '책 읽기'는 완료된 작업 목록을 만들어보세요.",
        "solution": "- [ ] 운동하기\n- [x] 책 읽기"
    },
    {
        "title": "접기/펼치기 (Collapsible Sections)",
        "description": "<details>와 <summary>를 사용하여 접을 수 있는 섹션을 만듭니다.",
        "example": "<details>\n  <summary>제목</summary>\n  숨겨진 내용\n</details>",
        "task": "'더 보기'라는 제목의 접기/펼치기 섹션을 만들고, 내용에 '추가 정보입니다.'를 넣어보세요.",
        "solution": "<details>\n  <summary>더 보기</summary>\n  추가 정보입니다.\n</details>"
    },
    {
        "title": "키보드 입력 (Keyboard Input)",
        "description": "<kbd> 태그를 사용하여 키보드 입력을 나타냅니다.",
        "example": "단축키: <kbd>Ctrl</kbd> + <kbd>C</kbd>",
        "task": "'Ctrl + V' 단축키를 키보드 입력 형식으로 표현해보세요.",
        "solution": "<kbd>Ctrl</kbd> + <kbd>V</kbd>"
    },
    {
        "title": "수학 수식 (Math Equations)",
        "description": "$를 사용하여 인라인 수식을, $$를 사용하여 블록 수식을 표현합니다.",
        "example": "인라인 수식: $E = mc^2$\n\n블록 수식:\n$$\ny = ax^2 + bx + c\n$$",
        "task": "피타고라스 정리 (a² + b² = c²)를 인라인 수식으로 표현해보세요.",
        "solution": "$a^2 + b^2 = c^2$"
    }
]

def check_answer(user_input, solution):
    return user_input.strip() == solution.strip()

def get_difference(user_input, solution):
    d = difflib.Differ()
    diff = list(d.compare(user_input.splitlines(), solution.splitlines()))
    return '\n'.join(diff)

def update_lesson(i):
    st.session_state.current_lesson = max(0, min(i, len(markdown_lessons) - 1))

def main():
    st.set_page_config(page_title="마크다운 학습 게임", layout="wide")
    
    st.title("마크다운 학습 게임")
    
    # 세션 상태 초기화
    if "current_lesson" not in st.session_state:
        st.session_state.current_lesson = 0
    
    if "completed_lessons" not in st.session_state:
        st.session_state.completed_lessons = [False] * len(markdown_lessons)
    
    # current_lesson이 유효한 범위 내에 있는지 확인
    st.session_state.current_lesson = max(0, min(st.session_state.current_lesson, len(markdown_lessons) - 1))

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
            st.write("차이점:")
            st.code(get_difference(user_input, lesson['solution']))
    
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