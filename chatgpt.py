import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Pahaar Trails | Explore Pakistan",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# GLOBAL CSS
# NOTE:
# No HTML div wrappers are used for Streamlit widgets.
# CSS only styles Streamlit's native components.
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');


/* ============================================================
   GLOBAL
   ============================================================ */

html, body, [class*="css"] {
    font-family: "DM Sans", sans-serif;
}

.stApp {
    background:
        linear-gradient(
            135deg,
            rgba(4, 18, 20, 0.98),
            rgba(7, 31, 31, 0.96)
        );
    color: #f4f7f6;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.block-container {
    max-width: 1280px;
    padding-top: 1.2rem;
    padding-bottom: 4rem;
}


/* ============================================================
   TYPOGRAPHY
   ============================================================ */

h1, h2, h3 {
    font-family: "Playfair Display", serif !important;
    color: #ffffff !important;
}

p, span, label {
    color: inherit;
}


/* ============================================================
   API KEY SCREEN
   ============================================================ */

.key-screen {
    max-width: 700px;
    margin: 7vh auto 0 auto;
    padding: 48px 42px;
    border-radius: 30px;
    text-align: center;
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.09),
            rgba(255,255,255,0.035)
        );
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 30px 90px rgba(0,0,0,0.45);
}

.key-icon {
    font-size: 52px;
    margin-bottom: 10px;
}

.key-brand {
    font-family: "Playfair Display", serif;
    font-size: 44px;
    font-weight: 700;
    letter-spacing: 1px;
}

.gold {
    color: #d8b66d !important;
}

.key-tagline {
    color: #9eafab !important;
    font-size: 13px;
    margin-top: 5px;
}

.key-title {
    font-family: "Playfair Display", serif;
    font-size: 30px;
    margin-top: 40px;
    color: #ffffff !important;
}

.key-text {
    max-width: 530px;
    margin: 12px auto 25px auto;
    color: #aebdb9 !important;
    font-size: 14px;
    line-height: 1.8;
}


/* API INPUT */

div[data-testid="stTextInput"] {
    margin-top: 5px;
}

div[data-testid="stTextInput"] label {
    color: #aebdb9 !important;
    font-size: 12px !important;
    font-weight: 600 !important;
}

div[data-testid="stTextInput"] input {
    min-height: 52px !important;
    padding: 13px 15px !important;
    border-radius: 14px !important;

    background: rgba(255,255,255,0.08) !important;

    border: 1px solid rgba(255,255,255,0.17) !important;

    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;

    font-size: 14px !important;
}

div[data-testid="stTextInput"] input::placeholder {
    color: #9caeaa !important;
    opacity: 1 !important;
}

div[data-testid="stTextInput"] input:focus {
    border-color: #d8b66d !important;
    box-shadow: 0 0 0 1px #d8b66d !important;
}


/* ============================================================
   ALL BUTTONS
   ============================================================ */

.stButton > button {
    min-height: 45px !important;

    border-radius: 12px !important;

    border: 1px solid rgba(255,255,255,0.10) !important;

    background: rgba(255,255,255,0.055) !important;

    color: #f1f5f4 !important;

    font-family: "DM Sans", sans-serif !important;

    font-weight: 600 !important;

    transition:
        transform 0.2s ease,
        background 0.2s ease,
        border-color 0.2s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px);

    background: rgba(216,182,109,0.12) !important;

    border-color: rgba(216,182,109,0.45) !important;

    color: #d8b66d !important;
}


/* ============================================================
   KEY START BUTTON
   ============================================================ */

.st-key-key_start .stButton > button {
    width: 100% !important;

    margin-top: 10px !important;

    min-height: 54px !important;

    border: none !important;

    background:
        linear-gradient(
            135deg,
            #d8b66d,
            #b88d4a
        ) !important;

    color: #12231f !important;

    font-size: 14px !important;

    font-weight: 700 !important;

    box-shadow: 0 15px 35px rgba(216,182,109,0.12);
}

.st-key-key_start .stButton > button:hover {
    color: #12231f !important;

    background:
        linear-gradient(
            135deg,
            #e5c77e,
            #c39a58
        ) !important;

    transform: translateY(-3px);
}

.key-security {
    color: #697b77 !important;
    font-size: 11px;
    text-align: center;
    margin-top: 18px;
    line-height: 1.7;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background: #061719 !important;
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] .block-container {
    padding: 25px 17px;
}

