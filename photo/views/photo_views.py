from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import base64
import requests, json
import cv2

import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.utils import timezone

from ..models import Photo
from ..forms import PhotoForm

def index(request):

    return render(request, 'photo/photo_index.html')

# def detail(requset, photo_id):
#     photo = get_object_or_404(Photo, pk=photo_id)
#     context = {'photo': photo}
#     return render(requset, 'photo/photo_detail.html', context)

def photo_list(request):
    photos = Photo.objects.all()
    context = {'photos':photos}
    return render(request, 'photo/photo_list.html', context)

@login_required(login_url='common:login')
def photo_form(request):
    return render(request, 'photo/photo_form.html')

@login_required(login_url='common:login')
def photo_create(request):
    if request.method == "POST":
        # 서버에 보내는 파일
        # image = request.FILES['file']

        # 로컬 저장 파일
        filepath = request.FILES['file']
        path = default_storage.save('content/'+filepath.name, ContentFile(filepath.read()))
        file = os.path.join(settings.MEDIA_ROOT, path)
        print(file)

        # image = cv2.imread(file, cv2.IMREAD_COLOR)
        encoding_img=fileToBase64(file)
        # encoding_img = base64.b64encode(image.read())
        # encoding_img = encoding_img.decode('utf8')
        # print(encoding_img+'$$$$$$$$$$$$$$$$$$$$$$$$$')
        datas = {'image': encoding_img}
        datas = json.dumps(datas)

        # 서버 주소
        base_url = "http://a31ec7fb36e7.ngrok.io"
        url = base_url + '/convert'

        # 서버로 보내기
        # res = "test"
        # res = web_request(method_name='POST', url=url, dict_data=datas) #결과값
        # del res['status_code']
        # del res['encoding']
        # del res['Content-Type']
        # del res['ok']
        # detection_len = len(res) #데이터 개수
        res = {'0': [275, 127, 358, 212, 'umook', 1.0], '1': [264, 46, 320, 110, 'gaeranmalee', 0.574],
                  '2': [179, 44, 246, 107, 'kongnamul', 0.99], '3': [78, 223, 174, 319, 'rice', 1.0],
                  '4': [102, 52, 162, 102, 'kimchigeon', 1.0], '5': [113, 116, 228, 213, 'kimchigeon', 1.0],
                  '6': [356, 38, 446, 136, 'kkatip', 0.839], '7': [193, 211, 299, 329, 'mookoook', 0.48]}
        # print(res['0'][4])
        namelist = []
        for key, value in res.items():
            namelist.append(value[4])

        src = cv2.imread(file, cv2.IMREAD_COLOR)
        draw =drawing(res, src, file)
        if draw == False:
            return redirect('photo:photo_index')
        # form = PhotoForm(request.POST)
        # if form.is_valid():

        photo = Photo()
        photo.author = request.user
        photo.text = namelist
        photo.photo = file.replace('/Users/ybsong/Documents/git/ybsong/teamProcject_modaco_AFP/media/', '')
        photo.created = timezone.now()
        photo.save()

    else:
        form = PhotoForm()
    context = {'res': res,
               # 'detection_len':detection_len,
               'draw': draw,
               'file': file,
               'form':photo
               }
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

def drawing(result,src, file):
    color = (0,255,0)
    tmp = src.copy()
    # print(type(result))
    for key,value in result.items():
        # print(key,value)
        left, top, right, bottom = value[0],value[1],value[2],value[3]
        cv2.rectangle(tmp, (left, top), (right, bottom), color, 2)
        cv2.putText(tmp, "{} [{:.2f}]".format(value[4], float(value[5])),(left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,color, 2)
    return cv2.imwrite(file, tmp)

def fileToBase64(filepath):
    fp = open(filepath, "rb")
    data = fp.read()
    fp.close()
    return base64.b64encode(data).decode('utf8')