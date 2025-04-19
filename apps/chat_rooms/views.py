from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def room_list(request):
    # Örnek oda verileri (gerçek uygulamada veritabanından gelecek)
    rooms = [
        {
            'id': 1,
            'title': 'Python Programlama Temelleri',
            'description': 'Python programlama dilinin temellerini öğrenmek ve pratik yapmak için oluşturulmuş bir çalışma grubu.',
            'category': 'Programlama',
            'owner': {'username': 'Ahmet Yılmaz', 'initials': 'AY'},
            'created_at': '3 gün önce',
            'member_count': 25,
            'message_count': 150,
            'is_active': True
        },
        # ...diğer odalar
    ]
    return render(request, 'chat_rooms/room_list.html', {'rooms': rooms})

@login_required 
def create_room(request):
    if request.method == 'POST':
        # Oda oluşturma işlemleri
        return redirect('chat_rooms:room_list')
    return render(request, 'chat_rooms/create_room.html')

@login_required
def chat_room(request, room_id):
    # Oda bilgilerini getir
    room = {
        'id': room_id,
        'title': 'Python Programlama Temelleri',
        'description': 'Python öğrenme grubu'
    }
    return render(request, 'chat_rooms/chat_room.html', {'room': room})