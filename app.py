from flask import Flask, render_template
import pymysql
import boto3

app = Flask(__name__)

# Configuración de la base de datos MySQL
db = pymysql.connect(
    host='database-music.ctqya64kc88a.us-east-2.rds.amazonaws.com',
    user='admin',
    password='fernando123',
    database='music'
)

# Configuración de S3
s3 = boto3.client('s3')

# Nombre de tu bucket de S3
bucket_name = 'your-bucket'

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT nombre, artista, album, ruta FROM canciones")
    canciones = cursor.fetchall()
    cursor.close()
    return render_template('index.html', canciones=canciones)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