.sidebar-logo {
    text-align: center;
    font-size: 39px;
    margin-bottom: 5px;
}

.sidebar-brand {
    text-align: center;
    font-family: "Playfair Display", serif;
    font-size: 23px;
    font-weight: 700;
}

.sidebar-tagline {
    text-align: center;
    color: #71817e !important;
    font-size: 10px;
    margin-top: 4px;
    margin-bottom: 25px;
}

.sidebar-section {
    color: #657875 !important;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.7px;
    margin-top: 23px;
    margin-bottom: 8px;
}

section[data-testid="stSidebar"] .stButton > button {
    text-align: left !important;
    padding: 10px 12px !important;
    min-height: 43px !important;
    margin-bottom: 4px !important;
}

section[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.08) !important;
}


/* ============================================================
   TOP BAR
   ============================================================ */

.top-brand {
    font-family: "Playfair Display", serif;
    font-size: 26px;
    font-weight: 700;
}

.top-caption {
    color: #778985 !important;
    font-size: 11px;
    margin-top: -4px;
}

.badge {
    text-align: right;
    color: #d8b66d !important;
    font-size: 11px;
    font-weight: 700;
    padding-top: 8px;
}


/* ============================================================
   HOME HERO
   ============================================================ */

.hero-box {
    min-height: 430px;

    margin-top: 10px;

    padding: 65px 35px;

    border-radius: 30px;

    text-align: center;

    display: flex;
    flex-direction: column;
    justify-content: center;

    background:
        linear-gradient(
            180deg,
            rgba(6,28,29,0.35),
            rgba(3,16,18,0.94)
        );

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow: 0 30px 80px rgba(0,0,0,0.35);
}

.hero-kicker {
    color: #d8b66d !important;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
}

.hero-title {
    font-family: "Playfair Display", serif;
    font-size: clamp(40px, 6vw, 72px);
    line-height: 1.02;
    margin: 17px 0 0 0;
    color: #ffffff !important;
}

.hero-text {
    max-width: 670px;
    margin: 22px auto 0 auto;
    color: #b8c7c3 !important;
    font-size: 14px;
    line-height: 1.8;
}


/* ============================================================
   PLANNER CARD
   IMPORTANT:
   This is NOT an HTML wrapper around Streamlit widgets.
   It is just a styled Streamlit container.
   ============================================================ */

.st-key-planner_card {
    margin-top: 24px;
    padding: 18px;
    border-radius: 19px;
    background: #f7f8f7;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 20px 50px rgba(0,0,0,0.28);
}


/* Make home planner input readable */

.st-key-planner_card div[data-testid="stTextInput"] {
    margin-top: 0;
}

.st-key-planner_card div[data-testid="stTextInput"] label {
    color: #465552 !important;
}

.st-key-planner_card div[data-testid="stTextInput"] input {
    min-height: 52px !important;

    background: #ffffff !important;

    border: 1px solid #d6ddda !important;

    color: #17201f !important;

    -webkit-text-fill-color: #17201f !important;

    font-size: 15px !important;
}

.st-key-planner_card div[data-testid="stTextInput"] input::placeholder {
    color: #6d7b78 !important;
    -webkit-text-fill-color: #6d7b78 !important;
    opacity: 1 !important;
}

.st-key-planner_card .stButton > button {
    min-height: 52px !important;

    margin-top: 28px !important;

    border: none !important;

    background: #173f3c !important;

    color: #ffffff !important;

    font-weight: 700 !important;
}

.st-key-planner_card .stButton > button:hover {
    background: #d8b66d !important;

    color: #14221f !important;
}


/* ============================================================
   QUICK ACTIONS
   ============================================================ */

.quick-label {
    text-align: center;
    color: #71817e !important;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin: 18px 0 8px 0;
}


/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-kicker {
    color: #d8b66d !important;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-top: 55px;
}

.section-title {
    font-family: "Playfair Display", serif;
    color: #ffffff !important;
    font-size: 36px;
    margin-top: 4px;
}

.section-text {
    color: #8f9f9b !important;
    font-size: 13px;
    line-height: 1.7;
    max-width: 620px;
}


/* ============================================================
   DESTINATION CARDS
   ============================================================ */

/*
   st.image() has no class hook of its own, so the destination photo
   is styled via Streamlit's rendered markup directly. This is the
   only place st.image() is used in the app, so the selector is safe
   to apply globally. Fixed height + object-fit keeps every card the
   same size regardless of each source photo's original aspect ratio.
*/
div[data-testid="stImage"] img {
    width: 100%;
    height: 230px;
    object-fit: cover;
    border-radius: 19px;
}

