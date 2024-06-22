from cryptography.fernet import Fernet

# Anahtar üretimi ve Fernet nesnesi oluşturma
key = Fernet.generate_key()
f = Fernet(key)

# Şifrelenecek dosyayı okuma
with open('secret_message.txt', 'rb') as file:
    file_content = file.read()

# Dosyayı şifreleme
encrypted_content = f.encrypt(file_content)

# Şifrelenmiş mesajı dosyaya yazma
with open('encrypted_message.txt', 'wb') as file:
    file.write(encrypted_content)

# Şifreli dosyayı çözme
decrypted_content = f.decrypt(encrypted_content)

# Çözülen dosyayı başka bir dosyaya yazma
with open('decrypted_message.txt', 'wb') as file:
    file.write(decrypted_content)

print(decrypted_content.decode())
