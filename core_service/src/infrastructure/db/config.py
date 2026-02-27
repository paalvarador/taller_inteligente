from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# 1. Buscamos el archivo .env de forma absoluta
# __file__ es la ubicación de este config.py
# Subimos niveles hasta llegar a 'taller_inteligente'
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
dotenv_path = os.path.join(base_dir, ".env")

# Cargamos el archivo indicando la ruta exacta
load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")

# --- DEBUG: Esto te dirá en consola qué está pasando ---
if not DATABASE_URL:
    print(f"DEBUG: Buscando .env en: {dotenv_path}")
    print(f"DEBUG: ¿El archivo existe?: {os.path.exists(dotenv_path)}")
    raise ValueError("Error: No se encontró la variable DATABASE_URL. Verifica tu archivo .env")

# Ajuste para compatibilidad con SQLAlchemy 1.4+ y 2.0+
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1) # type: ignore

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()