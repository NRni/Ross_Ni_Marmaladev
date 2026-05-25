# Marmaladev — Presentation Bullet Points

---

## Slide 1: Title

- **Project Name:** Marmaladev
- **Name:** Ross Ni
- **Class:** [Your class name here]

---

## Slide 2: The Problem

- Game jams are one of the best ways for indie developers to learn, network, and build portfolios
- **Finding teammates is hard** — especially for solo devs who don't have an existing network
- There's no dedicated platform for game developers to discover each other by location and skill set
- Existing tools (LinkedIn, Discord) are too general — not built for the game dev community
- **Target audience:** Indie game developers, designers, and artists looking to team up for game jams or collaborate on projects

---

## Slide 3: Your Solution

- **Marmaladev** is a Python web app that helps game developers find and connect with nearby devs
- Users create a profile with their name, bio, skills, job roles, years of experience, and portfolio links
- A built-in map shows where developers are located around the world
- Email-based sign-in — users create a profile once, then browse and edit anytime
- Built entirely in Python using Streamlit — no JavaScript, no separate frontend

---

## Slide 4: Key Features

### Feature 1: Developer Profile System
- Users sign in with email and create a detailed profile
- Select from 30+ real game industry roles across 3 categories (Designer, Developer, Artist)
- Multiple job selection — a gameplay programmer who also does technical art can list both
- Years of experience slider (0–30 years)
- Free-form portfolio links (GitHub, itch.io, personal site)

### Feature 2: Geocoded Location Map
- Users select from 70+ major game dev cities via dropdown, or type a custom street address
- Cities are geocoded to lat/lon coordinates (local lookup for known cities, Nominatim API fallback)
- Interactive map tab shows all developers as markers on a world map
- Profile cards display city with location pin

### Feature 3: Browse & Edit Profiles
- Browse tab shows all developer profiles in a responsive 2-column grid
- Custom purple theme with CSS animations (gradient backgrounds, hover effects, staggered card reveals)
- Edit tab lets users update their own profile — Create tab disappears once a profile exists
- Delete profile option with confirmation

---

## Slide 5: Technical Details

### Data Structures
- **Profile dataclass** — Python dataclass with validation (email, name, bio, skills, jobs, years, city, lat/lon, links)
- **Dictionaries** — profiles loaded as dicts from SQLite, passed between functions
- **Lists** — jobs stored as pipe-separated string, split back to list on load; links stored in separate table

### Libraries & APIs
- **Streamlit** — web UI framework (tabs, forms, maps, session state)
- **SQLite** — built-in Python database (`sqlite3` module, no install needed)
- **geopy / Nominatim** — free geocoding API (OpenStreetMap, no API key)
- **pandas** — DataFrame for map data
- **Custom CSS** — purple theme injected via `st.markdown(unsafe_allow_html=True)`

### Code Organization
- `app.py` — Streamlit UI, profile form, map rendering, sign-in flow
- `models.py` — Profile dataclass with validation, job category constants
- `db.py` — SQLite schema, connection management, migration logic
- `geocode.py` — City-to-coordinate lookup (70+ local cities + Nominatim fallback)

---

## Slide 6: Demo

- **[Live demo here — run `streamlit run app.py`]**
- Show sign-in with email
- Create a profile: select jobs, set years, pick a city
- Show the profile appearing in Browse tab with styled cards
- Switch to Map tab — show the marker on the world map
- Edit the profile — show the Create tab is now gone

---

## Slide 7: Reflection

### Challenges
- **Geocoding reliability:** Nominatim was blocked on the school network — solved by building a local lookup table of 70+ major cities as primary geocoder with Nominatim as fallback
- **Streamlit state management:** Profiles were being saved on every widget interaction before the user clicked Save — fixed by only saving on button click
- **Duplicate element IDs:** Streamlit requires unique keys for widgets when the same form appears in multiple tabs — solved with `key_prefix` parameter

### What I Learned
- How to structure a Python project across multiple modules (models, database, UI, geocoding)
- SQLite schema design and migration for evolving data models
- CSS injection in Streamlit for custom theming beyond default styles
- Working with external APIs and building fallbacks for network issues

### What I'd Add Next
- **Find nearby** — distance-based search to show developers within a radius
- **Coffee shop locations** — suggest meetup spots near matched developers
- **Game jam info** — pull in upcoming jams from external APIs
- **Multi-user auth** — proper login system instead of email-only identification
