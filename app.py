import streamlit as st

st.set_page_config(
    page_title="이지원 | 자기소개",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0">
""", unsafe_allow_html=True)

# ── 팔레트: #d8e2dc  #ffe5d9  #ffcad4  #f4acb7  #9d8189
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');

html, body, [class*="css"], [data-testid] {
    font-family: 'Noto Sans KR', -apple-system, sans-serif !important;
}

/* ── 기본 배경 ──────────────────────────────────── */
[data-testid="stAppViewContainer"] > .main { background: #faf8f7; }
[data-testid="stHeader"] { background: transparent !important; box-shadow: none !important; }
.block-container { padding: 1.8rem 2rem 3rem !important; max-width: 1080px; }

/* ── 사이드바 ───────────────────────────────────── */
[data-testid="stSidebar"] { background: #d8e2dc !important; border-right: none; }
[data-testid="stSidebar"] > div:first-child { padding: 1.8rem 1.2rem; }
[data-testid="stIconMaterial"] {
    font-family: 'Material Symbols Rounded' !important;
    font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    font-size: 20px !important;
}
[data-testid="stSidebar"] .stMarkdown a { color: #9d8189 !important; text-decoration: none; font-weight: 600; }
[data-testid="stSidebar"] hr { border-color: rgba(157,129,137,0.25) !important; }

/* 라디오 메뉴 */
[data-testid="stSidebar"] .stRadio > label { display: none; }
[data-testid="stSidebar"] .stRadio > div { gap: 0.25rem; display: flex; flex-direction: column; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label input[type="radio"],
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label > div:first-child { display: none !important; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label {
    background: transparent;
    border-radius: 10px;
    padding: 0.55rem 1rem !important;
    color: #5a4a4e !important;
    font-weight: 500;
    font-size: 0.92rem;
    transition: all 0.18s;
    border: 1px solid transparent;
    cursor: pointer;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label:hover {
    background: rgba(255,255,255,0.55);
    border-color: rgba(244,172,183,0.4);
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label[data-checked="true"],
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label:has(input:checked) {
    background: white;
    border-color: #f4acb7;
    color: #9d8189 !important;
    font-weight: 700;
    box-shadow: 0 2px 8px rgba(157,129,137,0.12);
}

/* ── 탭 ─────────────────────────────────────────── */
[data-baseweb="tab-list"] {
    background: white !important;
    border-radius: 12px !important;
    padding: 4px !important;
    border: 1px solid #ffcad4 !important;
    gap: 4px !important;
    box-shadow: 0 2px 8px rgba(157,129,137,0.06);
}
[data-baseweb="tab"] {
    border-radius: 9px !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    color: #9d8189 !important;
    padding: 0.45rem 1.1rem !important;
    transition: all 0.15s !important;
}
[data-baseweb="tab"]:hover { background: #fff0f3 !important; }
[aria-selected="true"][data-baseweb="tab"] {
    background: #9d8189 !important;
    color: white !important;
}
[data-baseweb="tab-highlight"], [data-baseweb="tab-border"] { display: none !important; }

/* ── expander ───────────────────────────────────── */
[data-testid="stExpander"] {
    background: white !important;
    border: 1px solid #ffcad4 !important;
    border-radius: 14px !important;
    box-shadow: 0 2px 8px rgba(157,129,137,0.06) !important;
    margin-bottom: 0.75rem !important;
    overflow: hidden !important;
}
[data-testid="stExpander"] summary {
    padding: 0.9rem 1.2rem !important;
    font-weight: 600 !important;
    color: #3a2e30 !important;
}
[data-testid="stExpander"] summary:hover { background: #fff5f7 !important; }
[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
    padding: 0 1.2rem 1rem !important;
}

/* ── form ────────────────────────────────────────── */
[data-testid="stTextInput"] > div > div > input,
[data-testid="stTextArea"] > div > div > textarea,
[data-baseweb="select"] { border: 1.5px solid #f4acb7 !important; border-radius: 10px !important; background: #fefefe !important; }
[data-testid="stTextInput"] > div > div > input:focus,
[data-testid="stTextArea"] > div > div > textarea:focus {
    box-shadow: 0 0 0 3px rgba(244,172,183,0.22) !important;
    border-color: #9d8189 !important;
}
[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #f4acb7 0%, #9d8189 100%) !important;
    color: white !important; border: none !important;
    border-radius: 12px !important; font-weight: 700 !important;
    letter-spacing: 0.04em !important; font-size: 0.95rem !important;
    box-shadow: 0 4px 16px rgba(157,129,137,0.28) !important;
    padding: 0.65rem 1.5rem !important; width: 100% !important;
    transition: opacity 0.2s, transform 0.15s !important;
}
[data-testid="stFormSubmitButton"] > button:hover { opacity: 0.9 !important; transform: translateY(-1px) !important; }

/* ── alert ───────────────────────────────────────── */
[data-testid="stAlert"] {
    border-radius: 12px !important;
    border-left-width: 4px !important;
}
hr { border-color: #f4acb7 !important; opacity: 0.25; margin: 1.2rem 0; }

/* ── custom components ───────────────────────────── */

/* hero */
.hero {
    background: linear-gradient(135deg, #f4acb7 0%, #9d8189 100%);
    border-radius: 22px; padding: 2.6rem 3rem; color: white;
    margin-bottom: 2rem; position: relative; overflow: hidden;
    box-shadow: 0 10px 36px rgba(157,129,137,0.28);
}
.hero-deco { position: absolute; border-radius: 50%; }
.hero h1 {
    font-size: 2.3rem !important; font-weight: 900 !important;
    color: white !important; margin: 0 0 0.4rem; letter-spacing: -0.03em; line-height: 1.15;
}
.hero h1::after { display: none !important; }
.hero p { font-size: 1rem; opacity: 0.9; margin: 0; letter-spacing: 0.06em; }
.hero-chips { margin-top: 1.3rem; display: flex; gap: 0.5rem; flex-wrap: wrap; }
.hero-chip {
    background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.38);
    border-radius: 20px; padding: 0.28rem 0.85rem; font-size: 0.8rem; color: white;
}

/* stats */
.stats-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 1rem; margin-bottom: 2rem; }
.stat-card {
    background: white; border-radius: 16px; padding: 1.3rem 1rem 1.1rem;
    text-align: center; border: 1px solid rgba(244,172,183,0.25);
    box-shadow: 0 2px 12px rgba(157,129,137,0.07);
    transition: box-shadow 0.2s, transform 0.2s;
}
.stat-card:hover { box-shadow: 0 6px 22px rgba(157,129,137,0.14); transform: translateY(-2px); }
.stat-v { font-size: 2rem; font-weight: 900; color: #9d8189; line-height: 1; }
.stat-l { font-size: 0.7rem; color: #bbb; font-weight: 600; margin-top: 0.35rem; letter-spacing: 0.06em; text-transform: uppercase; }
.stat-s { font-size: 0.78rem; color: #f4acb7; margin-top: 0.2rem; font-weight: 600; }

/* section title */
.sec-title {
    font-size: 1.05rem; font-weight: 800; color: #3a2e30;
    margin: 0 0 1rem; display: flex; align-items: center; gap: 0.6rem; letter-spacing: -0.01em;
}
.sec-title::after { content:""; flex:1; height:1px; background: linear-gradient(90deg, rgba(244,172,183,0.6), transparent); }

/* about card */
.about-card {
    background: white; border-radius: 16px; padding: 1.5rem 1.6rem;
    border: 1px solid rgba(244,172,183,0.25); box-shadow: 0 2px 12px rgba(157,129,137,0.07);
    line-height: 1.85; color: #5a4a4e; font-size: 0.93rem; margin-bottom: 1.2rem;
}

/* skill bar */
.skill-row { margin-bottom: 0.9rem; }
.skill-hd { display: flex; justify-content: space-between; margin-bottom: 0.3rem; align-items: baseline; }
.skill-name { font-weight: 600; font-size: 0.88rem; color: #3a2e30; }
.skill-pct  { font-size: 0.78rem; color: #9d8189; font-weight: 700; }
.skill-bg   { background: #f5f0f1; border-radius: 99px; height: 7px; overflow: hidden; }
.skill-fill { height: 100%; border-radius: 99px; background: linear-gradient(90deg, #ffcad4, #9d8189); }

/* tag */
.tag     { display: inline-block; background: #ffcad4; color: #9d8189; border-radius: 20px; font-size: 0.77rem; font-weight: 700; padding: 0.22rem 0.72rem; margin: 0.18rem 0.12rem; }
.tag-dk  { background: #9d8189; color: white; }
.tag-sm  { background: #ffe5d9; color: #9d8189; border: 1px solid #f4acb7; }

/* lib grid */
.lib-grid { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.6rem; }
.lib-item { background: #f5f0f1; border-radius: 8px; padding: 0.28rem 0.65rem; font-size: 0.78rem; font-weight: 600; color: #9d8189; font-family: monospace; }

/* timeline */
.tl-wrap { position: relative; padding-left: 2.2rem; }
.tl-wrap::before {
    content:""; position:absolute; left:7px; top:10px; bottom:0; width:2px;
    background: linear-gradient(to bottom, #f4acb7 0%, #d8e2dc 100%);
}
.tl-item { position: relative; margin-bottom: 1.6rem; }
.tl-dot {
    position: absolute; left:-2.2rem; top:8px;
    width:16px; height:16px; border-radius:50%;
    background: white; border: 3px solid #f4acb7;
    box-shadow: 0 0 0 4px rgba(244,172,183,0.18);
}
.tl-dot.cur { background: #9d8189; border-color: #9d8189; box-shadow: 0 0 0 4px rgba(157,129,137,0.18); }
.tl-box {
    background: white; border-radius: 14px; padding: 1.1rem 1.3rem;
    border: 1px solid rgba(244,172,183,0.28); box-shadow: 0 2px 10px rgba(157,129,137,0.07);
}
.tl-period { font-size: 0.74rem; color: #9d8189; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 0.3rem; }
.tl-company { font-size: 1rem; font-weight: 800; color: #3a2e30; margin-bottom: 0.15rem; }
.tl-role    { font-size: 0.83rem; color: #9d8189; font-weight: 600; margin-bottom: 0.6rem; display: inline-block; background: #fff0f3; border-radius: 6px; padding: 0.1rem 0.55rem; }
.tl-desc    { font-size: 0.86rem; color: #666; line-height: 1.75; margin-bottom: 0.6rem; }

/* project card */
.proj-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 1rem; }
.proj-card {
    background: white; border-radius: 16px; padding: 1.4rem;
    border: 1px solid rgba(244,172,183,0.25); box-shadow: 0 2px 12px rgba(157,129,137,0.07);
    display: flex; flex-direction: column; gap: 0.5rem;
    transition: box-shadow 0.2s, transform 0.2s;
}
.proj-card:hover { box-shadow: 0 8px 28px rgba(157,129,137,0.15); transform: translateY(-3px); }
.proj-no   { font-size: 0.7rem; font-weight: 800; color: #f4acb7; letter-spacing: 0.1em; text-transform: uppercase; }
.proj-name { font-size: 1rem; font-weight: 800; color: #3a2e30; line-height: 1.3; }
.proj-meta { font-size: 0.75rem; color: #bbb; }
.proj-desc { font-size: 0.84rem; color: #666; line-height: 1.75; flex: 1; }
.proj-kpi  {
    display: inline-block; background: linear-gradient(135deg, #ffe5d9, #ffcad4);
    color: #9d8189; border-radius: 8px; padding: 0.35rem 0.75rem;
    font-size: 0.78rem; font-weight: 800; border: 1px solid #f4acb7;
}

/* info card */
.info-card { background: white; border-radius: 16px; padding: 1.4rem; border: 1px solid rgba(244,172,183,0.28); box-shadow: 0 2px 12px rgba(157,129,137,0.07); }
.info-row  { display: flex; align-items: center; gap: 0.8rem; padding: 0.6rem 0; border-bottom: 1px solid rgba(244,172,183,0.2); font-size: 0.88rem; color: #5a4a4e; }
.info-row:last-child { border-bottom: none; padding-bottom: 0; }
.info-icon  { font-size: 1rem; width: 1.4rem; flex-shrink: 0; }
.info-label { font-weight: 700; color: #9d8189; min-width: 55px; font-size: 0.74rem; letter-spacing: 0.04em; text-transform: uppercase; }
.info-val a { color: #9d8189; text-decoration: none; font-weight: 600; }
.info-val a:hover { text-decoration: underline; }

/* cert badge */
.cert { display: flex; align-items: center; gap: 0.6rem; padding: 0.65rem 0.9rem; border-radius: 12px; margin-bottom: 0.5rem; font-size: 0.87rem; font-weight: 600; }
.cert.done { background: #ffe5d9; color: #9d8189; border: 1px solid #f4acb7; }
.cert.wip  { background: #f5f0f1; color: #aaa;    border: 1px solid #e0d8da; }

/* ══ 모바일 반응형 ════════════════════════════════ */
@media (max-width: 768px) {
    .block-container { padding: 1rem 0.8rem 3rem !important; }
    .hero { padding: 1.6rem 1.4rem; border-radius: 16px; }
    .hero h1 { font-size: 1.55rem !important; }
    .hero p  { font-size: 0.88rem; }
    .hero-deco { display: none; }
    .hero-chips { gap: 0.3rem; }
    .hero-chip  { font-size: 0.74rem; padding: 0.22rem 0.65rem; }
    .stats-grid { grid-template-columns: repeat(2, 1fr); gap: 0.65rem; margin-bottom: 1.2rem; }
    .stat-v { font-size: 1.6rem; }
    .proj-grid  { grid-template-columns: 1fr; }
    .tl-wrap    { padding-left: 1.5rem; }
    .tl-dot     { left: -1.5rem; }
    .sec-title  { font-size: 0.95rem; }
}
@media (max-width: 480px) {
    .hero h1 { font-size: 1.3rem !important; }
    .stats-grid { grid-template-columns: repeat(2, 1fr); gap: 0.5rem; }
    .stat-card  { padding: 1rem 0.7rem 0.8rem; }
}

/* ══ 다크모드 ════════════════════════════════════ */
@media (prefers-color-scheme: dark) {
    [data-testid="stAppViewContainer"] > .main { background: #1c1819 !important; }

    /* 카드 계열 */
    .stat-card, .about-card, .tl-box, .proj-card, .info-card {
        background: #2a2224 !important;
        border-color: rgba(244,172,183,0.15) !important;
        box-shadow: 0 2px 12px rgba(0,0,0,0.25) !important;
    }
    /* 텍스트 */
    .stat-v     { color: #f4acb7 !important; }
    .stat-l     { color: #6a5558 !important; }
    .stat-s     { color: #c4848f !important; }
    .tl-company, .proj-name, .sec-title { color: #eddadd !important; }
    .tl-desc, .proj-desc, .about-card   { color: #a88e92 !important; }
    .tl-period, .tl-role, .proj-no      { color: #c4848f !important; }
    .proj-meta  { color: #6a5558 !important; }
    .skill-name { color: #d4bfc2 !important; }
    .info-label { color: #c4848f !important; }
    .info-row   { color: #b09498 !important; border-color: rgba(244,172,183,0.1) !important; }
    /* 스킬바 배경 */
    .skill-bg   { background: #3a2e30 !important; }
    /* 라이브러리 배지 */
    .lib-item   { background: #3a2e30 !important; color: #f4acb7 !important; }
    /* 자격증 */
    .cert.wip   { background: #2a2224 !important; color: #6a5558 !important; border-color: #3a2e30 !important; }
    .cert.done  { background: #3a2224 !important; border-color: #6a3a42 !important; }
    /* 섹션 타이틀 구분선 */
    .sec-title::after { background: linear-gradient(90deg, rgba(244,172,183,0.4), transparent) !important; }
    /* 프로젝트 KPI */
    .proj-kpi   { background: #3a2224 !important; border-color: #6a3a42 !important; }
    /* 사이드바 */
    [data-testid="stSidebar"] { background: #1a1416 !important; }
    [data-testid="stSidebar"] .stMarkdown a { color: #f4acb7 !important; }
}
</style>
""", unsafe_allow_html=True)

