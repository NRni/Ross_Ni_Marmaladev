from __future__ import annotations
from typing import List, Optional
import base64
import html
from pathlib import Path

import streamlit as st
from db import get_connection, init_db, migrate_db
from models import Profile, ALL_JOBS, FLAT_JOBS
from geocode import geocode_city


def save_profile(profile: Profile) -> int:
    conn = get_connection()
    jobs_str = "|".join(profile.jobs)

    if profile.id is None:
        cur = conn.execute(
            "INSERT INTO profiles (email, name, bio, skills, jobs, years, city, lat, lon) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (profile.email, profile.name, profile.bio, profile.skills, jobs_str, profile.years, profile.city, profile.lat, profile.lon),
        )
        profile_id = cur.lastrowid
    else:
        conn.execute(
            "UPDATE profiles SET name=?, bio=?, skills=?, jobs=?, years=?, city=?, lat=?, lon=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
            (profile.name, profile.bio, profile.skills, jobs_str, profile.years, profile.city, profile.lat, profile.lon, profile.id),
        )
        profile_id = profile.id
        conn.execute("DELETE FROM links WHERE profile_id=?", (profile_id,))

    for url in profile.links:
        url = url.strip()
        if url:
            conn.execute("INSERT INTO links (profile_id, url) VALUES (?, ?)", (profile_id, url))

    conn.commit()
    conn.close()
    return profile_id


def load_profiles() -> List[dict]:
    conn = get_connection()
    rows = conn.execute("SELECT * FROM profiles ORDER BY updated_at DESC").fetchall()
    profiles = []
    for row in rows:
        links = conn.execute("SELECT url FROM links WHERE profile_id=?", (row["id"],)).fetchall()
        d = dict(row)
        d["urls"] = [l["url"] for l in links]
        d["jobs"] = [j for j in d["jobs"].split("|") if j]
        profiles.append(d)
    conn.close()
    return profiles


def load_profile(profile_id: int) -> Optional[dict]:
    conn = get_connection()
    row = conn.execute("SELECT * FROM profiles WHERE id=?", (profile_id,)).fetchone()
    if row is None:
        conn.close()
        return None
    links = conn.execute("SELECT url FROM links WHERE profile_id=?", (profile_id,)).fetchall()
    d = dict(row)
    d["urls"] = [l["url"] for l in links]
    d["jobs"] = [j for j in d["jobs"].split("|") if j]
    conn.close()
    return d


def load_profile_by_email(email: str) -> Optional[dict]:
    conn = get_connection()
    row = conn.execute("SELECT * FROM profiles WHERE email=?", (email,)).fetchone()
    if row is None:
        conn.close()
        return None
    links = conn.execute("SELECT url FROM links WHERE profile_id=?", (row["id"],)).fetchall()
    d = dict(row)
    d["urls"] = [l["url"] for l in links]
    d["jobs"] = [j for j in d["jobs"].split("|") if j]
    conn.close()
    return d


def delete_profile(profile_id: int) -> None:
    conn = get_connection()
    conn.execute("DELETE FROM profiles WHERE id=?", (profile_id,))
    conn.commit()
    conn.close()


