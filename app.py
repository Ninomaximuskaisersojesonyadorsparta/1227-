import streamlit as st
from openai import OpenAI
import os as os # 컴퓨터 파일이나 폴더 다룰때 필요한 도구

st.session_state.language = '한국어'

# Streamlit 설정
st.set_page_config(page_title="뽀로로 친구들과 이야기!", page_icon=":house_with_garden:")

# 초기 API 키 상태
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# API 키 입력 받기
st.session_state.api_key = st.text_input("OpenAI API 키를 입력하세요:", type="password")

# API 키가 입력되었을 때만 실행
if st.session_state.api_key:
    os.environ["OPENAI_API_KEY"] = st.session_state.api_key
    client = OpenAI(
       api_key=st.session_state.api_key
    )

# 환경 변수 설정
# os.environ["OPENAI_API_KEY"] = ""

# OpenAI API 키 설정
# client = OpenAI(
   #api_key=os.environ.get("OPENAI_API_KEY")
#)


# 애니 캐릭터와 그들의 정보 및 이미지 URL
characters = {
    "크롱": ["아기공룡", "https://i.namu.wiki/i/q_7uiXC7uY7Qj5kmTKRfthdmd73qcPCar5pb5gGnicyC6S2qsdqHr3H0wcfw5MMxVTIRedv9IMQVHe4B6e1qEvLy3Nv5xNMpW7ZgkvS9tX1aYCM-13ayEHT3a_nEl8oT3tkKToTvPjYRIWnjgEQApQ.webp"],
    "포비": ["북극곰", "https://i.namu.wiki/i/2PsdUu7VFU_3YUmOzjvfDaA9VJTXREln2dsTDaY4iJN4kaF-0mhYYC2a0lP8rT6oR6pPydZ0ieeggRjXlsVvZjcEzQDpP_Wf_EDSHO7CRyhoBmbfIiTS0UeGR_9x1nhOQOXIdv0lYr7TGfoN1svktQ.webp"]
}


# 사용자 아바타 이미지 URL
user_avatar_url = "data:image/webp;base64,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"
assistant_avatar_url = "data:image/webp;base64,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"


