Related: [[Final_Project_PRD]]

## Entry 1

### Date

April 25, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

1. Whether Cursor could be “linked” to my Obsidian vault and how that works.  
2. To copy `ai_usage_log_template.md` from Downloads into my Obsidian vault.  
3. To plan Python skills for **Marmaladev** using the details in **Final Project PRD.md**, then to implement that plan (fill the PRD, add a Cursor project skill).  
4. To record our dialogue in **AI Usage Log.md**, filling only the sections: Date, AI Tool Used, What I Asked AI, Why I Asked, What AI Gave Me, and What I Used.

### Why I Asked

1. I wanted to use Cursor and Obsidian on the same notes without confusion about sync or setup.  
2. I needed the AI usage template available inside the vault for coursework or reflection.  
3. I needed the PRD’s empty Python and data sections filled and optional agent guidance for building Marmaladev.  
4. I needed a concise log of this AI use for transparency or class requirements, without filling every subsection of the template yet.

### What AI Gave Me

1. **Obsidian + Cursor:** Clarified that both apps edit the same folder on disk; opening the vault in Cursor is enough—no separate “link.” Cautions about not editing the same file in both at once without saving.  
2. **Template:** Created `ai_usage_log_template.md` in the vault root with the same structure as the Downloads file.  
3. **Marmaladev plan/implementation:** Expanded **Final Project PRD.md** (Python skills bullets, data plan, first tiny step, risks) and added `.cursor/skills/marmaladev/SKILL.md` with product context, build order, and conventions.  
4. **This log:** Filled the six requested sections in Entry 1 to summarize the thread.

### What I Used

- The explanation that **KingHalliday** is both the Obsidian vault and a valid Cursor workspace.  
- The **`ai_usage_log_template.md`** file is now in the vault (and this **`AI Usage Log.md`** note).  
- The updated **`Final Project PRD.md`** and **`marmaladev`** Cursor skill for future coding on Marmaladev.  
- This **Entry 1** summary as my record of the conversation.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 2

### Date

April 25, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

To make logging AI use a **habit**: after each dialogue, update **AI Usage Log.md** with the same six sections (Date, AI Tool Used, What I Asked AI, Why I Asked, What AI Gave Me, What I Used). Also noted that **today is April 25** (correct the log date).

### Why I Asked

To keep coursework or transparency records consistent without having to remember to ask every time, and to fix the date on the previous entry.

### What AI Gave Me

- Corrected **Entry 1** date to April 25, 2026.  
- Filled **Entry 2** (this row) for this exchange.  
- Added a **Cursor project rule** (`.cursor/rules/ai-usage-log.mdc`) so the agent is instructed to append a new log entry at the end of substantive chats in this vault, using those six sections and the user’s stated “today” when they give it.

### What I Used

- **Entry 1** date set to April 25, 2026.  
- **Entry 2** as the record of this request.  
- The new **always-apply rule** so future sessions in this workspace should update **AI Usage Log.md** automatically in the agreed format.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 3

### Date

April 25, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

1. Whether I can use **LinkedIn’s API** for Marmaladev (finding or listing game developers).  
2. To **remember to update the AI usage log** after our dialogue.

### Why I Asked

1. To see if LinkedIn could power discovery or profiles instead of only manual data.  
2. To keep following the vault habit and the **`.cursor/rules/ai-usage-log.mdc`** rule without prompting every time.

### What AI Gave Me

1. **LinkedIn API:** Explained that **Sign in with LinkedIn** only gives **the signed-in user’s** basic profile—not a directory or “people near me” search. **Storing a LinkedIn profile URL** as a normal link needs **no API**. Broader search/network APIs are **partner-gated** and tightly restricted; **scraping** violates terms. For MVP, **self-entered profiles + optional LinkedIn link + user-provided location** is the realistic approach.  
2. **This log:** Filled **Entry 3** with those six sections and left a new blank **Entry 4** below.

### What I Used

- The conclusion that Marmaladev should **not** rely on LinkedIn for finding strangers, only optional **login** or a **URL field**.  
- **Entry 3** as the record of this session and a reminder that logging should continue automatically when work is substantive.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 4

### Date

April 25, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

1. Delete **Welcome.md**.  
2. **Link the AI Usage Log to the PRD** at the top of the doc (cross-navigation in the vault).

### Why I Asked

To remove the default welcome note and tie project docs together in Obsidian.

### What AI Gave Me

