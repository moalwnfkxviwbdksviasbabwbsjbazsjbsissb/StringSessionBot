import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "26286754").strip()
API_HASH = os.getenv("API_HASH", "7a637e05958e14496e6ab1910a9eb9e7").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6484547301:AAEBttmjmTL42Sdz_omIJSuwx2FT2VAoWac").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://levi303:levi303@cluster0.ws4aofd.mongodb.net/?retryWrites=true&w=majority").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "-1001825940899")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
