# 1. Temel imaj olarak hafif bir Python imajı seçiyoruz
FROM python:3.9-slim

# 2. Konteyner içinde çalışacağımız klasörü belirliyoruz
WORKDIR /app

# 3. Bağımlılık listesini konteyner içine kopyalıyoruz
COPY requirements.txt .

# 4. Gerekli kütüphaneleri yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# 5. Tüm kodlarımızı konteyner içine kopyalıyoruz
COPY . .

# 6. Uygulamanın çalışacağı portu belirtiyoruz
EXPOSE 5000

# 7. Uygulamayı başlatan komut
CMD ["python", "app.py"]