- Removed **Welcome.md** from the vault.  
- Prepended **`Related: [[AI Usage Log]]`** to **Final Project PRD.md** and **`Related: [[Final Project PRD]]`** to **AI Usage Log.md** so each opens the other from the top of the note.

### What I Used

- Vault without **Welcome.md**.  
- Bidirectional **Related** wikilinks between the PRD and the AI usage log.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 5

### Date

April 25, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

To record that I am **only allowed to use Python** in the Marmaladev project, and to **update the plan** (PRD and agent skill) if anything implied otherwise.

### Why I Asked

Course rule: implementation must stay in Python, so docs and AI guidance should match.

### What AI Gave Me

- **Final Project PRD.md:** New **Implementation constraint (course rule)** section (Python-only, allowed UI paths, no separate Node/React core; HTTP calls from Python OK). Tweaked **Python Skills → APIs** and **Data Plan → Where data comes from** so wording assumes a Python UI.  
- **`.cursor/skills/marmaladev/SKILL.md`:** **Hard constraint** block, **Stack (Python only)** with FastAPI/Flask/Streamlit/sqlite3 guidance and explicit “no non-Python frontend framework.”

### What I Used

- Updated PRD and **marmaladev** skill as the single source of truth for the Python-only rule.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 6

### Date

April 25, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

Where to put **Python files** while the project lives in **Obsidian**, and **how to run** the code.

### Why I Asked

To start coding without cluttering the vault and to know the exact terminal commands.

### What AI Gave Me

- Recommendation: keep code in a subfolder **`marmaladev/`** inside the vault (or a sibling folder outside if the course prefers).  
- Created **`marmaladev/main.py`** (stub) and **`marmaladev/requirements.txt`**.  
- Run instructions: `cd` into `marmaladev`, optional venv, `python3 main.py`; later `streamlit run app.py` or similar.  
- Fixed **Related** wikilinks to **`[[AI_Usage_Log]]`** and **`[[Final_Project_PRD]]`** so they match the actual note filenames; updated **`.cursor/rules/ai-usage-log.mdc`** to reference **`AI_Usage_Log.md`**.

### What I Used

- The **`marmaladev/`** folder as the code home; terminal workflow above.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 7

### Date

April 25, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

To clarify **Implementation constraint (course rule)** in the PRD—explain what each **component or plugin** means (**Jinja2**, etc.) because it felt vague.

### Why I Asked

Needed plain-language definitions before choosing a stack.

### What AI Gave Me

- Expanded **Final_Project_PRD.md**: rewrote the short constraint paragraph and added a **table** describing CLI, Streamlit, Tkinter, PySimpleGUI, Flask, FastAPI (+ **Uvicorn**). Added subsection **Extra names that confuse people** for **Jinja2**, **JSON responses** vs thin-page caveat, and **npm / Node / React**.

### What I Used

- The PRD as my glossary when deciding tools.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 8

### Date

April 25, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

`/create-rule` — **every dialogue** should be documented in the AI usage log (project Cursor rule).

### Why I Asked

To tighten logging policy so no exchanges are skipped as “too small.”

### What AI Gave Me

- Rewrote **[.cursor/rules/ai-usage-log.mdc](.cursor/rules/ai-usage-log.mdc)** (`alwaysApply: true`): removed the “substantive only” filter; **every dialogue turn** must append **AI_Usage_Log.md** with the six sections unless the user opts out; minimal entries OK for short chats.

### What I Used

- The updated **`ai-usage-log`** rule as the vault-wide habit.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 9

### Date

May 6, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

Whether I should **open a new folder** (outside the vault) to put **all the code**.

### Why I Asked

Not stated.

### What AI Gave Me

- **Either works.** Keeping code in **`KingHalliday/marmaladev/`** is fine for a class project (notes + code in one Cursor workspace).  
- **Separate folder** (e.g. `Desktop/Marmaladev/` or `Desktop/KingHalliday-code/`) helps if you want a **clean Obsidian graph**, avoid syncing `.venv`/`__pycache__` with notes, or treat the app as its **own Git repo**.  
- Use **File → Add Folder to Workspace** (or open two windows) if Obsidian stays in KingHalliday but code lives next door.

### What I Used

- Criteria above to decide split vs single vault folder.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 10

### Date

May 12, 2026

### AI Tool Used

Claude Code

### What I Asked AI

1. Git grab the `grill-me` skill from `https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me` and add it to the project's skills.
2. Set a rule to always update the AI usage log after every dialogue.

