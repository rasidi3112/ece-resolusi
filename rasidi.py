SMTP ( Simple Mail Transfer Protocol ) 

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, password, attachment_path=None):
    # Buat pesan email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Tambahkan isi pesan
    msg.attach(MIMEText(body, "plain"))

    # Tambahkan lampiran jika ada
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(attachment_path)}",
        )
        msg.attach(part)

    # Kirim email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print("Email berhasil dikirim.")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")

# Jalankan fungsi
sender_email = input("Masukkan email pengirim: ")
receiver_email = input("Masukkan email penerima: ")
subject = input("Masukkan subjek email: ")
body = input("Masukkan isi email: ")
smtp_server = "smtp.gmail.com"
smtp_port = 587
password = input("Masukkan password email pengirim: ")
attachment_path = input("Masukkan path file lampiran (kosongkan jika tidak ada): ") or None

send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, password, attachment_path)
