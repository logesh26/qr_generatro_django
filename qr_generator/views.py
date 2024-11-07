from django.shortcuts import render
import qrcode
from io import BytesIO
import base64
from django.http import JsonResponse

def generate_qr(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Handle AJAX request
        data = request.POST.get('data')
        qr_img = qrcode.make(data)
        buffer = BytesIO()
        qr_img.save(buffer, 'PNG')
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return JsonResponse({'img_base64': img_base64})  # Send back the base64 image
        
    return render(request, 'qr_generator/generate_qr.html')