# ── 사이드바 ──────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 0.5rem 0 1rem;">
        <div style="width:120px; height:120px; border-radius:50%; border:4px solid #f4acb7; box-shadow:0 6px 20px rgba(157,129,137,0.22); background:#ffe5d9; display:flex; align-items:center; justify-content:center; margin:0 auto;">
            <svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#f4acb7" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/>
            </svg>
        </div>
        <div style="margin-top:0.8rem; font-size:1.2rem; font-weight:900; color:#3a2e30; letter-spacing:-0.02em;">이지원</div>
        <div style="font-size:0.82rem; color:#9d8189; font-weight:600; margin-top:0.15rem; letter-spacing:0.04em;">FULL-STACK DEVELOPER</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:rgba(255,255,255,0.45); border-radius:12px; padding:0.9rem 1rem; margin-bottom:1rem; border:1px solid rgba(244,172,183,0.3);">
        <div style="font-size:0.72rem; font-weight:800; color:#9d8189; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:0.6rem;">CONTACT</div>
        <div style="display:flex; gap:0.5rem; align-items:center; font-size:0.84rem; color:#5a4a4e; margin-bottom:0.4rem;">
            <span>📧</span> <span>zwnfkko@gmail.com</span>
        </div>
        <div style="display:flex; gap:0.5rem; align-items:center; font-size:0.84rem; color:#5a4a4e; margin-bottom:0.4rem;">
            <span>📱</span> <span>010-1234-5678</span>
        </div>
        <div style="display:flex; gap:0.5rem; align-items:center; font-size:0.84rem;">
            <span>🐙</span> <a href="https://github.com/zwnfkko" style="color:#9d8189; font-weight:600; text-decoration:none;">github.com/zwnfkko</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    menu = st.radio("메뉴", ["🏠  홈", "💼  경력", "🛠️  기술스택", "📂  프로젝트", "📬  연락하기"], label_visibility="collapsed")

