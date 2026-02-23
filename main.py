import tweepy
import sqlite3
from datetime import datetime

# --- CONFIGURACIÓN ---
api_key = "TU_API_KEY_AQUI"
api_secret = "TU_API_SECRET_AQUI"
access_token = "TU_ACCESS_TOKEN_AQUI"
access_token_secret = "TU_ACCESS_TOKEN_SECRET_AQUI"

# --- FUNCIONES DE BASE DE DATOS (SQLite) ---
def guardar_tweet_en_sql(tweet_id, texto):
    """Registra la actividad del bot en la base de datos local."""
    conexion = sqlite3.connect('mi_bot_data.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registro_tweets (
            id_db INTEGER PRIMARY KEY AUTOINCREMENT,
            tweet_id_real TEXT,
            contenido TEXT,
            fecha DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('INSERT INTO registro_tweets (tweet_id_real, contenido) VALUES (?, ?)', 
                   (tweet_id, texto))
    conexion.commit()
    conexion.close()

# --- LÓGICA PRINCIPAL DEL BOT ---
def ejecutar_bot():
    try:
        # Autenticación con la API v2
        client = tweepy.Client(
            consumer_key=api_key, consumer_secret=api_secret,
            access_token=access_token, access_token_secret=access_token_secret
        )
        
        # Crear mensaje único para evitar error de duplicado (403)
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje = f"Bot activado y reportando actividad: {ahora} #PythonProject"
        
        # Publicar en Twitter
        response = client.create_tweet(text=mensaje)
        tweet_id = str(response.data['id'])
        
        # Guardar en SQLite
        guardar_tweet_en_sql(tweet_id, mensaje)
        print(f"Éxito: Tweet {tweet_id} publicado y guardado en DB.")
        
    except Exception as e:
        print(f"Error al ejecutar el bot: {e}")

if __name__ == "__main__":
    ejecutar_bot()
