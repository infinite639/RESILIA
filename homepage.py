import streamlit as st


st.set_page_config(page_title="RESILIA", layout="narrow", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
        #MainMenu, header, footer {visibility: hidden;}
        [data-testid="stAppViewContainer"] {
            background: #fcfaf6;
            min-height: 100vh;
            overflow: hidden;
        }
        [data-testid="stMainBlockContainer"] {
            max-width: none;
            padding: 0 !important;
        }
        .resilia-home {
            min-height: 100vh;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            box-sizing: border-box;
            padding: 6.5rem 1.5rem 12rem;
            overflow: hidden;
            color: #161c23;
            font-family: Arial, Helvetica, sans-serif;
        }
        .hero-content {position: relative; z-index: 1; text-align: center;}
        .brand {display: flex; align-items: center; justify-content: center; gap: 2rem;}
        .brand svg {width: 130px; height: 160px;}
        .wordmark {
            font-size: clamp(4rem, 8vw, 7.25rem);
            letter-spacing: 0.055em;
            font-weight: 800;
            line-height: 1;
        }
        .accent {width: 84px; height: 5px; background: #d93836; margin: 2.5rem auto 2.7rem;}
        .tagline {
            margin: 0 auto;
            max-width: 760px;
            font-size: clamp(1.55rem, 2.5vw, 2.35rem);
            letter-spacing: .02em;
            line-height: 1.45;
            font-weight: 400;
        }
        .actions {display: flex; gap: 1.35rem; justify-content: center; margin-top: 3.5rem;}
        .action {
            width: 360px;
            min-height: 96px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1.1rem;
            font-size: 1.65rem;
            font-weight: 600;
            text-decoration: none;
            transition: transform .2s ease, box-shadow .2s ease;
            box-sizing: border-box;
        }
        .action:hover {transform: translateY(-3px); box-shadow: 0 10px 25px rgba(145, 31, 28, .18);}
        .primary {background: #d93836; color: white; border: 1px solid #d93836;}
        .secondary {color: #d93836; border: 1.5px solid #d93836; background: rgba(255,255,255,.25);}
        .action svg {width: 39px; height: 39px; stroke: currentColor; fill: none; stroke-width: 2.6;}
        .wave {position: absolute; left: -10%; width: 120%; border-radius: 50% 50% 0 0; pointer-events: none;}
        .wave-one {height: 180px; bottom: -95px; background: #fff0ce; transform: rotate(3deg); opacity: .65;}
        .wave-two {height: 180px; bottom: -125px; background: #fbe8bb; transform: rotate(-4deg); opacity: .58;}
        .wave-three {height: 105px; bottom: -74px; background: #fff8e8; transform: rotate(2deg); opacity: .85;}
        @media (max-width: 800px) {
            .resilia-home {padding-top: 4rem; padding-bottom: 9rem;}
            .brand {gap: 1rem;}
            .brand svg {width: 80px; height: 100px;}
            .actions {flex-direction: column; margin-top: 2.5rem;}
            .action {width: min(360px, 86vw); min-height: 76px; font-size: 1.3rem;}
        }
    </style>

    <main class="resilia-home">
        <section class="hero-content">
            <div class="brand">
                <svg viewBox="0 0 130 160" aria-label="RESILIA shield logo">
                    <path d="M65 7 L118 27 V76 C118 111 96 137 65 153 C34 137 12 111 12 76 V27 Z" fill="#fcfaf6" stroke="#161c23" stroke-width="9" />
                    <g transform="translate(65 80)" fill="#d93836">
                        <path d="M-9-34H9l3 10 9 4 9-6 13 13-6 9 4 9 10 3V26l-10 3-4 9 6 9-13 13-9-6-9 4-3 10H-9l-3-10-9-4-9 6-13-13 6-9-4-9-10-3V8l10-3 4-9-6-9 13-13 9 6 9-4z" />
                        <circle r="14" fill="#fcfaf6" />
                    </g>
                </svg>
                <div class="wordmark">RESILIA</div>
            </div>
            <div class="accent"></div>
            <p class="tagline">*An AI powered building maintenance<br class="desktop-break"> and resilience system.</p>
            <nav class="actions" aria-label="Main navigation">
                <a class="action primary" href="#maintenance">
                    <svg viewBox="0 0 48 48" aria-hidden="true"><path d="M9 42h30M14 42V9h19v33M19 15h4M26 15h3M19 22h4M26 22h3M19 29h4M26 29h3M8 42V26h6M34 42V20h6v22"/><path d="M22 42v-7h5v7"/></svg>
                    <span>Maintenance</span>
                </a>
                <a class="action secondary" href="#feedback">
                    <svg viewBox="0 0 48 48" aria-hidden="true"><path d="M8 10h32v24H22l-9 7v-7H8z"/><circle cx="17" cy="22" r="1.6" fill="currentColor"/><circle cx="24" cy="22" r="1.6" fill="currentColor"/><circle cx="31" cy="22" r="1.6" fill="currentColor"/></svg>
                    <span>Feedback</span>
                </a>
            </nav>
        </section>
        <div class="wave wave-one"></div>
        <div class="wave wave-two"></div>
        <div class="wave wave-three"></div>
    </main>
    """,
    unsafe_allow_html=True,
)