# ── Hero ──────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-deco" style="width:200px;height:200px;background:rgba(255,255,255,0.07);top:-60px;right:80px;"></div>
    <div class="hero-deco" style="width:120px;height:120px;background:rgba(255,202,212,0.15);bottom:-30px;right:30px;"></div>
    <div class="hero-deco" style="width:70px;height:70px;background:rgba(255,255,255,0.06);top:30px;right:260px;"></div>
    <h1>안녕하세요, 이지원입니다 🌸</h1>
    <p>풀스택 개발자 · 데이터 분석가 · 문제 해결사</p>
    <div class="hero-chips">
        <span class="hero-chip">Python</span>
        <span class="hero-chip">React</span>
        <span class="hero-chip">FastAPI</span>
        <span class="hero-chip">Data Analysis</span>
        <span class="hero-chip">Seoul, Korea</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── 홈 ────────────────────────────────────────────────
if menu == "🏠  홈":
    st.markdown("""
    <div class="stats-grid">
        <div class="stat-card"><div class="stat-v">3년</div><div class="stat-l">경력</div><div class="stat-s">신입 → 주니어</div></div>
        <div class="stat-card"><div class="stat-v">12개</div><div class="stat-l">완료 프로젝트</div><div class="stat-s">+3 올해</div></div>
        <div class="stat-card"><div class="stat-v">5가지</div><div class="stat-l">사용 언어</div><div class="stat-s">Python, JS 외</div></div>
        <div class="stat-card"><div class="stat-v">3개</div><div class="stat-l">자격증</div><div class="stat-s">최근 취득</div></div>
    </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([3, 2], gap="large")

    with col_left:
        st.markdown('<p class="sec-title">👤 소개</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="about-card">
            안녕하세요! 저는 <strong style="color:#9d8189;">이지원</strong>입니다.<br><br>
            사용자 경험을 최우선으로 생각하는 <strong style="color:#9d8189;">풀스택 개발자</strong>로,
            백엔드부터 프론트엔드, 데이터 분석까지 폭넓게 다룹니다.<br><br>
            새로운 기술을 빠르게 습득하고 팀과 협력하여 문제를 해결하는 것을 즐깁니다.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<p class="sec-title">🎓 학력</p>', unsafe_allow_html=True)
        st.markdown("""
        | 기간 | 학교 | 전공 | 학위 |
        |------|------|------|------|
        | 2018 – 2022 | ○○대학교 | 컴퓨터공학과 | 학사 |
        | 2022 – 2024 | ○○대학원 | 소프트웨어공학 | 석사 |
        """)

    with col_right:
        st.markdown('<p class="sec-title">🌟 핵심 역량</p>', unsafe_allow_html=True)
        competencies = [
            ("문제 해결력", 90), ("커뮤니케이션", 85),
            ("팀워크", 95), ("자기 학습", 88), ("창의성", 80),
        ]
        bars = "".join([f"""
        <div class="skill-row">
            <div class="skill-hd"><span class="skill-name">{n}</span><span class="skill-pct">{v}%</span></div>
            <div class="skill-bg"><div class="skill-fill" style="width:{v}%"></div></div>
        </div>""" for n, v in competencies])
        st.markdown(f'<div style="background:white;border-radius:16px;padding:1.4rem;border:1px solid rgba(244,172,183,0.25);box-shadow:0 2px 12px rgba(157,129,137,0.07);">{bars}</div>', unsafe_allow_html=True)

# ── 경력 ──────────────────────────────────────────────
elif menu == "💼  경력":
    st.markdown('<p class="sec-title">💼 경력 사항</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="tl-wrap">
        <div class="tl-item">
            <div class="tl-dot cur"></div>
            <div class="tl-box">
                <div class="tl-period">2024.03 – 현재</div>
                <div class="tl-company">(주) ABC테크</div>
                <span class="tl-role">백엔드 개발자</span>
                <div class="tl-desc">FastAPI 기반 RESTful API 설계 및 개발, PostgreSQL DB 최적화, CI/CD 파이프라인 구축</div>
                <div>
                    <span class="tag tag-dk">Python</span><span class="tag tag-dk">FastAPI</span>
                    <span class="tag tag-dk">PostgreSQL</span><span class="tag tag-dk">Docker</span><span class="tag tag-dk">AWS</span>
                </div>
            </div>
        </div>
        <div class="tl-item">
            <div class="tl-dot"></div>
            <div class="tl-box">
                <div class="tl-period">2022.07 – 2024.02</div>
                <div class="tl-company">(주) DEF솔루션</div>
                <span class="tl-role">풀스택 개발자</span>
                <div class="tl-desc">React + Django 기반 사내 ERP 시스템 개발, 데이터 시각화 대시보드 구축</div>
                <div>
                    <span class="tag tag-dk">React</span><span class="tag tag-dk">Django</span>
                    <span class="tag tag-dk">MySQL</span><span class="tag tag-dk">Chart.js</span>
                </div>
            </div>
        </div>
        <div class="tl-item">
            <div class="tl-dot"></div>
            <div class="tl-box">
                <div class="tl-period">2021.01 – 2022.06</div>
                <div class="tl-company">GHI스타트업</div>
                <span class="tl-role">인턴 개발자</span>
                <div class="tl-desc">Python 데이터 파이프라인 개발, Streamlit 대시보드 프로토타이핑</div>
                <div>
                    <span class="tag tag-dk">Python</span><span class="tag tag-dk">Pandas</span><span class="tag tag-dk">Streamlit</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── 기술스택 ───────────────────────────────────────────
elif menu == "🛠️  기술스택":
    st.markdown('<p class="sec-title">🛠️ 기술 스택</p>', unsafe_allow_html=True)
    tab1, tab2, tab3, tab4 = st.tabs(["🐍  백엔드", "🎨  프론트엔드", "🗄️  데이터베이스", "⚙️  DevOps"])

    def skill_bars(items):
        return "".join([f"""
        <div class="skill-row">
            <div class="skill-hd"><span class="skill-name">{n}</span><span class="skill-pct">{v}%</span></div>
            <div class="skill-bg"><div class="skill-fill" style="width:{v}%"></div></div>
        </div>""" for n, v in items])

    def lib_grid(libs):
        items = "".join([f'<span class="lib-item">{l}</span>' for l in libs])
        return f'<div class="lib-grid">{items}</div>'

    with tab1:
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.markdown(skill_bars([("Python", 90), ("FastAPI", 80), ("Django", 75), ("Node.js", 65)]), unsafe_allow_html=True)
        with col2:
            st.markdown(f'<p style="font-size:0.82rem;font-weight:800;color:#9d8189;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:0.4rem;">주요 라이브러리</p>{lib_grid(["Pandas","NumPy","SQLAlchemy","Pydantic","Celery","Streamlit"])}', unsafe_allow_html=True)

    with tab2:
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.markdown(skill_bars([("React", 80), ("TypeScript", 70), ("HTML/CSS", 85), ("Vue.js", 55)]), unsafe_allow_html=True)
        with col2:
            st.markdown(f'<p style="font-size:0.82rem;font-weight:800;color:#9d8189;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:0.4rem;">주요 라이브러리</p>{lib_grid(["Redux","Tailwind CSS","Chart.js","Axios"])}', unsafe_allow_html=True)

    with tab3:
        st.markdown(skill_bars([("PostgreSQL", 85), ("MySQL", 80), ("MongoDB", 65), ("Redis", 60)]), unsafe_allow_html=True)

    with tab4:
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.markdown(skill_bars([("Docker", 75), ("AWS", 65), ("Linux", 80), ("Git", 90)]), unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <p style="font-size:0.82rem;font-weight:800;color:#9d8189;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:0.8rem;">자격증</p>
            <div class="cert done">✅ AWS Solutions Architect Associate</div>
            <div class="cert done">✅ 정보처리기사</div>
            <div class="cert wip">🔄 CKAD (취득 준비 중)</div>
            """, unsafe_allow_html=True)