### Why I Asked

1. Wanted to use Matt Pocock's "grill me" skill for stress-testing plans/designs.
2. To keep the AI usage log habit consistent when using Claude Code (not just Cursor).

### What AI Gave Me

1. Downloaded `SKILL.md` from the GitHub repo and created `.cursor/skills/grill-me/SKILL.md` in the vault.
2. Created `CLAUDE.md` at the vault root with the same logging rule as `.cursor/rules/ai-usage-log.mdc`, adapted for Claude Code.

### What I Used

- `.cursor/skills/grill-me/SKILL.md` — the "grill me" skill for interviewing/plan stress-testing.
- `CLAUDE.md` — persistent rule so Claude Code always logs to `AI_Usage_Log.md`.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 11

### Date

May 12, 2026

### AI Tool Used

Claude Code

### What I Asked AI

Update the grill-me skill so each question gives 4 choices (A/B/C/D) with a recommendation, and asks one question at a time.

### Why I Asked

Wanted structured options instead of open-ended grilling — easier to make decisions.

### What AI Gave Me

Updated `.cursor/skills/grill-me/SKILL.md` — each question now presents 4 choices, states a recommendation with reason, and asks one at a time.

### What I Used

- Updated `grill-me` skill with the 4-choice format.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 12

### Date

May 15, 2026

### AI Tool Used

Claude Code

### What I Asked AI

1. Start building Marmaladev — use grill-me to ask questions about the design.
2. Push the project to GitHub at `https://github.com/NRni/Ross_Ni_Marmaladev`.
3. Help with GitHub OAuth authentication.

### Why I Asked

1. Ready to start building, wanted structured decision-making.
2. Version control and sharing the repo.
3. Couldn't authenticate with `gh` CLI — needed a workaround.

### What AI Gave Me

1. **Grill-me questions:** Asked about UI approach (chose Streamlit) and map library (chose streamlit-folium with Google Maps as fallback).
2. **Build plan:** 6-step plan — profile model → Streamlit CRUD → map → links → nearby matching → polish.
3. **GitHub push:** Initialized git, installed `gh` CLI manually (brew had permission issues), authenticated with a personal access token, resolved merge conflicts, and force-pushed to GitHub.
4. **Data storage question:** Recommended SQLite for the next decision.

### What I Used

- Streamlit as the UI framework.
- streamlit-folium for maps (Google Maps API as fallback).
- Repo live at `https://github.com/NRni/Ross_Ni_Marmaladev`.
- `gh` CLI installed at `~/bin/gh`.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

Answer the data storage question (JSON vs SQLite vs in-memory vs cloud DB) to continue building.

---

## Entry 13

### Date

May 15, 2026

### AI Tool Used

Claude Code

### What I Asked AI

1. Continue grill-me questions (data storage, location, profile fields, links, discovery, profile management, code structure, nearby matching).
2. Start building the Marmaladev MVP.

### Why I Asked

1. To make structured design decisions before coding.
2. Ready to implement after completing the grill-me session.

### What AI Gave Me

1. **Grill-me decisions:** SQLite, city+geocoding (deferred), standard profile fields, free-form URLs, list+map discovery, single-user local, split-by-feature structure, skip nearby matching for MVP.
2. **MVP code:**
   - `db.py` — SQLite schema (profiles + links tables), WAL mode.
   - `models.py` — Profile dataclass with validation (name required, role/experience enums, URL check).
   - `app.py` — Streamlit UI with 3 tabs: Browse Profiles, Create Profile, Edit/Delete.
   - `requirements.txt` — streamlit, streamlit-folium, folium.
3. Fixed Python 3.8 compatibility (`int | None` → `Optional[int]`, added `from __future__ import annotations`).
4. Verified Streamlit runs at `http://localhost:8501`.
5. Pushed to GitHub.

### What I Used

- Working MVP with profile CRUD in Streamlit.
- SQLite database (`marmaladev.db` created on first run).
- Code pushed to `https://github.com/NRni/Ross_Ni_Marmaladev`.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

Add map tab with streamlit-folium (step 4 of build plan).

---

## Entry 14

### Date

May 15, 2026

### AI Tool Used

Claude Code

### What I Asked AI

1. Add full job categories (Game Designer, Game Developer, Game Artist) with sub-specialties as checkboxes.
2. Replace experience dropdown with a years-of-experience slider.
3. Fix bug where adding a job category created duplicate profiles before saving.

