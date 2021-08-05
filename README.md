# teamProcject_modaco_AFP
팀 프로젝트_모두 다같이 코딩(모다코)_음식사진분석(Analysis of food photographs)

## 프로젝트 계획
> 현재 쉽게 찾을 수 있는 Image Detection 프로그램들은 대부분 양식을 찾는데 집중하고 있습니다. 한식만을 위한 Image Detection 프로그램을 개발하고자 프로젝트를 시작하게 되었습니다. 음식 사진을 찍으면 해당 음식의 칼로리와 영양소를 분석해서 제공하는데 목적을 두었습니다.

#### 구현할 목록
- Machine learning이 완료된 모델을 API처럼 활용하기
  - 서버의 과부하를 막기 위해 분리된 형태(Rest API)로 활용
- QnA게시판(로그인 했을경우에만 쓰기, 읽기, 삭제, 추천 가능)
- 회원가입, 로그인, 로그아웃

## 프로젝트 환경설정
- python, Pycharm 설치
  - Pycharm에서 setting > project:프로젝트명 > 설정 > location에 프로젝트주소/venv(가상환경) > ok하고 터미널에서 가상환경venv실행된 곳에서 pip를 통해 라이브러리 다운로드
  - 다만, Pycharm에서 제공하는 venv(가상환경)을 사용한 것이 아니라 anaconda를 사용했기에 anaconda에 설치되어있던 라이브러리를 그대로 사용하였음 (모델분석에서 사용된 라이브러리를 포함한 상태여서 anaconda를 사용하기로 결정)
- pip install django : python 프레임워크, MTV(Model-Template-View)패턴을 통해 약속된 형식으로 협업에 보다 용이하고, 신속하게 개발하는 것에 유리
- pip install requests : HTTP 프로토콜을 이용하여 웹에서 리소스를 가져오거나, HTTP패킷을 직접 만들어서 전송할 수 있다.
- pip install Pillow : 파이썬 이미지 처리하기 위한 라이브러리
- pip install pymysql : AWS RDS(MySQL)을 사용할때 mysql이 정상적으로 작동하지 않는 이슈가 발생하여 python에서 mysql을 사용하기 위한 라이브러리
- pip install selenium : web crawling을 위한 라이브러리
- pip install urllib3 : URL 작업을 위한 여러 모듈을 모은 패키지
- pip install opencv-python : 원본사진에 분석을 완료한 결과값을 표시하는 이미지 처리 라이브러리 (cv2)

## 구현기능 설명
1. HOME
- 프로젝트를 시작한 계기, 모델링 진행 및 애로사항 등을 소개
- 사진분석 링크 클릭시 FoodService(url 'photo:photo_form')실행
- 전체적인 화면구성을 bootstrap을 이용하여 반응형 웹과 내비바 등 기능 구현
- photo앱에서 구현
<img width="1440" alt="index" src="https://user-images.githubusercontent.com/86213046/128174324-6c257f2a-9d68-40d0-bec2-fe69271145fa.png">
<img width="616" alt="indexSmall" src="https://user-images.githubusercontent.com/86213046/128174383-bebc3023-0807-46c3-b026-7c428305074e.png">

2. Food Service
- FoodService는 로그인을 하여야 이용 가능(login_required)
- 파일 선택을 클릭하여 이미지 업로드
  * 이미지가 있을 경우에만 상단에 이미지가 나타나는 기능 구현.
- POST방식을 이용하여 서버API에 전달(Rest API)
  * 이때 이미지 파일은 base64를 통해 텍스트 형식으로 바뀌고, Json형식으로 서버에 전달
  * 분석을 완료하면 서버API에서는 dict형식으로 장고Client로 전달(분석과 웹개발에서 똑같은 python언어를 사용해서 dict형식으로 결정)
- photo앱에서 구현
<img width="1440" alt="FoodService" src="https://user-images.githubusercontent.com/86213046/128175229-a7f1b26d-fb3f-4434-b060-ed21f1389c7e.png">

- 원본 이미지와 서버API 결과값을 활용해 이미지 처리(cv2)
- 분석완료 여부, 분석 개수, 음식명을 표시
- 이미지 처리가 완료된 이미지는 로그인 한 계정을 기준으로 DB(models.ImageField)에 저장
- 더 많은 결과값 보기 클릭시 Food List(url 'photo:photo_list')실행
- photo앱에서 구현
<img width="1440" alt="FoodServiceAnalysis" src="https://user-images.githubusercontent.com/86213046/128304121-fb6b03de-1139-444d-83c6-7498b08d4469.png">

3. Food List
- 계정명, 등록일시, 이미지, 분석결과 표시(DB에서 가져옴)
- 등록일시 기준으로 내림차순 정렬
- photo앱에서 구현
<img width="1440" alt="FoodList" src="https://user-images.githubusercontent.com/86213046/128308348-79ffe8d6-85ec-4e4b-b574-f6291f639a41.png">

4. 고객센터
- 등록된 질문목록
  * 처음은 등록일시 기준 내림차순(objects.order_by('-craete_date'))
- 검색(최신순, 인기순, 추천순)
- 페이징(Paginator)
- 질문등록(login_required)
- 댓글수, 추천수 표시
- question앱에서 구현
<img width="1440" alt="QuestionList" src="https://user-images.githubusercontent.com/86213046/128308677-bd884188-922b-4583-bea3-4c54d3032199.png">

- 답변, 댓글, 추천 기능(login_required)
- 답변 내용 미입력시 경고문 출력
- question앱에서 구현
<img width="1440" alt="QuestionDetail" src="https://user-images.githubusercontent.com/86213046/128314341-91349f2b-a73d-47fa-93ff-2f06f1e10771.png">
<img width="1440" alt="QuestionDetailComment" src="https://user-images.githubusercontent.com/86213046/128314734-461a8f57-3339-40ac-b199-783238a25d30.png">

5. 회원
- 비로그인 상태로 로그인 서비스(login_required)이용시 로그인 화면으로 이동
<img width="1440" alt="Login" src="https://user-images.githubusercontent.com/86213046/128315020-186f3564-fe34-48b7-8b41-1a232af7feed.png">
- 계정등록 기능 (django.contrib.auth)
<img width="1440" alt="SignUp" src="https://user-images.githubusercontent.com/86213046/128315067-a05c3541-89c9-4e2a-b54a-497e843e76c6.png">
- common앱에서 구현