.destination-name {
    font-family: "Playfair Display", serif;
    font-size: 24px;
    color: #ffffff !important;
    margin-top: 8px;
}

.destination-region {
    color: #d8b66d !important;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.4px;
}

.destination-description {
    color: #91a09d !important;
    font-size: 11px;
    line-height: 1.6;
    min-height: 35px;
}


/* ============================================================
   FEATURE CARDS
   ============================================================ */

.feature-box {
    min-height: 170px;
    padding: 25px;
    border-radius: 19px;
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.08);
}

.feature-icon {
    font-size: 27px;
}

.feature-title {
    color: #ffffff !important;
    font-size: 15px;
    font-weight: 700;
    margin-top: 10px;
}

.feature-text {
    color: #909f9c !important;
    font-size: 11px;
    line-height: 1.7;
    margin-top: 6px;
}


/* ============================================================
   STATS
   ============================================================ */

.stat-box {
    text-align: center;
    padding: 23px 10px;
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.06);
}

.stat-number {
    font-family: "Playfair Display", serif;
    font-size: 27px;
    color: #d8b66d !important;
}

.stat-label {
    color: #71817e !important;
    font-size: 9px;
    margin-top: 3px;
}


/* ============================================================
   CHAT PAGE
   ============================================================ */

.chat-title {
    font-family: "Playfair Display", serif;
    font-size: 32px;
    color: #ffffff !important;
}

.chat-subtitle {
    color: #8f9f9b !important;
    font-size: 12px;
    line-height: 1.6;
}


/* Chat messages */

div[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.055) !important;

    border:
        1px solid rgba(255,255,255,0.08) !important;

    border-radius: 17px !important;

    margin-bottom: 10px !important;
}

div[data-testid="stChatMessage"] p,
div[data-testid="stChatMessage"] li {
    color: #edf3f1 !important;

    font-size: 14px !important;

    line-height: 1.75 !important;
}


/* ============================================================
   CHAT INPUT
   ============================================================ */

div[data-testid="stChatInput"] {
    background: #ffffff !important;

    border-radius: 17px !important;

    border: 1px solid #d9dfdd !important;

    box-shadow: 0 18px 50px rgba(0,0,0,0.25) !important;
}

div[data-testid="stChatInput"] textarea {
    color: #17201f !important;

    -webkit-text-fill-color: #17201f !important;

    font-size: 14px !important;

    caret-color: #173f3c !important;
}

div[data-testid="stChatInput"] textarea::placeholder {
    color: #657471 !important;

    -webkit-text-fill-color: #657471 !important;

    opacity: 1 !important;
}

div[data-testid="stChatInput"] button {
    color: #173f3c !important;
}


/* ============================================================
   SELECT BOXES / NUMBER INPUTS
   ============================================================ */

div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.06) !important;

    border-color: rgba(255,255,255,0.12) !important;

    color: #ffffff !important;

    border-radius: 11px !important;
}

div[data-testid="stNumberInput"] input {
    background: rgba(255,255,255,0.06) !important;

    color: #ffffff !important;

    -webkit-text-fill-color: #ffffff !important;
}


/* ============================================================
   BUDGET CARD
   ============================================================ */