### Why I Asked

1. Wanted specific, real game industry roles instead of generic "dev/designer/both".
2. Years of experience is more meaningful than "junior/mid/senior".
3. Streamlit was saving profiles on every widget interaction, not just on button click.

### What AI Gave Me

1. Updated `models.py` — full job lists (9 designer, 9 developer, 12 artist roles), multi-select via checkboxes.
2. Updated `app.py` — 3 expandable job sections, slider for years (0–30), save only on button click.
3. Updated `db.py` — `jobs` column (pipe-separated), `years` column, migration from old schema.
4. Deleted old database for fresh start.

### What I Used

- Multi-job profile system with all game industry roles.
- Years slider instead of experience levels.
- Fixed duplicate profile bug.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

Add map tab with streamlit-folium.

---

## Entry 15

### Date

May 15, 2026

### AI Tool Used

Claude Code

### What I Asked AI

After saving a new profile in the Create tab, the saved profile should be visible there (not just cleared), and it should appear in the Edit/Delete tab.

### Why I Asked

Wanted to see confirmation of what was just saved, and have immediate access to edit it.

### What AI Gave Me

Updated `app.py` to use `st.session_state["just_saved_id"]` — after saving, the Create tab shows the saved profile card at the top with a success message, then a blank form below for creating another. Profile also appears in Edit/Delete tab.

### What I Used

- Saved profile visible in Create tab after submission.
- Profile immediately available in Edit/Delete tab.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

Add map tab with streamlit-folium.

---

## Entry 16

### Date

May 15, 2026

### AI Tool Used

Claude Code

### What I Asked AI

1. Clear the Create form after saving — only edit via Edit tab.
2. Add email sign-in, only show Create Profile on first visit, hide it after profile exists.

### Why I Asked

1. Wanted clean separation: Create for first-time, Edit for changes.
2. Each user should be identified by email, and only create a profile once.

### What AI Gave Me

1. Create tab clears after save with "Profile saved!" message.
2. Email sign-in gate — users enter email to access the app.
3. If no profile exists for that email → Browse + Create tabs.
4. If profile exists → Browse + My Profile (edit/delete) tabs. Create tab hidden.
5. Updated `models.py` (email field), `db.py` (email column, unique constraint), `app.py` (sign-in flow, `load_profile_by_email`).

### What I Used

- Email-based sign-in flow.
- Conditional tabs based on profile existence.
- Old database deleted for fresh schema.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

Add map tab with streamlit-folium.

---

## Entry 17

### Date

May 15, 2026

### AI Tool Used

Cursor (Composer)

### What I Asked AI

- Read though the project.

### Why I Asked

Not stated (likely orientation / understanding the repo before further work).

### What AI Gave Me

- Walkthrough of visible layout: Obsidian vault root, `Final_Project_PRD.md`, `marmaladev/` Streamlit + SQLite app, `.cursor` rules/skills, `AI_Usage_Log.md`.
- Summary of Marmaladev: PRD goals (local game-dev matching), Python-only constraint, MVP (profiles, location, links).
- Summary of current code: `app.py` (email gate, browse/create/edit/delete, job taxonomies, links), `models.py` (`Profile` + validation), `db.py` (SQLite schema + email migration), `main.py` stub, `requirements.txt` (Streamlit + Folium stack; map UI not wired in app yet).

### What I Used

- High-level map of the repo and what is implemented vs. still planned (e.g. map tab per prior log).

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 18

### Date

May 15, 2026

### AI Tool Used

Claude Code

### What I Asked AI

Start doing the geocoding.

### Why I Asked

Wanted to add city-to-coordinate conversion so profiles can appear on a map.

### What AI Gave Me

1. `geocode.py` — uses Nominatim (OpenStreetMap, free, no API key) to convert city names to lat/lon.
2. Added `city`, `lat`, `lon` fields to Profile model and database schema.
3. City input in profile form — geocodes automatically on save.
4. **Map tab** using streamlit-folium — shows markers for all profiles with locations, with popup info (name, jobs, city, skills).
5. Updated profile cards to show city with pin emoji.

### What I Used

- Nominatim geocoding (free, no API key).
- streamlit-folium map with markers and popups.
- Three tabs: Browse Profiles, Map, Create/My Profile.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 19

### Date

### AI Tool Used

### What I Asked AI

### Why I Asked

### What AI Gave Me

### What I Used

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step