def apply_purple_theme() -> None:
    """Inject custom purple theme + lightweight animations."""
    font_css = ""
    nabla_path = Path(__file__).resolve().parents[1] / "Nabla" / "Nabla-Regular-VariableFont_EDPT,EHLT.ttf"
    if nabla_path.exists():
        nabla_data = base64.b64encode(nabla_path.read_bytes()).decode("ascii")
        font_css += f"""
          @font-face {{
            font-family: "NablaLocal";
            src: url("data:font/ttf;base64,{nabla_data}") format("truetype");
            font-weight: 100 900;
            font-style: normal;
            font-display: swap;
          }}
        """
    abril_path = Path(__file__).resolve().parents[1] / "Abril_Fatface" / "AbrilFatface-Regular.ttf"
    if abril_path.exists():
        abril_data = base64.b64encode(abril_path.read_bytes()).decode("ascii")
        font_css += f"""
          @font-face {{
            font-family: "AbrilLocal";
            src: url("data:font/ttf;base64,{abril_data}") format("truetype");
            font-weight: 400;
            font-style: normal;
            font-display: swap;
          }}
        """
    montserrat_path = Path(__file__).resolve().parents[1] / "Montserrat" / "Montserrat-VariableFont_wght.ttf"
    if montserrat_path.exists():
        montserrat_data = base64.b64encode(montserrat_path.read_bytes()).decode("ascii")
        font_css += f"""
          @font-face {{
            font-family: "MontserratLocal";
            src: url("data:font/ttf;base64,{montserrat_data}") format("truetype");
            font-weight: 100 900;
            font-style: normal;
            font-display: swap;
          }}
        """

    css = """
        <style>
          __FONT_CSS__

          .stApp {
            background: radial-gradient(circle at 20% 20%, #31124b 0%, #180926 40%, #10071a 100%);
            color: #f5eeff;
            font-family: "MontserratLocal", "Montserrat", "Avenir Next", "SF Pro Text", "Segoe UI", "Helvetica Neue", Arial, sans-serif;
          }

          *, *::before, *::after,
          p, span, label, small, li, a,
          input, textarea, select, option, button,
          [data-testid="stMarkdownContainer"],
          [data-testid="stMarkdownContainer"] *,
          [data-testid="stCaptionContainer"],
          [data-testid="stCaptionContainer"] *,
          [data-testid="stTextInput"] *,
          [data-testid="stTextArea"] *,
          [data-testid="stSelectbox"] *,
          [data-testid="stMultiSelect"] *,
          [data-testid="stSlider"] *,
          [data-testid="stCheckbox"] *,
          [data-testid="stRadio"] *,
          [data-testid="stButton"] *,
          [data-testid="stTabs"] *,
          [data-baseweb] *,
          .st-emotion-cache-ue6h4q,
          .st-emotion-cache-16idsys,
          .st-emotion-cache-1wivap2 {
            font-family: "MontserratLocal", "Montserrat", "Avenir Next", "SF Pro Text", "Segoe UI", "Helvetica Neue", Arial, sans-serif !important;
          }

          h1, h2, h3, h4, h5, h6,
          .profile-name,
          [data-testid="stExpander"] summary,
          [data-testid="stAlertContainer"] strong {
            font-family: "AbrilLocal", "MontserratLocal", "Montserrat", "Avenir Next", "SF Pro Text", "Segoe UI", "Helvetica Neue", Arial, sans-serif !important;
          }

          .hero-title {
            font-family: "NablaLocal", "AbrilLocal", "MontserratLocal", "Montserrat", "Avenir Next", "SF Pro Text", "Segoe UI", "Helvetica Neue", Arial, sans-serif !important;
          }

          [data-testid="stHeader"] {
            background: transparent;
          }

          h1, h2, h3 {
            color: #f7eaff !important;
            letter-spacing: 0.2px;
            font-size-adjust: 0.55;
          }

          .main .block-container {
            padding-top: 1.6rem;
          }

          [data-testid="stMarkdownContainer"] p,
          [data-testid="stCaptionContainer"] {
            color: #d9c9f6;
          }

          @keyframes pulseGlow {
            0% { box-shadow: 0 0 0 rgba(170, 98, 255, 0.30); }
            50% { box-shadow: 0 0 24px rgba(170, 98, 255, 0.45); }
            100% { box-shadow: 0 0 0 rgba(170, 98, 255, 0.30); }
          }

          @keyframes slideFadeUp {
            from {
              opacity: 0;
              transform: translateY(8px);
            }
            to {
              opacity: 1;
              transform: translateY(0);
            }
          }

          .hero-banner {
            border: 1px solid rgba(186, 122, 255, 0.45);
            background: linear-gradient(130deg, rgba(94, 34, 153, 0.55), rgba(49, 18, 75, 0.60));
            border-radius: 18px;
            padding: 1rem 1.2rem;
            margin-bottom: 0.9rem;
            animation: pulseGlow 7s ease-in-out infinite;
          }

          .hero-title {
            font-size: 1.45rem;
            font-weight: 700;
            color: #f8eeff;
            margin: 0;
          }

          .hero-subtitle {
            font-size: 0.96rem;
            color: #d9c9f6;
            margin-top: 0.25rem;
          }

          .profile-card {
            border: 1px solid rgba(186, 122, 255, 0.35);
            background: linear-gradient(160deg, rgba(43, 15, 69, 0.75), rgba(29, 11, 46, 0.76));
            border-radius: 16px;
            padding: 1rem 1.1rem;
            margin-bottom: 0.8rem;
            animation: slideFadeUp 420ms ease-out;
          }

          .profile-name {
            color: #f8eeff;
            font-size: 1.15rem;
            font-weight: 700;
            margin: 0 0 0.25rem 0;
          }

          .meta-line {
            color: #d8c4f9;
            font-size: 0.92rem;
            margin-bottom: 0.15rem;
          }

          .skill-pill {
            display: inline-block;
            border: 1px solid rgba(186, 122, 255, 0.45);
            background: rgba(128, 64, 210, 0.24);
            color: #f0dcff;
            border-radius: 999px;
            padding: 0.2rem 0.5rem;
            margin: 0.2rem 0.26rem 0 0;
            font-size: 0.8rem;
          }

          .link-list {
            margin: 0.45rem 0 0 1rem;
            padding: 0;
          }

          .link-list a {
            color: #dba8ff !important;
            text-decoration: none;
          }

          .link-list a:hover {
            color: #efcaff !important;
            text-decoration: underline;
          }

          .stButton > button {
            border: 1px solid rgba(196, 140, 255, 0.55) !important;
            background: linear-gradient(140deg, #7f3fd6, #5d2c96) !important;
            color: #fff6ff !important;
            transition: transform 0.18s ease, box-shadow 0.2s ease;
          }

          .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 18px rgba(153, 84, 230, 0.35);
          }

          [data-baseweb="tab-list"] {
            gap: 0.35rem;
            background: rgba(55, 22, 86, 0.42);
            border: 1px solid rgba(186, 122, 255, 0.25);
            border-radius: 12px;
            padding: 0.24rem;
          }

          [data-baseweb="tab"] {
            background: transparent;
            border-radius: 9px;
            border: 1px solid transparent;
            color: #d9c9f6 !important;
            transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, transform 0.15s ease;
            font-family: "MontserratLocal", "Montserrat", "Avenir Next", "SF Pro Text", "Segoe UI", "Helvetica Neue", Arial, sans-serif !important;
          }

          [data-baseweb="tab"]:hover {
            background: rgba(139, 79, 210, 0.24);
            border-color: rgba(186, 122, 255, 0.28);
            color: #f1deff !important;
            transform: translateY(-1px);
          }

          [data-baseweb="tab-highlight"] {
            background: transparent !important;
          }

          button[aria-selected="true"][role="tab"] {
            background: rgba(158, 93, 233, 0.34) !important;
            border-color: rgba(208, 161, 255, 0.55) !important;
            color: #fff2ff !important;
            box-shadow: 0 0 0 1px rgba(208, 161, 255, 0.18);
          }

          [role="tabpanel"] {
            animation: tabFadeIn 220ms ease-out;
          }

          @keyframes tabFadeIn {
            from {
              opacity: 0;
              transform: translateY(3px);
            }
            to {
              opacity: 1;
              transform: translateY(0);
            }
          }

          .stTextInput > div > div > input,
          .stTextArea textarea {
            background: rgba(31, 13, 48, 0.75) !important;
            border: 1px solid rgba(186, 122, 255, 0.30) !important;
            color: #f9ecff !important;
          }
        </style>
        """
    st.markdown(
        css.replace("__FONT_CSS__", font_css),
        unsafe_allow_html=True,
    )


