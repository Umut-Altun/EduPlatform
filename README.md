# EduPlatform - Eğitim İçerik Paylaşım Platformu

Bu platform, eğitim içeriklerinin paylaşılabildiği, kullanıcıların etkileşimde bulunabildiği ve öğrenme deneyimini zenginleştiren bir web uygulamasıdır.

## Özellikler

- İçerik Paylaşımı (notlar, projeler, ödevler)
- Kullanıcı Profilleri
- Beğeni ve Yorum Sistemi
- İçerik Kategorileri
- Gelişmiş Filtreleme ve Arama

## Gereksinimler

- Python 3.8+
- Django 4.2+
- Diğer gereksinimler requirements.txt dosyasında listelenmiştir

## Kurulum

1. Repoyu klonlayın:
```bash
git clone https://github.com/[kullanıcı-adınız]/edu_platform.git
cd edu_platform
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv venv
# Windows için:
venv\Scripts\activate
# Linux/Mac için:
source venv/bin/activate
```

3. Gereksinimleri yükleyin:
```bash
pip install -r requirements.txt
```

4. Veritabanı migrasyonlarını yapın:
```bash
python manage.py migrate
```

5. Geliştirme sunucusunu başlatın:
```bash
python manage.py runserver
```

## Katkıda Bulunma

1. Bu repoyu forklayın
2. Yeni bir branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Bir Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.