---
name: marmaladev
description: Marmaladev product context and Python conventions for this Obsidian vault or any linked codebase. Use when implementing profiles, location, link uploads, APIs, or persistence for Marmaladev.
---

# Marmaladev

## Product context

Marmaladev helps game developers and designers find teammates in adjacent locations for game jams and community discussion. Authoritative scope lives in the vault note `Final_Project_PRD.md`.

**Hard constraint**

- **Python only** for all project code the student writes: no Node/React/Swift/etc. for core features unless the instructor grants an exception. Prefer **Streamlit**, **Flask**, **FastAPI** (+ Jinja2 if needed), **Tkinter** / **PySimpleGUI**, or **CLI**. External HTTP APIs may be called with **`httpx`** or **`requests`**.

**MVP**

- Personal profiles (info and work links).
- Location support for adjacent matching (map or coarse geo).
- Link upload or portfolio URLs.

**Suggested build order**

1. Profiles as dicts; list of profiles in memory.
2. Functions for validation and simple adjacency (stub or haversine).
3. JSON file persistence, then HTTP API when ready.
4. Introduce classes (OOP) when duplication grows; tighten error handling for I/O and external APIs.

## Stack (Python only)

Default web direction: **FastAPI** + **Pydantic**, or **Flask**; **Django** if the course requires it. For a quick all-Python UI, **Streamlit** is a strong MVP fit (profiles + map widgets). Keep persistence pluggable: JSON files first, then a Python-friendly DB layer if needed (**sqlite3** is fine). Do not introduce a non-Python frontend framework.

## Conventions for agents

- Use type hints on public functions and API handlers.
- Validate at boundaries: HTTP layer and file load or save paths.
- Surface user-facing errors clearly; log or wrap unexpected failures without leaking secrets (API keys).
- Keep profile and location fields aligned with the PRD; do not expand scope to unrelated social features without an explicit ask.

## Privacy and safety

- Treat precise location as sensitive; support coarse regions where possible.
- Validate and sanitize URLs and text fields to reduce injection or broken-link issues.