.st-key-budget_box {
    padding: 28px;
    border-radius: 22px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer-line {
    margin-top: 65px;
    padding-top: 25px;
    border-top: 1px solid rgba(255,255,255,0.07);
    text-align: center;
    color: #647571 !important;
    font-size: 10px;
}

.footer-brand {
    font-family: "Playfair Display", serif;
    color: #d8b66d !important;
    font-size: 20px;
    margin-bottom: 4px;
}


/* ============================================================
   RESPONSIVE
   ============================================================ */

@media (max-width: 800px) {

    .key-screen {
        margin-top: 3vh;
        padding: 35px 20px;
    }

    .key-brand {
        font-size: 34px;
    }

    .hero-box {
        min-height: 480px;
        padding: 45px 20px;
    }

    .hero-title {
        font-size: 43px;
    }

    .section-title {
        font-size: 30px;
    }

}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
You are Pahaar Trails AI, a professional travel assistant
specializing exclusively in domestic travel and tourism within Pakistan.

Your purpose is to help travelers discover Pakistan and plan practical,
memorable journeys.

You can help with:

- Destinations in Pakistan
- Hunza
- Skardu
- Gilgit
- Naran
- Kaghan
- Swat
- Kalam
- Murree
- Chitral
- Neelum Valley
- Azad Kashmir
- Fairy Meadows
- Islamabad
- Lahore
- Karachi
- Northern Pakistan
- Historical places
- Cultural tourism
- Family trips
- Solo trips
- Group trips
- Weekend trips
- Road trips
- Multi-day itineraries
- Day trips
- Hotels and accommodation
- Guest houses
- Resorts
- Camping
- Hiking
- Trekking
- Sightseeing
- Adventure tourism
- Local food
- Transportation
- Routes and distances
- Estimated travel times
- Travel budgets
- Hotel budgets
- Food budgets
- Transportation budgets
- Best time to visit
- Seasonal travel
- Snowfall destinations
- Packing
- General domestic travel preparation

IMPORTANT DOMAIN RULE:

Only answer questions related to domestic travel and tourism within Pakistan.

If the user asks something unrelated, say:

"I'm sorry, I can only help with domestic travel and tourism in Pakistan.
Please ask me something related to destinations, trip planning, hotels,
transportation, budgets, attractions, or tourism within Pakistan."

Do not provide international travel advice.

Never pretend that you have real-time information if you do not.

Do not invent:
- Hotel availability
- Exact current prices
- Current road conditions
- Current weather
- Opening hours
- Current transportation schedules

When information may change, clearly tell the traveler to verify
the latest information before travelling.

For trip planning:

- Keep answers practical and easy to understand.
- Use day-by-day itineraries where useful.
- Give estimated costs clearly.
- Separate budget categories.
- Mention assumptions.
- Prioritize realistic travel plans.
"""


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "api_key": "",
    "authenticated": False,
    "page": "home",
    "messages": [SystemMessage(content=SYSTEM_PROMPT)],
    "journey_history": [],
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def render_html(html):
    """
    Render a raw HTML string with Streamlit.

    Streamlit's markdown renderer follows CommonMark, which treats any
    line indented by 4+ spaces as a literal (escaped) code block. HTML
    written inside indented multi-line Python strings inherits that
    indentation, so `unsafe_allow_html=True` alone does not stop the
    tags from showing up as visible text. Stripping each line before
    handing it to st.markdown avoids the code-block interpretation
    without changing the HTML itself.
    """
    normalized = "\n".join(
        line.strip() for line in html.strip().splitlines()
    )
    st.markdown(normalized, unsafe_allow_html=True)


def reset_chat():
    st.session_state.messages = [
        SystemMessage(content=SYSTEM_PROMPT)
    ]


def add_user_request(text):
    text = text.strip()

    if not text:
        return

    st.session_state.messages.append(
        HumanMessage(content=text)
    )

    title = text.replace("\n", " ")

    if len(title) > 55:
        title = title[:55] + "..."

    st.session_state.journey_history.append(title)


def ask_ai():
    """
    Send current conversation to OpenAI.
    """

    chat = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        api_key=st.session_state.api_key,
    )

    return chat.invoke(
        st.session_state.messages
    )


def go_to_planner_with_request(text):
    add_user_request(text)
    st.session_state.page = "planner"
    st.rerun()


# ============================================================
# API KEY FIRST SCREEN
# ============================================================

if not st.session_state.authenticated:

    render_html(
        """
        <div class="key-screen">

    <div class="key-icon">🏔️</div>

     <div class="key-brand">
        PAHAAR <span class="gold">TRAILS</span>
        </div>

    <div class="key-tagline">
     AI-powered travel planning for Pakistan
     </div>

     <div class="key-title">
     Your journey starts here.
       </div>

      <div class="key-text">
             Enter your OpenAI API key to activate your personal
        Pahaar Trails travel assistant and start exploring
           the beauty of Pakistan.
      </div>

    </div>
        """
    )

    # Native Streamlit layout
    left, center, right = st.columns(
        [1, 2, 1]
    )

    with center:

        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here",
            help="The key is kept only in this current Streamlit session.",
        )

        with st.container(key="key_start"):

            start = st.button(
                "✨  Start Exploring Pakistan",
                use_container_width=True,
            )

        render_html(
            """
            <div class="key-security">
                🔒 Your API key is used only for this current session.
                <br>
                The application does not save it to a file.
            </div>
            """
        )

        if start:

            cleaned_key = api_key.strip()

            if not cleaned_key:

                st.error(
                    "Please enter your OpenAI API key to continue."
                )

            elif not cleaned_key.startswith("sk-"):

                st.warning(
                    "The API key format does not look correct. "
                    "Please check your OpenAI API key."
                )

            else:

                st.session_state.api_key = cleaned_key

                st.session_state.authenticated = True

                st.session_state.page = "home"

                reset_chat()

                st.rerun()

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    render_html(
        """
        <div class="sidebar-logo">🏔️</div>

        <div class="sidebar-brand">
            PAHAAR <span class="gold">TRAILS</span>
        </div>

        <div class="sidebar-tagline">
            Explore Pakistan differently.
        </div>
        """
    )

    st.markdown(
        '<div class="sidebar-section">EXPLORE</div>',
        unsafe_allow_html=True,
    )

    if st.button(
        "🏠  Home",
        use_container_width=True,
    ):
        st.session_state.page = "home"
        st.rerun()

    if st.button(
        "✨  AI Trip Planner",
        use_container_width=True,
    ):
        st.session_state.page = "planner"
        st.rerun()

    if st.button(
        "🏔️  Destinations",
        use_container_width=True,
    ):
        st.session_state.page = "destinations"
        st.rerun()

    if st.button(
        "💰  Budget Planner",
        use_container_width=True,
    ):
        st.session_state.page = "budget"
        st.rerun()

    st.markdown(
        '<div class="sidebar-section">MY JOURNEY</div>',
        unsafe_allow_html=True,
    )

    if st.button(
        "＋  New Journey",
        use_container_width=True,
    ):

        reset_chat()

        st.session_state.page = "planner"

        st.rerun()

    if st.session_state.journey_history:

        st.markdown(
            '<div class="sidebar-section">RECENT</div>',
            unsafe_allow_html=True,
        )

        for journey in reversed(
            st.session_state.journey_history[-5:]
        ):

            st.caption(
                f"💬 {journey}"
            )

    st.markdown("---")

    st.caption(
        "Plan smarter.\n\n"
        "Travel farther.\n\n"
        "Discover Pakistan."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "🔐  End Session",
        use_container_width=True,
    ):

        st.session_state.api_key = ""

        st.session_state.authenticated = False

        reset_chat()

        st.session_state.page = "home"

        st.rerun()


# ============================================================
# TOP BAR
# ============================================================

top_left, top_right = st.columns(
    [4, 1]
)

with top_left:

    render_html(
        """
        <div class="top-brand">
            PAHAAR <span class="gold">TRAILS</span>
        </div>

        <div class="top-caption">
            AI travel planning for Pakistan
        </div>
        """
    )

with top_right:

    render_html(
        """
        <div class="badge">
            🇵🇰 MADE FOR PAKISTAN
        </div>
        """
    )


# ============================================================
# DESTINATION IMAGES
# ============================================================
# Centralized destination -> photo mapping. Every entry is a real,
# name-verified photo of that exact place (Wikimedia Commons, served
# from upload.wikimedia.org: stable, direct, no API key, no
# expiring tokens). Keys are normalized (lowercase + stripped) so
# lookups tolerate case/whitespace variation (e.g. "fairy meadows",
# "Fairy Meadows", " FAIRY MEADOWS ").

DESTINATION_IMAGES = {
    "hunza": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/"
        "Ultar_Sar_from_Karimabad_Hunza_Valley_Northern_Pakistan.jpg/"
        "960px-Ultar_Sar_from_Karimabad_Hunza_Valley_Northern_Pakistan.jpg"
    ),
    "skardu": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/"
        "Chunda_valley,_Skardu.jpg/960px-Chunda_valley,_Skardu.jpg"
    ),
    "swat": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/"
        "Aerial_view_of_Swat_Valley.jpg/960px-Aerial_view_of_Swat_Valley.jpg"
    ),
    "kashmir": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/"
        "Arang_Kel,_Neelum_Valley,_Azad_Kashmir,_Pakistan.jpg/"
        "960px-Arang_Kel,_Neelum_Valley,_Azad_Kashmir,_Pakistan.jpg"
    ),
    "azad kashmir": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/"
        "Arang_Kel,_Neelum_Valley,_Azad_Kashmir,_Pakistan.jpg/"
        "960px-Arang_Kel,_Neelum_Valley,_Azad_Kashmir,_Pakistan.jpg"
    ),
    "neelum valley": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/"
        "Arang_Kel,_Neelum_Valley,_Azad_Kashmir,_Pakistan.jpg/"
        "960px-Arang_Kel,_Neelum_Valley,_Azad_Kashmir,_Pakistan.jpg"
    ),
    "naran": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/"
        "Naran_kaghan_valley_Pakistan.jpg/960px-Naran_kaghan_valley_Pakistan.jpg"
    ),
    "kaghan": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/"
        "Naran_kaghan_valley_Pakistan.jpg/960px-Naran_kaghan_valley_Pakistan.jpg"
    ),
    "fairy meadows": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/"
        "Fairy_Meadows_and_the_view_of_Nanga_Parbat.jpg/"
        "960px-Fairy_Meadows_and_the_view_of_Nanga_Parbat.jpg"
    ),
}

# Only used if a destination name has no entry above, so a missing
# mapping never breaks the layout with a broken-image icon.
FALLBACK_DESTINATION_IMAGE = (
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/"
    "Deosai_Plains_Beauty.jpg/960px-Deosai_Plains_Beauty.jpg"
)


def get_destination_image(destination_name):
    key = destination_name.strip().lower()
    return DESTINATION_IMAGES.get(key, FALLBACK_DESTINATION_IMAGE)


# ============================================================
# DESTINATION DATA
# ============================================================

destinations = [
    {
        "name": "Hunza",
        "region": "GILGIT-BALTISTAN",
        "description": "Valleys, peaks and unforgettable views.",
        "image": get_destination_image("Hunza"),
    },
    {
        "name": "Skardu",
        "region": "GILGIT-BALTISTAN",
        "description": "Lakes, mountains and high-altitude adventure.",
        "image": get_destination_image("Skardu"),
    },
    {
        "name": "Swat",
        "region": "KHYBER PAKHTUNKHWA",
        "description": "Green valleys and peaceful escapes.",
        "image": get_destination_image("Swat"),
    },
    {
        "name": "Kashmir",
        "region": "AZAD KASHMIR",
        "description": "Rivers, forests and hidden valleys.",
        "image": get_destination_image("Kashmir"),
    },
    {
        "name": "Naran",
        "region": "KAGHAN VALLEY",
        "description": "Lakes, meadows and mountain roads.",
        "image": get_destination_image("Naran"),
    },
    {
        "name": "Fairy Meadows",
        "region": "GILGIT-BALTISTAN",
        "description": "A magical gateway to Nanga Parbat.",
        "image": get_destination_image("Fairy Meadows"),
    },
]


# ============================================================
# HOME PAGE
# ============================================================

if st.session_state.page == "home":

    # --------------------------------------------------------
    # HERO
    # --------------------------------------------------------

    render_html(
        """
    <div class="hero-box">

      <div class="hero-kicker">
        YOUR PAKISTAN • YOUR JOURNEY
   </div>

    <div class="hero-title">
       Discover the <span class="gold">extraordinary</span><br>
       side of Pakistan.
        </div>

     <div class="hero-text">
      Tell us where you want to go, what you want to experience,
        and how you want to travel. Pahaar Trails turns your idea
           into a practical journey.
    </div>

    </div>
        """
    )


    # --------------------------------------------------------
    # MAIN PLANNER
    # --------------------------------------------------------

    with st.container(key="planner_card"):

        planner_left, planner_right = st.columns(
            [5, 1.5]
        )

        with planner_left:

            home_prompt = st.text_input(
                "START PLANNING YOUR JOURNEY",
                placeholder="e.g. Plan a 5-day family trip to Hunza...",
                label_visibility="visible",
                key="home_trip_input",
            )

        with planner_right:

            plan_clicked = st.button(
                "✨ Plan My Trip",
                use_container_width=True,
                key="home_plan_button",
            )


    if plan_clicked:

        if home_prompt.strip():

            go_to_planner_with_request(
                home_prompt
            )

        else:

            st.warning(
                "Tell us a little about your dream trip first."
            )


    # --------------------------------------------------------
    # QUICK QUESTIONS
    # --------------------------------------------------------

    st.markdown(
        '<div class="quick-label">TRY ONE OF THESE</div>',
        unsafe_allow_html=True,
    )

    quick_questions = [
        "🏔️  Plan a Hunza trip",
        "🏕️  Weekend adventure",
        "👨‍👩‍👧  Family vacation",
        "💰  Budget-friendly Pakistan trip",
    ]

    quick_columns = st.columns(4)

    for index, question in enumerate(
        quick_questions
    ):

        with quick_columns[index]:

            if st.button(
                question,
                use_container_width=True,
                key=f"quick_{index}",
            ):

                clean_question = question.split(
                    "  ",
                    1
                )[-1]

                go_to_planner_with_request(
                    clean_question
                )


    # --------------------------------------------------------
    # POPULAR DESTINATIONS
    # --------------------------------------------------------

    st.markdown(
    '<div class="section-kicker">START SOMEWHERE BEAUTIFUL</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
     '<div class="section-title">Popular escapes</div>',
        unsafe_allow_html=True,
    )

    render_html(
        """
     <div class="section-text">
      From high-altitude valleys to peaceful lakes,
       discover places worth putting on your map.
    </div>
        """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    destination_columns = st.columns(3)

    for index, destination in enumerate(
        destinations
    ):

        with destination_columns[index % 3]:

            st.image(
                destination["image"],
                use_container_width=True,
            )

            render_html(
                f"""
            <div class="destination-region">
            {destination["region"]}
              </div>

                <div class="destination-name">
                    {destination["name"]}
                </div>

                <div class="destination-description">
                    {destination["description"]}
                </div>
                """
            )

            if st.button(
                f"Explore {destination['name']}",
                use_container_width=True,
                key=f"home_destination_{index}",
            ):

                request = (
                    f"Tell me about travelling to "
                    f"{destination['name']} and create a practical itinerary."
                )

                go_to_planner_with_request(
                    request
                )


    # --------------------------------------------------------
    # WHY PAHAAR TRAILS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-kicker">WHY PAHAAR TRAILS</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Travel planning, simplified.</div>',
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    features = [
        (
            "✨",
            "Personalized Planning",
            "Tell us your destination, duration and travel style. Get a journey shaped around your needs.",
        ),
        (
            "🗺️",
            "Smart Itineraries",
            "Get practical day-by-day plans covering destinations, activities and routes.",
        ),
        (
            "💰",
            "Budget Guidance",
            "Understand estimated accommodation, food, transportation and activity costs.",
        ),
        (
            "🏔️",
            "Pakistan Focused",
            "A travel assistant built specifically around domestic tourism in Pakistan.",
        ),
    ]

    feature_columns = st.columns(4)

    for index, feature in enumerate(
        features
    ):

        with feature_columns[index]:

            render_html(
                f"""
                <div class="feature-box">

                    <div class="feature-icon">
                        {feature[0]}
                    </div>

                    <div class="feature-title">
                        {feature[1]}
                    </div>

                    <div class="feature-text">
                        {feature[2]}
                    </div>

                </div>
                """
            )


    # --------------------------------------------------------
    # STATS
    # --------------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    stat_columns = st.columns(4)

    stats = [
        ("100+", "PLACES TO DISCOVER"),
        ("24/7", "AI TRAVEL ASSISTANCE"),
        ("PK", "PAKISTAN FOCUSED"),
        ("∞", "JOURNEYS TO CREATE"),
    ]

    for index, stat in enumerate(stats):

        with stat_columns[index]:

            render_html(
                f"""
                <div class="stat-box">

                    <div class="stat-number">
                        {stat[0]}
                    </div>

                    <div class="stat-label">
                        {stat[1]}
                    </div>

                </div>
                """
            )


# ============================================================
# DESTINATIONS PAGE
# ============================================================

elif st.session_state.page == "destinations":

    st.markdown(
        '<div class="section-kicker">EXPLORE PAKISTAN</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Where will you go?</div>',
        unsafe_allow_html=True,
    )

    render_html(
        """
        <div class="section-text">
            Explore beautiful destinations across Pakistan
            and let Pahaar Trails help plan your journey.
        </div>
        """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    destination_columns = st.columns(3)

    for index, destination in enumerate(
        destinations
    ):

        with destination_columns[index % 3]:

            st.image(
                destination["image"],
                use_container_width=True,
            )

            render_html(
                f"""
                <div class="destination-region">
                    {destination["region"]}
                </div>

                <div class="destination-name">
                    {destination["name"]}
                </div>

                <div class="destination-description">
                    {destination["description"]}
                </div>
                """
            )

            if st.button(
                f"Plan {destination['name']} Trip",
                use_container_width=True,
                key=f"destination_page_{index}",
            ):

                request = (
                    f"Create a complete practical trip plan "
                    f"for {destination['name']}."
                )

                go_to_planner_with_request(
                    request
                )


# ============================================================
# BUDGET PLANNER
# ============================================================

elif st.session_state.page == "budget":

    st.markdown(
        '<div class="section-kicker">TRAVEL SMART</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Build your travel budget.</div>',
        unsafe_allow_html=True,
    )

    render_html(
        """
        <div class="section-text">
            Give us a few details and Pahaar Trails will
            help create an estimated travel budget.
        </div>
        """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    with st.container(key="budget_box"):

        budget_left, budget_right = st.columns(2)

        with budget_left:

            budget_destination = st.selectbox(
                "Destination",
                [
                    "Hunza",
                    "Skardu",
                    "Swat",
                    "Naran",
                    "Kashmir",
                    "Murree",
                    "Gilgit",
                    "Chitral",
                    "Fairy Meadows",
                    "Other",
                ],
            )

            days = st.number_input(
                "Number of days",
                min_value=1,
                max_value=30,
                value=5,
            )

        with budget_right:

            travelers = st.number_input(
                "Number of travelers",
                min_value=1,
                max_value=20,
                value=2,
            )

            travel_style = st.selectbox(
                "Travel style",
                [
                    "Budget",
                    "Comfort",
                    "Premium",
                    "Adventure",
                ],
            )

        st.markdown("<br>", unsafe_allow_html=True)

        budget_button = st.button(
            "💰  Create My Budget",
            use_container_width=True,
        )

    if budget_button:

        budget_question = f"""
Create an estimated travel budget for a trip in Pakistan.

Destination: {budget_destination}
Duration: {days} days
Number of travelers: {travelers}
Travel style: {travel_style}

Please organize the response into:

1. Transportation
2. Accommodation
3. Food
4. Activities
5. Miscellaneous
6. Estimated total

Use Pakistani Rupees where appropriate.

Clearly state that these are estimates and actual prices
can change depending on season, availability and travel choices.
"""

        go_to_planner_with_request(
            budget_question
        )


# ============================================================
# AI TRIP PLANNER / CHAT
# ============================================================

elif st.session_state.page == "planner":

    st.markdown(
        '<div class="chat-title">✨ Your Pahaar Trails Planner</div>',
        unsafe_allow_html=True,
    )

    render_html(
        """
        <div class="chat-subtitle">
            Ask about destinations, itineraries, budgets,
            routes, activities, accommodation and travel
            within Pakistan.
        </div>
        """
    )

    st.markdown("<br>", unsafe_allow_html=True)


    # --------------------------------------------------------
    # DISPLAY CHAT HISTORY
    # --------------------------------------------------------

    for message in st.session_state.messages:

        if isinstance(message, HumanMessage):

            with st.chat_message(
                "user",
                avatar="🧳",
            ):

                st.markdown(
                    message.content
                )

        elif isinstance(message, AIMessage):

            with st.chat_message(
                "assistant",
                avatar="🏔️",
            ):

                st.markdown(
                    message.content
                )


    # --------------------------------------------------------
    # CHAT INPUT
    # --------------------------------------------------------

    prompt = st.chat_input(
        "Ask Pahaar Trails — e.g. Plan a 5-day Skardu trip..."
    )


    if prompt:

        user_message = HumanMessage(
            content=prompt
        )

        st.session_state.messages.append(
            user_message
        )

        with st.chat_message(
            "user",
            avatar="🧳",
        ):

            st.markdown(prompt)


        with st.chat_message(
            "assistant",
            avatar="🏔️",
        ):

            with st.spinner(
                "Pahaar Trails is planning your journey..."
            ):

                try:

                    response = ask_ai()

                    answer = response.content

                    st.markdown(
                        answer
                    )

                    st.session_state.messages.append(
                        AIMessage(
                            content=answer
                        )
                    )

                except Exception as error:

                    st.error(
                        "We couldn't complete your request."
                    )

                    st.caption(
                        "Please check your OpenAI API key and try again."
                    )


# ============================================================
# FOOTER
# ============================================================

render_html(
    """
    <div class="footer-line">

        <div class="footer-brand">
            PAHAAR TRAILS
        </div>

        <div>
            Explore Pakistan. Create memories. Find your trail.
        </div>

        <div style="margin-top:7px;">
            AI Travel Planning • Domestic Tourism • Pakistan 🇵🇰
        </div>

    </div>
    """
)
