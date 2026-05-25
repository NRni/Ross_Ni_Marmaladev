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

May 19, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Read my files and make the UI cooler, mostly purple, with more animation, using Python only.

### Why I Asked

Wanted the Marmaladev app to feel more polished and visually engaging while staying within the Python-only course constraint.

### What AI Gave Me

- Read project files and confirmed the UI is Streamlit in `marmaladev/app.py`.
- Implemented a purple visual overhaul directly in Python via injected Streamlit CSS.
- Added animation effects (hero glow, profile card entrance, button hover lift, and tab polish).
- Upgraded profile cards into custom styled HTML blocks with skill pills and improved link styling.
- Preserved existing core flows (sign-in, tabs, create/edit/delete) and added celebratory UX feedback.
- Ran lints and compile checks to confirm `app.py` is valid.

### What I Used

- Updated `marmaladev/app.py` with a purple animated UI theme.
- Python-only approach aligned with class rules.
### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 20

### Date

May 19, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- How to see what changed, and whether there is a localhost to view it.

### Why I Asked

Needed a practical way to inspect code edits and preview the UI update.

### What AI Gave Me

- Clear commands to inspect diffs (`git diff`, targeted file diff) and run the app locally with Streamlit.
- Clarified that the app runs on the user's localhost and where to open it in the browser.

### What I Used

- Local verification workflow: diff first, then run and view UI changes on localhost.
### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 21

### Date

May 19, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Whether the font can be changed, and if a font file upload is needed.

### Why I Asked

Wanted to further improve the look-and-feel of the Marmaladev UI typography.

### What AI Gave Me

- Updated `marmaladev/app.py` to apply a modern font stack globally through the existing Streamlit CSS theme.
- Clarified that no upload is required for built-in/system fonts, while custom font files are only needed for a specific branded typeface.
- Validated the change with compile and lint checks.

### What I Used

- Global UI font update using a clean sans-serif stack in the app theme.
### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 22

### Date

May 19, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Read my files and change the font because I downloaded fonts.

### Why I Asked

Wanted to apply a specific downloaded typeface to the app UI.

### What AI Gave Me

- Searched the workspace and found the downloaded font file at `Honk/Honk-Regular-VariableFont_MORF,SHLN.ttf`.
- Updated `marmaladev/app.py` to load that local font with embedded `@font-face` (base64 data URL) and apply it as the first-choice app font.
- Fixed a CSS string formatting issue during implementation and re-validated the file.
- Confirmed the updated app compiles and has no linter errors.

### What I Used

- Local custom font integrated into the Streamlit theme from the downloaded `.ttf` file.
### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 23

### Date

May 19, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Ensure the font changes apply to every text element in the project, not just a limited part.

### Why I Asked

The previous font update appeared partial, so a full app-wide typography override was needed.

### What AI Gave Me

- Updated `marmaladev/app.py` CSS selectors to enforce the custom font across all common Streamlit text surfaces (markdown, captions, labels, inputs, textareas, tabs, buttons, widgets, and BaseWeb elements).
- Kept the downloaded local font (`Honk`) as first priority in the stack.
- Re-ran compile and lint checks with no errors.

### What I Used

- Full app-wide font enforcement for all visible text in the Streamlit UI.
### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 24

### Date

May 19, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Make only titles and big text use Honk, and make small text use Cutive Mono.

### Why I Asked

Wanted a cleaner typography hierarchy: expressive display font for emphasis and a readable mono font for regular content.

### What AI Gave Me

- Found `Cutive_Mono/CutiveMono-Regular.ttf` in the workspace.
- Updated `marmaladev/app.py` to embed both local fonts (`HonkLocal` and `CutiveMonoLocal`) with `@font-face`.
- Set app-wide/body and small text to `CutiveMonoLocal`.
- Scoped `HonkLocal` specifically to titles and larger display elements (headings, hero title, profile names, tab labels, expander summaries, emphasized alert text).
- Re-ran compile and lint checks with no issues.