# CSS 스타일 정의
def chat_styles():
    st.markdown("""
    <style>
    body, .stApp {
        background-color: white;
    }
    .stApp {
        color: black;
    }
    .title {
        color: black;
    }
    .title img {
        width: 100%;
        max-width: 300px;
        display: block;
        margin: 0 auto 20px auto;
    }
    .chat-bubble {
        padding: 10px;
        margin: 5px;
        border-radius: 10px;
        display: inline-block; /* 텍스트 길이에 맞춰 말풍선 길이 조정 */
        max-width: 70%;
        word-wrap: break-word;
        display: flex;
        align-items: flex-start;
    }
    .chat-avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        margin-right: 10px;
        object-fit: cover;
    }
    .user-bubble {
        background-color: #e0e0e0;
        color: black;
        border-top-right-radius: 0;
        margin-left: auto;
        flex-direction: row-reverse;
        gap: 10px;
    }
    .assistant-bubble {
        background-color: #faffa3;
        color: black;
        border-top-left-radius: 0;
        margin-right: auto;
        gap: 10px;
    }
    .user-message {
        align-self: flex-end;
    }
    .assistant-message {
        align-self: flex-start;
    }
    .spinner-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 10px 0;
    }
    .member-selection {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .member-card {
        background-color: #f1f1f1;
        border: none;
        padding: 10px;
        margin: 5px;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        cursor: pointer;
        width: 200px;
        text-align: center;
    }
    .member-card img {
        border-radius: 50%;
        width: 100px;
        height: 100px;
        object-fit: cover;
        margin-bottom: 10px;
    }
    .member-card span {
        margin-bottom: 10px;
    }
    .member-button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 14px;
        cursor: pointer;
        border-radius: 5px;
        width: 100%;
        box-sizing: border-box;
    }
    .member-card button {
        background-color: transparent;
        border: none;
        padding: 0;
        text-align: center;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)


# 말풍선 스타일의 메시지 표시 함수
def display_chat_message(role, content, avatar_url):
    bubble_class = "user-bubble" if role == "user" else "assistant-bubble"
    message_class = "user-message" if role == "user" else "assistant-message"
    st.markdown(f"""
    <div class="chat-bubble {bubble_class} {message_class}">
        <img src="{avatar_url}" class="chat-avatar">
        <div>{content}</div>
    </div>
    """, unsafe_allow_html=True)


# 대화를 생성하는 함수
def generate_conversation(language, character, user_input):
    prompt = f"""
    1. 당신은 지금 {character}의 역할을 연기하고 있습니다. 사용자의의 요구와 질문에 {character}의 말투와 스타일로 한국어로 응답하세요.

    2. 다음은 애니 캐릭터에 대한 정보 링크입니다
    [크롱]: [https://namu.wiki/w/%ED%81%AC%EB%A1%B1].
    [포비]: [https://namu.wiki/w/%ED%8F%AC%EB%B9%84(%EB%BD%80%EB%A1%B1%EB%BD%80%EB%A1%B1%20%EB%BD%80%EB%A1%9C%EB%A1%9C)], 말투는 반말로 해주세요.
    이 정보를 바탕으로, 질문에 답하거나 이 캐릭터로 역할을 연기하세요.

    3. 사용자가 주제를 추천하길 원한다면, 최근 구글에서서 [특정 주제 분야, 예: 기술, 여행, 음식 등]와 관련된 인기 있는 주제를 검색하여 추천해 주세요.

    4. 사용자가 글의 개선하고 싶어하면 내용을 검토한 후, 명확성, 톤, 전반적인 품질을 향상시킬 수 있는 수정 사항을 제안해 주세요

    사용자 입력: {user_input}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Streamlit 애플리케이션 시작
st.title("즐거운 이야기!")

# CSS 스타일 적용
chat_styles()

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.character = None
    st.session_state.language = "한국어"
    st.session_state.character_avatar_url = assistant_avatar_url
    st.session_state.stage = 1

# 대화 히스토리 표시
chat_container = st.empty()
with chat_container.container():
    st.markdown('<div class="chat-wrapper"><div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state.messages:
        display_chat_message(msg["role"], msg["content"], st.session_state.character_avatar_url if msg["role"] == "assistant" else user_avatar_url)
    st.markdown('</div></div>', unsafe_allow_html=True)

# 캐릭터 선택 단계
if st.session_state.stage == 1:
    selected_character = None
    st.markdown('<div class="member-selection">', unsafe_allow_html=True)
    st.markdown("<h3>캐릭터를 선택하세요:</h3>", unsafe_allow_html=True)
    for character, info in characters.items():
        character_key = f"button_{character}"
        if st.button(f"{character} 선택", key=f"{character_key}_button"):
            selected_character = character
            break
        st.markdown(f"""
        <div class="member-card" id="{character_key}">
            <img src="{info[1]}" class="chat-avatar">
            <span>{character}</span>
        </div>
        """, unsafe_allow_html=True)

    if selected_character:
        st.session_state.character = selected_character
        st.session_state.character_avatar_url = characters[selected_character][1]
        request_message = f"안녕하세요! {selected_character}입니다. 무엇을 도와드릴까요?"
        st.session_state.messages.append({"role": "assistant", "content": request_message})
        st.session_state.stage = 2
        st.rerun()

# 대화 처리 단계
elif st.session_state.stage == 2:
    user_input = st.chat_input("대화를 입력하세요:", key="input_conversation")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner('답변 생성 중... 잠시만 기다려 주세요.'):
            response = generate_conversation(st.session_state.language, st.session_state.character, user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})

# 대화 히스토리 다시 표시
chat_container.empty()  # 이전 메시지 지우기
with chat_container.container():
    st.markdown('<div class="chat-wrapper"><div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state.messages:
        display_chat_message(msg["role"], msg["content"], st.session_state.character_avatar_url if msg["role"] == "assistant" else user_avatar_url)
    st.markdown('</div></div>', unsafe_allow_html=True)
