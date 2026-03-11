"""
Sandy's Dashboard - Database Operations
"""
import json
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

# Database path - works in both local and Streamlit Cloud
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "sandy_dashboard.db"
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "clients.json"


def init_database():
    """Initialize database with sample data."""
    try:
        # Ensure data directory exists
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create clients table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id TEXT PRIMARY KEY,
                name TEXT,
                avatar TEXT,
                compartment TEXT,
                interest_level INTEGER,
                last_contact TEXT,
                next_followup TEXT,
                conversion_probability INTEGER,
                disc_style TEXT,
                disc_drive INTEGER,
                disc_influence INTEGER,
                disc_steadiness INTEGER,
                disc_compliance INTEGER,
                ilwe_income TEXT,
                ilwe_lifestyle TEXT,
                ilwe_wealth TEXT,
                ilwe_equity TEXT,
                green_flags TEXT,
                red_flags TEXT,
                next_steps TEXT,
                notes TEXT,
                best_match TEXT,
                blocker TEXT,
                created_at TEXT,
                updated_at TEXT
            )
        """)

        # Create activity log table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS activity_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                action_type TEXT,
                client_id TEXT,
                details TEXT,
                page TEXT
            )
        """)

        # Create error log table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS error_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                error_type TEXT,
                error_message TEXT,
                page TEXT,
                stack_trace TEXT
            )
        """)

        # Check if data exists
        cursor.execute("SELECT COUNT(*) FROM clients")
        if cursor.fetchone()[0] == 0:
            # Load sample data from JSON
            if DATA_PATH.exists():
                with open(DATA_PATH, encoding="utf-8") as f:
                    data = json.load(f)

                now = datetime.now().isoformat()

                for client in data.get("clients", []):
                    cursor.execute("""
                        INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        client.get("id", ""),
                        client.get("name", ""),
                        client.get("avatar", "👤"),
                        client.get("compartment", "IC"),
                        client.get("interest_level", 3),
                        client.get("last_contact", ""),
                        client.get("next_followup", ""),
                        client.get("conversion_probability", 50),
                        client.get("disc_style", "I"),
                        client.get("disc_drive", 50),
                        client.get("disc_influence", 50),
                        client.get("disc_steadiness", 50),
                        client.get("disc_compliance", 50),
                        client.get("ilwe_income", ""),
                        client.get("ilwe_lifestyle", ""),
                        client.get("ilwe_wealth", ""),
                        client.get("ilwe_equity", ""),
                        json.dumps(client.get("green_flags", [])),
                        json.dumps(client.get("red_flags", [])),
                        json.dumps(client.get("next_steps", [])),
                        client.get("notes", ""),
                        client.get("best_match", ""),
                        client.get("blocker", ""),
                        now,
                        now,
                    ))

        conn.commit()
        conn.close()
        return True

    except Exception as e:
        print(f"Database initialization error: {e}")
        return False


def get_db_connection():
    """Get database connection with retry."""
    try:
        init_database()
        return sqlite3.connect(DB_PATH)
    except Exception as e:
        print(f"Database connection error: {e}")
        return None


def get_all_clients():
    """Get all clients - from SQLite if available, else fallback to JSON."""
    conn = get_db_connection()
    if not conn:
        # Fallback to JSON
        if DATA_PATH.exists():
            with open(DATA_PATH, encoding="utf-8") as f:
                data = json.load(f)
            return data.get("clients", [])
        return []

    try:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients ORDER BY name")
        rows = cursor.fetchall()

        clients = []
        for row in rows:
            client = dict(row)
            try:
                client["green_flags"] = json.loads(client.get("green_flags") or "[]")
                client["red_flags"] = json.loads(client.get("red_flags") or "[]")
                client["next_steps"] = json.loads(client.get("next_steps") or "[]")
            except Exception:
                client["green_flags"] = []
                client["red_flags"] = []
                client["next_steps"] = []
            clients.append(client)

        return clients
    except Exception as e:
        print(f"Error getting clients: {e}")
        if DATA_PATH.exists():
            with open(DATA_PATH, encoding="utf-8") as f:
                data = json.load(f)
            return data.get("clients", [])
        return []
    finally:
        conn.close()