def render_hero(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="hero-banner">
          <p class="hero-title">{html.escape(title)}</p>
          <p class="hero-subtitle">{html.escape(subtitle)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def profile_form(defaults: Optional[dict] = None, key_prefix: str = "create") -> None:
    """Render the profile form."""
    d = defaults or {}
    default_jobs = d.get("jobs", [])

    name = st.text_input("Display Name", value=d.get("name", ""), key=f"{key_prefix}_name")
    bio = st.text_area("Bio", value=d.get("bio", ""), max_chars=500, key=f"{key_prefix}_bio")
    skills = st.text_input(
        "Skills (comma-separated)",
        value=d.get("skills", ""),
        placeholder="Unity, pixel art, C#",
        key=f"{key_prefix}_skills",
    )

    st.markdown("**Jobs** (select all that apply)")
    selected_jobs: List[str] = []
    for category, job_list in ALL_JOBS.items():
        with st.expander(f"🎮 {category}" if "Designer" in category else
                         f"💻 {category}" if "Developer" in category else
                         f"🎨 {category}"):
            for job in job_list:
                if st.checkbox(job, value=job in default_jobs, key=f"{key_prefix}_job_{job}"):
                    selected_jobs.append(job)

    years = st.slider("Years of experience", min_value=0, max_value=30, value=d.get("years", 0), key=f"{key_prefix}_years")

    # Location — select from list or type custom
    from geocode import CITY_COORDS
    city_options = sorted([c.title() for c in CITY_COORDS.keys()])
    city_options.insert(0, "")

    default_city = d.get("city", "")
    if default_city and default_city.title() not in city_options:
        city_options.insert(1, default_city)

    col_loc1, col_loc2 = st.columns([2, 1])
    with col_loc1:
        selected_city = st.selectbox(
            "Select your city",
            city_options,
            index=city_options.index(default_city.title()) if default_city.title() in city_options else 0,
            key=f"{key_prefix}_city_select",
        )
    with col_loc2:
        custom_city = st.text_input(
            "Or type address",
            value="" if selected_city else default_city,
            placeholder="e.g. 123 Main St, Tokyo",
            key=f"{key_prefix}_city_custom",
        )

    city = custom_city.strip() if custom_city.strip() else selected_city

    existing_urls = d.get("urls", [""])
    urls_text = st.text_area(
        "Links (one per line)",
        value="\n".join(existing_urls),
        placeholder="https://github.com/you\nhttps://your-portfolio.com",
        key=f"{key_prefix}_urls",
    )

    submitted = st.button("Save Profile", type="primary", key=f"{key_prefix}_save")
    if submitted:
        links = [u.strip() for u in urls_text.splitlines() if u.strip()]

        # Geocode city
        lat, lon = d.get("lat"), d.get("lon")
        if city.strip():
            try:
                coords = geocode_city(city)
                if coords:
                    lat, lon = coords
                else:
                    st.warning(f"Could not find coordinates for '{city}'. Saving without location.")
                    lat, lon = None, None
            except Exception:
                st.warning("Geocoding service unavailable. Saving without location.")
                lat, lon = d.get("lat"), d.get("lon")
        else:
            lat, lon = None, None

        p = Profile(
            email=d.get("email", st.session_state.get("user_email", "")),
            id=d.get("id"),
            name=name,
            bio=bio,
            skills=skills,
            jobs=selected_jobs,
            years=years,
            city=city.strip(),
            lat=lat,
            lon=lon,
            links=links,
        )
        errors = p.validate()
        if errors:
            for e in errors:
                st.error(e)
        else:
            save_profile(p)
            st.session_state["just_saved_id"] = True
            st.rerun()


def render_profile_card(profile: dict) -> None:
    jobs = profile.get("jobs", [])
    jobs_line = " · ".join(html.escape(job) for job in jobs)
    years = profile.get("years")
    city = html.escape(profile.get("city", ""))
    bio = html.escape(profile.get("bio", ""))
    skills = [s.strip() for s in profile.get("skills", "").split(",") if s.strip()]

    skill_html = "".join(f'<span class="skill-pill">{html.escape(skill)}</span>' for skill in skills)
    links_html = "".join(
        f'<li><a href="{html.escape(url)}" target="_blank">{html.escape(url)}</a></li>'
        for url in profile.get("urls", [])
    )

    years_line = ""
    if years:
        years_line = f"{years} year{'s' if years != 1 else ''} of experience"

    st.markdown(
        f"""
        <div class="profile-card">
          <p class="profile-name">{html.escape(profile.get("name", ""))}</p>
          {f'<p class="meta-line">{jobs_line}</p>' if jobs_line else ''}
          {f'<p class="meta-line">{years_line}</p>' if years_line else ''}
          {f'<p class="meta-line">📍 {city}</p>' if city else ''}
          {f'<p>{bio}</p>' if bio else ''}
          <div>{skill_html}</div>
          {f'<ul class="link-list">{links_html}</ul>' if links_html else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_map(profiles: List[dict]) -> None:
    """Render a map with profile markers."""
    import pandas as pd

    located = [p for p in profiles if p.get("lat") is not None and p.get("lon") is not None]

    if not located:
        st.info("No profiles with locations yet.")
        return

    df = pd.DataFrame([
        {"lat": p["lat"], "lon": p["lon"], "name": p["name"]}
        for p in located
    ])

    st.map(df, zoom=2, size=20)

    # Show profile list below the map
    for p in located:
        st.markdown(f"**{p['name']}** — 📍 {p.get('city', '')} · {' · '.join(p.get('jobs', []))}")


def sign_in_screen() -> None:
    """Show sign-in form."""
    render_hero("🎮 Marmaladev", "Find game developers near you")
    st.header("Sign In")
    email = st.text_input("Enter your email to continue", placeholder="you@example.com", key="signin_email")
    if st.button("Continue", type="primary", key="signin_btn"):
        if not email.strip() or "@" not in email:
            st.error("Please enter a valid email.")
        else:
            st.session_state["user_email"] = email.strip().lower()
            st.rerun()


def main():
    st.set_page_config(page_title="Marmaladev", page_icon="🎮", layout="wide")
    apply_purple_theme()
    init_db()
    migrate_db()

    # Sign-in gate
    if "user_email" not in st.session_state:
        sign_in_screen()
        return

    email = st.session_state["user_email"]
    existing = load_profile_by_email(email)
    has_profile = existing is not None

    # Show saved confirmation once
    if "just_saved_id" in st.session_state:
        st.session_state.pop("just_saved_id")
        st.success("Profile saved!")
        st.balloons()

    render_hero("🎮 Marmaladev", "Build your profile and discover nearby game devs")
    st.caption(f"Signed in as {email}")

    # Build tabs
    if has_profile:
        tab_list, tab_map, tab_edit = st.tabs(["Browse Profiles", "Map", "My Profile"])
    else:
        tab_list, tab_map, tab_create = st.tabs(["Browse Profiles", "Map", "Create Profile"])

    profiles = load_profiles()

    with tab_list:
        if not profiles:
            st.info("No profiles yet. Be the first!")
        else:
            st.header(f"{len(profiles)} Developer{'s' if len(profiles) != 1 else ''}")
            for p in profiles:
                render_profile_card(p)

    with tab_map:
        st.header("Developer Map")
        render_map(profiles)

    if has_profile:
        with tab_edit:
            st.header(f"Edit: {existing['name']}")
            profile_form(defaults=existing, key_prefix="edit")
            st.divider()
            if st.button("Delete Profile", key="delete_btn"):
                delete_profile(existing["id"])
                st.warning("Profile deleted.")
                st.toast("Profile removed", icon="🟣")
                st.rerun()
    else:
        with tab_create:
            st.header("Create Your Profile")
            profile_form(defaults={"email": email}, key_prefix="create")


if __name__ == "__main__":
    main()
