import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "marmaladev.db"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db() -> None:
    conn = get_connection()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS profiles (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            bio         TEXT NOT NULL DEFAULT '',
            skills      TEXT NOT NULL DEFAULT '',
            jobs        TEXT NOT NULL DEFAULT '',
            years       INTEGER NOT NULL DEFAULT 0,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS links (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            profile_id  INTEGER NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
            url         TEXT NOT NULL,
            label       TEXT NOT NULL DEFAULT '',
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()


def migrate_db() -> None:
    """Add jobs/years columns if upgrading from old schema."""
    conn = get_connection()
    cols = {row[1] for row in conn.execute("PRAGMA table_info(profiles)").fetchall()}
    if "role" in cols and "jobs" not in cols:
        conn.execute("ALTER TABLE profiles ADD COLUMN jobs TEXT NOT NULL DEFAULT ''")
        conn.execute("ALTER TABLE profiles ADD COLUMN years INTEGER NOT NULL DEFAULT 0")
        conn.execute("UPDATE profiles SET jobs = role")
        conn.commit()
    conn.close()
