from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

# Konfigurasi koneksi database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'         # ganti sesuai user MySQL Anda
app.config['MYSQL_PASSWORD'] = ''         # ganti sesuai password MySQL Anda
app.config['MYSQL_DB'] = 'bukutamu'       # nama database

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama = request.form['nama']
        pesan = request.form['pesan']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO pesan (nama, pesan) VALUES (%s, %s)", (nama, pesan))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM pesan ORDER BY id ASC")  # ASC = urut dari lama ke baru
    pesan_list = []
    for row in cur.fetchall():
        pesan_list.append({'id': row[0], 'nama': row[1], 'pesan': row[2]})
    cur.close()
    return render_template('index.html', pesan_list=pesan_list, current_year=datetime.now().year)

@app.route('/hapus/<int:id>', methods=['POST'])
def hapus(id):
    cur = mysql.connection.cursor()
    # Hapus pesan berdasarkan id
    cur.execute("DELETE FROM pesan WHERE id = %s", (id,))
    mysql.connection.commit()
    # Reset ulang id agar urut dari 1
    cur.execute("SET @num := 0;")
    cur.execute("UPDATE pesan SET id = (@num := @num + 1) ORDER BY id;")
    cur.execute("ALTER TABLE pesan AUTO_INCREMENT = 1;")
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)