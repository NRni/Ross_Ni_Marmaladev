from __future__ import annotations
from typing import Optional

import streamlit as st
from db import get_connection, init_db
from models import Profile, ROLES, EXPERIENCE_LEVELS


def save_profile(profile: Profile) -> int:
    conn = get_connection()
    if profile.id is None:
        cur = conn.execute(
            "INSERT INTO profiles (name, bio, skills, role, experience) VALUES (?, ?, ?, ?, ?)",
            (profile.name, profile.bio, profile.skills, profile.role, profile.experience),
        )
        profile_id = cur.lastrowid
    else:
        conn.execute(
            "UPDATE profiles SET name=?, bio=?, skills=?, role=?, experience=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
            (profile.name, profile.bio, profile.skills, profile.role, profile.experience, profile.id),
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


def load_profiles() -> list[dict]:
    conn = get_connection()
    rows = conn.execute("SELECT * FROM profiles ORDER BY updated_at DESC").fetchall()
    profiles = []
    for row in rows:
        links = conn.execute("SELECT url FROM links WHERE profile_id=?", (row["id"],)).fetchall()
        profiles.append({**dict(row), "urls": [l["url"] for l in links]})
    conn.close()
    return profiles


def load_profile(profile_id: int) -> Optional[dict]:
    conn = get_connection()
    row = conn.execute("SELECT * FROM profiles WHERE id=?", (profile_id,)).fetchone()
    if row is None:
        conn.close()
        return None
    links = conn.execute("SELECT url FROM links WHERE profile_id=?", (profile_id,)).fetchall()
    conn.close()
    return {**dict(row), "urls": [l["url"] for l in links]}


def delete_profile(profile_id: int) -> None:
    conn = get_connection()
    conn.execute("DELETE FROM profiles WHERE id=?", (profile_id,))
    conn.commit()
    conn.close()


def profile_form(profile: Optional[dict] = None) -> Optional[Profile]:
    defaults = profile or {}
    name = st.text_input("Display Name", value=defaults.get("name", ""))
    bio = st.text_area("Bio", value=defaults.get("bio", ""), max_chars=500)
    skills = st.text_input("Skills (comma-separated)", value=defaults.get("skills", ""), placeholder="Unity, pixel art, C#")

    col1, col2 = st.columns(2)
    with col1:
        role = st.selectbox("Role", ROLES, index=ROLES.index(defaults.get("role", "dev")))
    with col2:
        experience = st.selectbox("Experience", EXPERIENCE_LEVELS, index=EXPERIENCE_LEVELS.index(defaults.get("experience", "junior")))

    existing_urls = defaults.get("urls", [""])
    urls_text = st.text_area(
        "Links (one per line)",
        value="\n".join(existing_urls),
        placeholder="https://github.com/you\nhttps://your-portfolio.com",
    )
    links = [u.strip() for u in urls_text.splitlines() if u.strip()]

    if st.button("Save Profile", type="primary"):
        p = Profile(
            id=defaults.get("id"),
            name=name,
            bio=bio,
            skills=skills,
            role=role,
            experience=experience,
            links=links,
        )
        errors = p.validate()
        if errors:
            for e in errors:
                st.error(e)
            return None
        return p
    return None


def render_profile_card(profile: dict) -> None:
    with st.container(border=True):
        st.subheader(profile["name"])
        st.caption(f"{profile['role'].title()} · {profile['experience'].title()}")
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

    st.title("🎮 Marmaladev")
    st.caption("Find game developers near you")

    tab_list, tab_create, tab_edit = st.tabs(["Browse Profiles", "Create Profile", "Edit / Delete"])

    with tab_create:
        st.header("Create Your Profile")
        profile = profile_form()
        if profile:
            save_profile(profile)
            st.success(f"Profile saved for {profile.name}!")
            st.rerun()

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
            selected = st.selectbox("Select profile to edit", list(options.keys()))
            pid = options[selected]
            profile = load_profile(pid)
            if profile:
                st.header(f"Edit: {profile['name']}")
                updated = profile_form(profile)
                if updated:
                    save_profile(updated)
                    st.success("Profile updated!")
                    st.rerun()
                st.divider()
                if st.button("Delete Profile", type="secondary"):
                    delete_profile(pid)
                    st.warning("Profile deleted.")
                    st.rerun()


if __name__ == "__main__":
    main()
