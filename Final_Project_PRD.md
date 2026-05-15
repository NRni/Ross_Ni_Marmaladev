Related: [[AI_Usage_Log]]

## Project Title

Marmaladev
## One Sentence Pitch

Marmaladev is a program that helps you find game developers and designers in your adjacent location. 

## Target User

The program has more of a niche target user; it is for game devs who want to group up in a game jam and want to exchange community insights. 
## Purpose

This is useful because game jamming is one of the most interesting and self-improving parts of game development; however, it is hard for indie developers to find teammates. It will be great if I make a program that helps the developers connect with the development community around them. It is also a platform that provides an opportunity for people to gather around and discuss community issues and insights. 

## Implementation constraint (course rule)

**Python only:** All **application logic and UI code I write** must be **Python**. I can still open URLs in a browser or use widgets that render inside the browser—that is normal—but I will not build a separate **Node.js** or **React** (or similar) project as the main codebase unless the instructor explicitly allows it. Calling geocoding or map APIs **from Python** (using libraries like `httpx` or `requests`) is fine.

**Pick one primary way users interact with Marmaladev** (you do not need all of these—choose what fits the assignment):

| Approach | What it is |
|----------|------------|
| **CLI** | **Command-line interface:** the user types commands in a terminal (e.g. `python main.py add-profile`). No graphical window; fastest way to prove profiles + JSON work. |
| **Streamlit** | A Python library that turns Python scripts into a **simple web UI** in the browser. You write widgets (`text_input`, `map`, buttons) in Python only—good demo for profiles + maps without HTML skills. |
| **Tkinter** | Built-in Python **desktop windows** (buttons, forms). Looks older but needs no browser; everything is Python. |
| **PySimpleGUI** | Another Python layer that makes **desktop GUIs** easier than raw Tkinter; still all Python. |
| **Flask** | A small **Python web framework**. Your Python code receives HTTP requests and returns web pages or data. You add URLs like `/profiles` and write the logic in `.py` files. |
| **FastAPI** | Like Flask but newer defaults for **JSON APIs** (structured data for apps). Often paired with **Uvicorn**—the program that **runs** your FastAPI app as a web server (example: `uvicorn main:app`). |

### Extra names that confuse people

- **Jinja2:** A **template engine** often used **with Flask**. You write an HTML file with placeholders (for example `{{ user_name }}`), and **Python fills them in** before sending the page to the browser. Your logic stays in Python; Jinja2 only merges data into HTML strings. You do **not** need Jinja2 if you use Streamlit or only return JSON.
- **JSON responses:** Your Python app sends **structured data** (lists/dicts as text) instead of a fully laid-out webpage. A separate tiny HTML file could display it with a little JavaScript—that JavaScript is **not** Python; if your course forbids client-side JS entirely, prefer Streamlit, Tkinter, or Flask + Jinja2 only.
- **npm / Node / React:** **npm** installs JavaScript packages; **Node** runs JavaScript on a server; **React** is a JavaScript UI framework. Those are what we **avoid** for core Marmaladev work unless your instructor says otherwise.

## MVP

The smallest working version will include a place for developers to upload their personal information and work, and a map function that tells the developer's location. 

## Must Have Features

  

1. Personal profile feature

2. Location detector

3. Link upload feature

  

## Nice To Have Features

  

1. Coffee shop, great-to-chat locations

2.

  

## Stretch Feature

  

1. Jam info and news. 

  

## Python Skills I Might Use

  

### Functions

- Split logic into small units: validate a profile, parse coordinates, format API responses.
- Keep the app readable as features grow (profiles, links, location).

### Lists

- Hold many developer profiles in memory or in API result sets.
- Store multiple portfolio or social links per user.

### Dictionaries

- Represent one profile as a record: name, bio, skills, rough location, links.
- Match JSON request and response bodies when building HTTP APIs.

### APIs

- Python web framework routes or handlers: create or update profile, fetch nearby devs, serve link metadata.
- Optional **HTTP requests from Python** to map or geolocation services (still Python-only on my side).

### File I/O

- Early prototype: persist profiles to JSON on disk so data survives restarts.
- Read config or seed data; later may move to a database.

### OOP

- Model distinct concepts: Profile, Location, PortfolioLink, or a small service for find nearby.
- Avoid one giant script as MVP features 1 through 3 grow.

### Error Handling

- User input: invalid URLs, empty required profile fields.
- Network and HTTP failures from geocoding or external map APIs; missing location data.

## Data Plan

**What data does my project need?**

- Profile fields: display name, bio, skills or roles (dev or design), portfolio and social links.
- Location: coarse or precise coordinates (or city or region) to support adjacent matching.
- Optional: timestamps or IDs so updates and lists stay consistent.

**Where will the data come from?**

- Users enter profiles and links through the **Python** UI (forms, CLI prompts, Streamlit widgets, etc.); location can be typed (city or coordinates) or requested in a way that stays inside my allowed Python stack.
- Optional third-party APIs called **from Python** for geocoding or map display if the MVP goes beyond stub logic.

**How will I store or organize the data?**

- Start with in-memory structures plus JSON file persistence for a small prototype.
- Evolve to a database if the project needs multi-user hosting, search, and reliability.

## First Tiny Step

The first thing I need to build is a small script or module that defines one developer profile as a dictionary, validates the required fields, and saves a list of profiles to a JSON file so I can reload them after restarting the program.

## Possible Risk

The hardest part might be balancing accurate nearby matching with privacy (how precise location is), handling API keys and quotas for real maps, and keeping bad or malicious input from breaking uploads or links.