### What I Used

- Two-font UI system: Honk for large/display text and Cutive Mono for normal/small text.
### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 25

### Date

May 19, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Change the animation for Browse Profiles, Map, and My Profile tabs because the UI feels weird.

### Why I Asked

The current tab motion and styling felt off and needed smoother, cleaner interactions.

### What AI Gave Me

- Updated tab-specific CSS in `marmaladev/app.py` to reduce awkward movement and improve visual clarity.
- Removed Honk from tab labels to avoid distorted-looking navigation text.
- Restyled tab container and active/hover states with softer transitions and less jumpiness.
- Added subtle `tabpanel` fade-in animation for smoother content switching.
- Re-ran compile and lint checks with no errors.

### What I Used

- Cleaner navigation feel for Browse Profiles / Map / My Profile tabs with refined animations.
### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 26

### Date

May 19, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Create a Cursor rule to always "grill me" for each prompt.

### Why I Asked

Wanted persistent, structured challenge questions on every request.

### What AI Gave Me

- Added `.cursor/rules/always-grill-me.mdc` as an always-apply rule.
- Configured the rule to ask one challenge question per prompt, provide 4 options (A/B/C/D), include a recommendation, and ask one question at a time.
- Included response style guidance and a concrete example in the rule.

### What I Used

- New always-on Cursor rule for "grill me" behavior in this workspace.
### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 27

### Date

May 19, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Use Nabla for titles and Kings for normal text.

### Why I Asked

Wanted a new visual hierarchy with a stylized title font and a separate body font.

### What AI Gave Me

- Found local font files `Nabla/Nabla-Regular-VariableFont_EDPT,EHLT.ttf` and `Kings/Kings-Regular.ttf`.
- Updated `marmaladev/app.py` to embed both fonts via `@font-face`.
- Mapped titles/display text to `NablaLocal` and normal/body UI text to `KingsLocal`.
- Kept existing theme/animations and verified compile + lint checks pass.

### What I Used

- New typography mapping: Nabla for headings and Kings for regular text in the app.
### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 28

### Date

May 19, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Keep Marmaladev title text special, but set other titles to Amatic SC and small text to Ubuntu.

### Why I Asked

Wanted finer typography control across headings vs body text while preserving the brand title style.

### What AI Gave Me

- Found local `Amatic SC` and `Ubuntu` font files in the workspace.
- Updated `marmaladev/app.py` to embed `Amatic SC` (regular + bold) and `Ubuntu` (regular) with `@font-face`.
- Mapped fonts so:
  - `Marmaladev` hero title uses `Nabla`
  - other title elements use `Amatic SC`
  - normal/small text uses `Ubuntu`
- Kept existing styling and confirmed compile + lint checks pass.

### What I Used

- Final typography split: Nabla for Marmaladev title, Amatic SC for other titles, Ubuntu for body/small text.
### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 29

### Date

May 19, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Treat section labels like "2 Developers", "Developer Map", and "Edit: Nicole" as titles, and change title font to Abril Fatface while setting small text to Montserrat.

### Why I Asked

Wanted the heading hierarchy to be visually consistent and easier to read with preferred fonts.

### What AI Gave Me

- Found local font files `Abril_Fatface/AbrilFatface-Regular.ttf` and `Montserrat/Montserrat-VariableFont_wght.ttf`.
- Updated `marmaladev/app.py` font embedding to use `AbrilLocal` for title-style elements and `MontserratLocal` for normal/small text.
- Kept the `Marmaladev` hero title special (still Nabla as previously requested).
- Verified the app compiles and lint checks are clean.

### What I Used

- Updated typography mapping: Abril Fatface for titles and Montserrat for body/small text.
### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 30

### Date

May 23, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Add more animation to the Marmaladev UI.

### Why I Asked

Wanted the app to feel more dynamic and polished beyond the existing purple theme.

### What AI Gave Me