def get_client_by_id(client_id):
    """Get single client by ID."""
    conn = get_db_connection()
    if not conn:
        return None

    try:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
        row = cursor.fetchone()

        if row:
            client = dict(row)
            try:
                client["green_flags"] = json.loads(client.get("green_flags") or "[]")
                client["red_flags"] = json.loads(client.get("red_flags") or "[]")
                client["next_steps"] = json.loads(client.get("next_steps") or "[]")
            except Exception:
                client["green_flags"] = []
                client["red_flags"] = []
                client["next_steps"] = []
            return client
        return None
    except Exception as e:
        print(f"Error getting client: {e}")
        return None
    finally:
        conn.close()


def get_clients_by_compartment(compartment):
    """Filter clients by compartment."""
    if compartment == "All":
        return get_all_clients()

    conn = get_db_connection()
    if not conn:
        clients = get_all_clients()
        return [c for c in clients if c.get("compartment") == compartment]

    try:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients WHERE compartment = ? ORDER BY name", (compartment,))
        rows = cursor.fetchall()

        clients = []
        for row in rows:
            client = dict(row)
            try:
                client["green_flags"] = json.loads(client.get("green_flags") or "[]")
                client["red_flags"] = json.loads(client.get("red_flags") or "[]")
                client["next_steps"] = json.loads(client.get("next_steps") or "[]")
            except Exception:
                client["green_flags"] = []
                client["red_flags"] = []
                client["next_steps"] = []
            clients.append(client)

        return clients
    except Exception as e:
        print(f"Error getting clients by compartment: {e}")
        clients = get_all_clients()
        return [c for c in clients if c.get("compartment") == compartment]
    finally:
        conn.close()


def get_pipeline_counts():
    """Get client counts by compartment."""
    clients = get_all_clients()
    stages = ["IC", "C1", "C1.1", "C2", "C3", "C4", "C5", "CLOSED"]
    return {s: sum(1 for c in clients if c.get("compartment") == s) for s in stages}


def get_dashboard_stats():
    """Get dashboard KPIs."""
    clients = get_all_clients()
    active = sum(1 for c in clients if c.get("compartment") not in ["CLOSED", None])
    closed = sum(1 for c in clients if c.get("compartment") == "CLOSED")
    c4_count = sum(1 for c in clients if c.get("compartment") == "C4")
    pipeline_value = sum(c.get("interest_level", 0) * 50000 for c in clients if c.get("compartment") != "CLOSED")

    return {
        "active_clients": active,
        "inactive_clients": 0,
        "closed_ytd": closed,
        "c4_clients": c4_count,
        "pipeline_value": pipeline_value,
    }


def get_todays_schedule():
    """Get today's scheduled calls (mock data)."""
    return [
        {"time": "10:00 AM", "client": "Jim Smith", "compartment": "C3", "type": "Presentation"},
        {"time": "2:00 PM", "client": "Sarah Johnson", "compartment": "C1", "type": "Discovery"},
    ]


def get_hot_prospects(limit=3):
    """Get top prospects by interest level."""
    clients = get_all_clients()
    active = [c for c in clients if c.get("compartment") != "CLOSED"]
    sorted_clients = sorted(active, key=lambda c: (c.get("interest_level", 0), c.get("conversion_probability", 0)), reverse=True)
    return sorted_clients[:limit]


def get_overdue_followups(days=7):
    """Get clients not contacted in N days."""
    clients = get_all_clients()
    cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    return [c for c in clients if (c.get("last_contact") or "") < cutoff and c.get("compartment") != "CLOSED"]
