from __future__ import annotations
from typing import List, Optional

import streamlit as st
from db import get_connection, init_db, migrate_db
from models import Profile, ALL_JOBS, FLAT_JOBS


def save_profile(profile: Profile) -> int:
    conn = get_connection()
    jobs_str = "|".join(profile.jobs)

    if profile.id is None:
        cur = conn.execute(
            "INSERT INTO profiles (name, bio, skills, jobs, years) VALUES (?, ?, ?, ?, ?)",
            (profile.name, profile.bio, profile.skills, jobs_str, profile.years),
        )
        profile_id = cur.lastrowid
    else:
        conn.execute(
            "UPDATE profiles SET name=?, bio=?, skills=?, jobs=?, years=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
            (profile.name, profile.bio, profile.skills, jobs_str, profile.years, profile.id),
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


def delete_profile(profile_id: int) -> None:
    conn = get_connection()
    conn.execute("DELETE FROM profiles WHERE id=?", (profile_id,))
    conn.commit()
    conn.close()


def profile_form(defaults: Optional[dict] = None, key_prefix: str = "create") -> None:
    """Render the profile form. Returns submitted Profile or None."""
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

    # Jobs — grouped by category
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
        p = Profile(
            id=d.get("id"),
            name=name,
            bio=bio,
            skills=skills,
            jobs=selected_jobs,
            years=years,
            links=links,
        )
        errors = p.validate()
        if errors:
            for e in errors:
                st.error(e)
        else:
            pid = save_profile(p)
            st.session_state["just_saved_id"] = pid
            st.rerun()


def render_profile_card(profile: dict) -> None:
    with st.container(border=True):
        st.subheader(profile["name"])
        if profile["jobs"]:
            st.caption(" · ".join(profile["jobs"]))
        if profile["years"]:
            st.caption(f"{profile['years']} year{'s' if profile['years'] != 1 else ''} of experience")
        if profile["bio"]:
            st.write(profile["bio"])
        if profile["skills"]:
            skills = [s.strip() for s in profile["skills"].split(",") if s.strip()]
            st.write(" ".join(f"`{s}`" for s in skills))
        if profile["urls"]:
            for url in profile["urls"]:
                st.markdown(f"- [{url}]({url})")


def main():
    st.set_page_config(page_title="Marmaladev", page_icon="🎮", layout="wide")
    init_db()
    migrate_db()

    st.title("🎮 Marmaladev")
    st.caption("Find game developers near you")

    tab_list, tab_create, tab_edit = st.tabs(["Browse Profiles", "Create Profile", "Edit / Delete"])

    with tab_create:
        if "just_saved_id" in st.session_state:
            st.session_state.pop("just_saved_id")
            st.success("Profile saved! Go to Edit / Delete tab to make changes.")
        st.header("Create Your Profile")
        profile_form(key_prefix="create")

    with tab_list:
        profiles = load_profiles()
        if not profiles:
            st.info("No profiles yet. Create one to get started!")
        else:
            st.header(f"{len(profiles)} Developer{'s' if len(profiles) != 1 else ''}")
            for p in profiles:
                render_profile_card(p)

    with tab_edit:
        profiles = load_profiles()
        if not profiles:
            st.info("No profiles to edit.")
        else:
            options = {f"{p['name']} (#{p['id']})": p["id"] for p in profiles}
            selected = st.selectbox("Select profile to edit", list(options.keys()), key="edit_select")
            pid = options[selected]
            profile = load_profile(pid)
            if profile:
                st.header(f"Edit: {profile['name']}")
                profile_form(defaults=profile, key_prefix="edit")
                st.divider()
                if st.button("Delete Profile", key="delete_btn"):
                    delete_profile(pid)
                    st.warning("Profile deleted.")
                    st.rerun()


if __name__ == "__main__":
    main()
