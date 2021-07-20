from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import base64
import requests, json

from ..models import Photo
from ..forms import PhotoForm

def index(request):

    return render(request, 'photo/photo_form.html')

# def detail(requset, photo_id):
#     photo = get_object_or_404(Photo, pk=photo_id)
#     context = {'photo': photo}
#     return render(requset, 'photo/photo_detail.html', context)

@login_required(login_url='common:login')
def photo_create(request):
    if request.method == "POST":
        filepath = request.FILES['file']
        image = request.FILES['file'] #파일 이름 ex)한상.jpg
        encoding_img = base64.b64encode(image.read())
        encoding_img = encoding_img.decode('utf8')
        datas = {'image': encoding_img}
        base_url = "http://3af2ecc4eaa8.ngrok.io"
        url = base_url + '/convert'
        datas = json.dumps(datas)
        res = "test"
        # res = web_request(method_name='POST', url=url, dict_data=datas) #결과값
        # del res['status_code']
        # del res['encoding']
        # del res['Content-Type']
        # del res['ok']
        detection_len = len(res) #데이터 개수
    else:
        pass
    context = {'image':image , 'res': res, 'detection_len':detection_len, 'filepath':filepath}
    return render(request, 'photo/photo_result.html', context)

def web_request(method_name, url, dict_data, is_urlencoded=True):
    """Web GET or POST request를 호출 후 그 결과를 dict형으로 반환 """
    method_name = method_name.upper()  # 메소드이름을 대문자로 바꾼다
    if method_name not in ('GET', 'POST'):
        raise Exception('method_name is GET or POST plz...')

    if method_name == 'GET':  # GET방식인 경우
        response = requests.get(url=url, params=dict_data)
    elif method_name == 'POST':  # POST방식인 경우
        ## 영빈씨 이녀석이 젤중요 이게 24시간 걸리게 한놈입니다. 뒤에 헤더가 없음 못받아욧...
        response = requests.post(url=url, data=json.dumps(dict_data), headers={'Content-Type': 'application/json'})

    dict_meta = {'status_code': response.status_code, 'ok': response.ok, 'encoding': response.encoding,
                 'Content-Type': response.headers['Content-Type']}
    if 'json' in str(response.headers['Content-Type']):  # JSON 형태인 경우
        return {**dict_meta, **response.json()}
    else:  # 문자열 형태인 경우
        return {**dict_meta, **{'text': response.text}}