# ── 프로젝트 ───────────────────────────────────────────
elif menu == "📂  프로젝트":
    st.markdown('<p class="sec-title">📂 주요 프로젝트</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="proj-grid">
        <div class="proj-card">
            <div class="proj-no">Project 01</div>
            <div class="proj-name">실시간 주식 대시보드</div>
            <div class="proj-meta">📅 2024.06 – 2024.09 &nbsp;|&nbsp; 👤 개인 프로젝트</div>
            <div class="proj-desc">WebSocket으로 실시간 주가 데이터를 수신하여 Streamlit으로 시각화하는 대시보드. 포트폴리오 수익률 분석 기능 포함.</div>
            <div>
                <span class="tag">Python</span><span class="tag">Streamlit</span>
                <span class="tag">WebSocket</span><span class="tag">Plotly</span>
            </div>
            <div class="proj-kpi">📈 일 평균 200명 사용</div>
        </div>
        <div class="proj-card">
            <div class="proj-no">Project 02</div>
            <div class="proj-name">사내 ERP 시스템</div>
            <div class="proj-meta">📅 2023.01 – 2023.12 &nbsp;|&nbsp; 👤 팀 리드 (4인)</div>
            <div class="proj-desc">중소기업용 맞춤형 ERP 시스템. 인사·재무·재고 관리 모듈을 통합하여 업무 효율 향상.</div>
            <div>
                <span class="tag">React</span><span class="tag">Django</span>
                <span class="tag">MySQL</span><span class="tag">Docker</span>
            </div>
            <div class="proj-kpi">🚀 업무 효율 40% 향상</div>
        </div>
        <div class="proj-card">
            <div class="proj-no">Project 03</div>
            <div class="proj-name">AI 챗봇 고객센터</div>
            <div class="proj-meta">📅 2024.01 – 2024.04 &nbsp;|&nbsp; 👤 백엔드 담당</div>
            <div class="proj-desc">LLM 기반 고객 응대 챗봇. FAQ 자동 응답 및 상담사 연결 기능 구현.</div>
            <div>
                <span class="tag">Python</span><span class="tag">LangChain</span>
                <span class="tag">FastAPI</span><span class="tag">Redis</span>
            </div>
            <div class="proj-kpi">⚡ 대기 시간 60% 단축</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── 연락하기 ───────────────────────────────────────────
elif menu == "📬  연락하기":
    st.markdown('<p class="sec-title">📬 연락하기</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown('<p style="font-size:0.82rem;font-weight:800;color:#9d8189;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:0.8rem;">메시지 보내기</p>', unsafe_allow_html=True)
        with st.form("contact_form"):
            name    = st.text_input("이름")
            email   = st.text_input("이메일")
            subject = st.selectbox("문의 유형", ["협업 제안", "채용 문의", "기술 질문", "기타"])
            message = st.text_area("메시지", height=140, placeholder="내용을 입력해주세요.")
            submitted = st.form_submit_button("전송하기 →", type="primary", use_container_width=True)
            if submitted:
                if name and email and message:
                    st.success(f"✅ {name}님, 메시지가 전송되었습니다! 빠른 시일 내에 답변 드리겠습니다.")
                else:
                    st.error("이름, 이메일, 메시지를 모두 입력해주세요.")

    with col2:
        st.markdown('<p style="font-size:0.82rem;font-weight:800;color:#9d8189;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:0.8rem;">연락처 정보</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="info-card">
            <div class="info-row">
                <span class="info-icon">📧</span>
                <span class="info-label">Email</span>
                <span class="info-val">zwnfkko@gmail.com</span>
            </div>
            <div class="info-row">
                <span class="info-icon">📱</span>
                <span class="info-label">Phone</span>
                <span class="info-val">010-1234-5678</span>
            </div>
            <div class="info-row">
                <span class="info-icon">🐙</span>
                <span class="info-label">GitHub</span>
                <span class="info-val"><a href="https://github.com/zwnfkko" target="_blank">github.com/zwnfkko</a></span>
            </div>
            <div class="info-row">
                <span class="info-icon">💼</span>
                <span class="info-label">LinkedIn</span>
                <span class="info-val"><a href="#" target="_blank">linkedin.com/in/jiwon</a></span>
            </div>
            <div class="info-row">
                <span class="info-icon">📍</span>
                <span class="info-label">Location</span>
                <span class="info-val">서울특별시</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="margin-top:1rem; background:linear-gradient(135deg,#ffe5d9,#ffcad4); border-radius:12px; padding:1rem 1.2rem; border:1px solid #f4acb7;">
            <div style="font-size:0.8rem; font-weight:800; color:#9d8189; letter-spacing:0.06em; text-transform:uppercase; margin-bottom:0.4rem;">응답 가능 시간</div>
            <div style="font-size:0.88rem; color:#5a4a4e; line-height:1.7;">
                ⏰ 평일 오전 10시 ~ 오후 6시<br>
                <span style="color:#9d8189; font-weight:600;">보통 24시간 이내 답변드립니다.</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
