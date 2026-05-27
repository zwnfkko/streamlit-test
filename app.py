import streamlit as st

st.set_page_config(
    page_title="?댁???| ?먭린?뚭컻",
    page_icon="?뙵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS 而ㅼ뒪? ?ㅽ???st.markdown("""
<style>
    .profile-header {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .profile-name {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
    }
    .profile-title {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }
    .section-card {
        background: #fff5f7;
        border-left: 4px solid #f5576c;
        padding: 1rem 1.5rem;
        border-radius: 0 8px 8px 0;
        margin-bottom: 1rem;
    }
    .avatar-wrap img {
        border-radius: 50%;
        border: 4px solid #f5576c;
        box-shadow: 0 4px 16px rgba(245,87,108,0.25);
    }
    .skill-tag {
        display: inline-block;
        background: #f5576c;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin: 0.2rem;
    }
    .contact-item {
        font-size: 1rem;
        padding: 0.4rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ?? ?ъ씠?쒕컮 ??????????????????????????????????????????
with st.sidebar:
    st.markdown('<div class="avatar-wrap">', unsafe_allow_html=True)
    st.image("https://api.dicebear.com/7.x/adventurer/svg?seed=Jiwon&backgroundColor=ffd5dc&hair=long16&hairColor=6a4e35&eyes=variant12&eyebrows=variant08&mouth=variant04&skinColor=f9c9b6", width=160)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("### ?댁????뙵")
    st.markdown("**??ㅽ깮 媛쒕컻??*")
    st.divider()
    st.markdown("#### ?곕씫泥?)
    st.markdown("?벁 zwnfkko@gmail.com")
    st.markdown("?벑 010-1234-5678")
    st.markdown("?맩 [github.com/zwnfkko](https://github.com/zwnfkko)")
    st.divider()
    menu = st.radio("?섏씠吏 ?대룞", ["?룧 ??, "?뮳 寃쎈젰", "?썱截?湲곗닠?ㅽ깮", "?뱛 ?꾨줈?앺듃", "?벉 ?곕씫?섍린"])

# ?? 硫붿씤 ?ㅻ뜑 ??????????????????????????????????????????
st.markdown("""
<div class="profile-header">
    <p class="profile-name">?덈뀞?섏꽭?? ?댁??먯엯?덈떎 ?뙵</p>
    <p class="profile-title">??ㅽ깮 媛쒕컻??쨌 ?곗씠??遺꾩꽍媛 쨌 臾몄젣 ?닿껐??/p>
</div>
""", unsafe_allow_html=True)

# ?? ??????????????????????????????????????????????????
if menu == "?룧 ??:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("寃쎈젰", "3??, "?좎엯?믪＜?덉뼱")
    col2.metric("?꾨즺 ?꾨줈?앺듃", "12媛?, "+3 ?ы빐")
    col3.metric("?ъ슜 ?몄뼱", "5媛吏", "Python, JS ??)
    col4.metric("?먭꺽利?, "3媛?, "理쒓렐 痍⑤뱷")

    st.divider()

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.subheader("?뫀 ?뚭컻")
        st.markdown("""
        <div class="section-card">
        ?덈뀞?섏꽭?? ???<strong>?댁???/strong>?낅땲??<br><br>
        ?ъ슜??寃쏀뿕??理쒖슦?좎쑝濡??앷컖?섎뒗 <strong>??ㅽ깮 媛쒕컻??/strong>濡?
        諛깆뿏?쒕????꾨줎?몄뿏?? ?곗씠??遺꾩꽍源뚯? ??꼻寃??ㅻ９?덈떎.<br><br>
        ?덈줈??湲곗닠??鍮좊Ⅴ寃??듬뱷?섍퀬 ?怨??묐젰?섏뿬 臾몄젣瑜??닿껐?섎뒗 寃껋쓣 利먭퉩?덈떎.
        </div>
        """, unsafe_allow_html=True)

        st.subheader("?럳 ?숇젰")
        st.markdown("""
        | 湲곌컙 | ?숆탳 | ?꾧났 | ?숈쐞 |
        |------|------|------|------|
        | 2018 ??2022 | ?뗢뿃??숆탳 | 而댄벂?곌났?숆낵 | ?숈궗 |
        | 2022 ??2024 | ?뗢뿃??숈썝 | ?뚰봽?몄썾?닿났??| ?앹궗 |
        """)

    with col_right:
        st.subheader("?뙚 ?듭떖 ??웾")
        competencies = {
            "臾몄젣 ?닿껐??: 90,
            "而ㅻ??덉??댁뀡": 85,
            "??뚰겕": 95,
            "?먭린 ?숈뒿": 88,
            "李쎌쓽??: 80,
        }
        for skill, score in competencies.items():
            st.markdown(f"**{skill}**")
            st.progress(score / 100)

# ?? 寃쎈젰 ??????????????????????????????????????????????
elif menu == "?뮳 寃쎈젰":
    st.subheader("?뮳 寃쎈젰 ?ы빆")

    experiences = [
        {
            "period": "2024.03 ???꾩옱",
            "company": "(二? ABC?뚰겕",
            "role": "諛깆뿏??媛쒕컻??,
            "desc": "FastAPI 湲곕컲 RESTful API ?ㅺ퀎 諛?媛쒕컻, PostgreSQL DB 理쒖쟻?? CI/CD ?뚯씠?꾨씪??援ъ텞",
            "tags": ["Python", "FastAPI", "PostgreSQL", "Docker", "AWS"],
        },
        {
            "period": "2022.07 ??2024.02",
            "company": "(二? DEF?붾（??,
            "role": "??ㅽ깮 媛쒕컻??,
            "desc": "React + Django 湲곕컲 ?щ궡 ERP ?쒖뒪??媛쒕컻, ?곗씠???쒓컖????쒕낫??援ъ텞",
            "tags": ["React", "Django", "MySQL", "Chart.js"],
        },
        {
            "period": "2021.01 ??2022.06",
            "company": "GHI?ㅽ??몄뾽",
            "role": "?명꽩 媛쒕컻??,
            "desc": "Python ?곗씠???뚯씠?꾨씪??媛쒕컻, Streamlit ??쒕낫???꾨줈?좏??댄븨",
            "tags": ["Python", "Pandas", "Streamlit"],
        },
    ]

    for exp in experiences:
        with st.expander(f"**{exp['period']}** | {exp['company']} ??{exp['role']}", expanded=True):
            st.markdown(f"**??븷:** {exp['role']}")
            st.markdown(f"**湲곌컙:** {exp['period']}")
            st.markdown(f"**二쇱슂 ?낅Т:** {exp['desc']}")
            tags_html = " ".join([f'<span class="skill-tag">{t}</span>' for t in exp["tags"]])
            st.markdown(f"**?ъ슜 湲곗닠:** {tags_html}", unsafe_allow_html=True)

# ?? 湲곗닠?ㅽ깮 ???????????????????????????????????????????
elif menu == "?썱截?湲곗닠?ㅽ깮":
    st.subheader("?썱截?湲곗닠 ?ㅽ깮")

    tab1, tab2, tab3, tab4 = st.tabs(["?릫 諛깆뿏??, "?렓 ?꾨줎?몄뿏??, "?뾼截??곗씠?곕쿋?댁뒪", "?숋툘 DevOps"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            skills = {"Python": 90, "FastAPI": 80, "Django": 75, "Node.js": 65}
            for s, v in skills.items():
                st.markdown(f"**{s}**")
                st.progress(v / 100)
                st.caption(f"{v}%")
        with col2:
            st.markdown("**二쇱슂 ?쇱씠釉뚮윭由?*")
            libs = ["Pandas", "NumPy", "SQLAlchemy", "Pydantic", "Celery", "Streamlit"]
            for l in libs:
                st.markdown(f"- `{l}`")

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            skills = {"React": 80, "TypeScript": 70, "HTML/CSS": 85, "Vue.js": 55}
            for s, v in skills.items():
                st.markdown(f"**{s}**")
                st.progress(v / 100)
                st.caption(f"{v}%")
        with col2:
            st.markdown("**二쇱슂 ?쇱씠釉뚮윭由?*")
            libs = ["Redux", "Tailwind CSS", "Chart.js", "Axios"]
            for l in libs:
                st.markdown(f"- `{l}`")

    with tab3:
        skills = {"PostgreSQL": 85, "MySQL": 80, "MongoDB": 65, "Redis": 60}
        for s, v in skills.items():
            col1, col2 = st.columns([3, 1])
            col1.progress(v / 100, text=s)
            col2.markdown(f"**{v}%**")

    with tab4:
        col1, col2 = st.columns(2)
        with col1:
            skills = {"Docker": 75, "AWS": 65, "Linux": 80, "Git": 90}
            for s, v in skills.items():
                st.markdown(f"**{s}**")
                st.progress(v / 100)
        with col2:
            st.markdown("**?먭꺽利?*")
            st.success("??AWS Solutions Architect Associate")
            st.success("???뺣낫泥섎━湲곗궗")
            st.info("?봽 CKAD (痍⑤뱷 以鍮?以?")

# ?? ?꾨줈?앺듃 ???????????????????????????????????????????
elif menu == "?뱛 ?꾨줈?앺듃":
    st.subheader("?뱛 二쇱슂 ?꾨줈?앺듃")

    projects = [
        {
            "title": "?ㅼ떆媛?二쇱떇 ??쒕낫??,
            "period": "2024.06 ??2024.09",
            "desc": "WebSocket?쇰줈 ?ㅼ떆媛?二쇨? ?곗씠?곕? ?섏떊?섏뿬 Streamlit?쇰줈 ?쒓컖?뷀븯????쒕낫?? ?ы듃?대━???섏씡瑜?遺꾩꽍 湲곕뒫 ?ы븿.",
            "tech": ["Python", "Streamlit", "WebSocket", "Plotly", "PostgreSQL"],
            "role": "媛쒖씤 ?꾨줈?앺듃",
            "highlight": "???됯퇏 200紐??ъ슜",
        },
        {
            "title": "?щ궡 ERP ?쒖뒪??,
            "period": "2023.01 ??2023.12",
            "desc": "以묒냼湲곗뾽??留욎땄??ERP ?쒖뒪?? ?몄궗쨌?щТ쨌?ш퀬 愿由?紐⑤뱢???듯빀?섏뿬 ?낅Т ?⑥쑉 40% ?μ긽.",
            "tech": ["React", "Django", "MySQL", "Docker"],
            "role": "? 由щ뱶 (4??",
            "highlight": "?낅Т ?⑥쑉 40% ?μ긽",
        },
        {
            "title": "AI 梨쀫큸 怨좉컼?쇳꽣",
            "period": "2024.01 ??2024.04",
            "desc": "LLM 湲곕컲 怨좉컼 ?묐? 梨쀫큸. FAQ ?먮룞 ?묐떟 諛??곷떞???곌껐 湲곕뒫 援ы쁽. ?곷떞 ?湲??쒓컙 60% ?⑥텞.",
            "tech": ["Python", "FastAPI", "LangChain", "Redis", "React"],
            "role": "諛깆뿏???대떦",
            "highlight": "?湲??쒓컙 60% ?⑥텞",
        },
    ]

    for proj in projects:
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {proj['title']}")
                st.caption(f"?뱟 {proj['period']}  |  ?뫀 {proj['role']}")
                st.markdown(proj["desc"])
                tags_html = " ".join([f'<span class="skill-tag">{t}</span>' for t in proj["tech"]])
                st.markdown(tags_html, unsafe_allow_html=True)
            with col2:
                st.metric("?깃낵", proj["highlight"])

# ?? ?곕씫?섍린 ???????????????????????????????????????????
elif menu == "?벉 ?곕씫?섍린":
    st.subheader("?벉 ?곕씫?섍린")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 硫붿떆吏 蹂대궡湲?)
        with st.form("contact_form"):
            name = st.text_input("?대쫫")
            email = st.text_input("?대찓??)
            subject = st.selectbox("臾몄쓽 ?좏삎", ["?묒뾽 ?쒖븞", "梨꾩슜 臾몄쓽", "湲곗닠 吏덈Ц", "湲고?"])
            message = st.text_area("硫붿떆吏", height=150)
            submitted = st.form_submit_button("?꾩넚?섍린", type="primary", use_container_width=True)
            if submitted:
                if name and email and message:
                    st.success(f"??{name}?? 硫붿떆吏媛 ?꾩넚?섏뿀?듬땲?? 鍮좊Ⅸ ?쒖씪 ?댁뿉 ?듬??쒕━寃좎뒿?덈떎.")
                else:
                    st.error("?대쫫, ?대찓?? 硫붿떆吏瑜?紐⑤몢 ?낅젰?댁＜?몄슂.")

    with col2:
        st.markdown("#### ?곕씫泥??뺣낫")
        st.markdown("""
        | | |
        |--|--|
        | ?벁 ?대찓??| zwnfkko@google.com |
        | ?벑 ?꾪솕 | 010-1234-5678 |
        | ?맩 GitHub | [github.com/zwnfkko](https://github.com/zwnfkko) |
        | ?뮳 LinkedIn | linkedin.com/in/jiwon |
        | ?뱧 ?꾩튂 | ?쒖슱?밸퀎??|
        """)

        st.markdown("#### ?묐떟 媛???쒓컙")
        st.info("???됱씪 ?ㅼ쟾 10??~ ?ㅽ썑 6??n\n蹂댄넻 24?쒓컙 ?대궡 ?묐떟?⑸땲??")