- Expanded animations in `marmaladev/app.py`: drifting background, floating purple orbs, hero float, title reveal, staggered profile cards, card hover lift/glow, skill pill pop, link slide, button press/hover, input focus glow, expander/alert/map fade-in, and reduced-motion fallback.
- Added staggered card entrance via `card_index` in `render_profile_card`.
- Verified compile and lint checks pass.

### What I Used

- Richer motion layer across the Streamlit UI while keeping readability.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 31

### Date

May 23, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Center the Browse Profiles / Map / My Profile UI, make it bigger, and improve tab toggle animation.

### Why I Asked

The tab section felt off-center, too small, and the tab switching animation needed polish.

### What AI Gave Me

- Updated `marmaladev/app.py` CSS to center the main tab area and content with max-width constraints.
- Increased sizes for hero, section titles, profile cards, map, and form widgets inside tabs.
- Reworked tab toggle styling into a sliding purple pill highlight with smoother cubic-bezier transitions and tab panel switch animation.
- Verified compile and lint checks pass.

### What I Used

- Centered, larger tab UI with improved toggle animation for Browse / Map / My Profile.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 32

### Date

May 23, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Help — I can't open the app.

### Why I Asked

The Streamlit UI was not loading in the browser as expected.

### What AI Gave Me

- Checked the running terminal and found Streamlit is serving on `http://localhost:8502` (not the default 8501).
- Verified both ports 8501 and 8502 respond, and `app.py` imports fine in the user's conda environment.
- Provided clear steps to open the correct URL, restart Streamlit cleanly, and troubleshoot if the browser still fails.

### What I Used

- Correct localhost URL and restart commands to open Marmaladev.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 33

### Date

May 23, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Localhost loads but shows only blur with no text.

### Why I Asked

The app appeared broken in the browser despite Streamlit running.

### What AI Gave Me

- Diagnosed likely CSS layering issue: blurred decorative orbs (`::before`/`::after`) were painting over UI content.
- Fixed stacking in `marmaladev/app.py` by pushing content layers above background (`z-index`), lowering orb opacity, and using lighter Montserrat regular font file to reduce load time.
- Provided restart/refresh steps to verify the fix.

### What I Used

- Layering fix so text and controls render above the purple blur background.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 34

### Date

May 23, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Stop centering all text; lay boxes left-to-right; fix Deploy button cut off screen.

### Why I Asked

Previous centering/layout changes made the UI hard to use and clipped the Streamlit Deploy control.

### What AI Gave Me

- Removed global text centering for headings, captions, profile cards, and tab form widgets.
- Switched Browse Profiles cards to a 2-column left-to-right grid using `st.columns`.
- Left-aligned profile card content and widened main layout.
- Removed `overflow-x: hidden` and adjusted header/toolbar CSS so Deploy button stays visible.
- Verified `app.py` compiles cleanly.

### What I Used

- Left-aligned layout with horizontal profile card rows and visible top-right Deploy button.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 35

### Date

May 23, 2026

### AI Tool Used

Cursor (Composer / AI assistant in the editor)

### What I Asked AI

- Deploy button still not on screen — please fit it in the viewport.

### Why I Asked

The Streamlit Deploy control remained clipped or off-screen after prior layout fixes.

### What AI Gave Me

- Reworked header/toolbar CSS in `marmaladev/app.py`: fixed header bar to top of viewport, constrained app width to `100vw`, and aligned toolbar actions to the right with safe padding.
- Added top padding to main content so it does not sit under the fixed header.
- Prevented custom button transforms from affecting header/deploy controls.
- Verified compile check passes.

### What I Used

- Fixed top header layout so Deploy stays visible inside the screen.

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step

---

## Entry 36

### Date

### AI Tool Used

### What I Asked AI

### Why I Asked

### What AI Gave Me

### What I Used

### What I Changed or Rejected

### What I Still Do Not Fully Understand

### My Next Step
