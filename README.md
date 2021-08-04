# teamProcject_modaco_AFP
팀 프로젝트_모두 다같이 코딩(모다코)_음식사진분석(Analysis of food photographs)

## 프로젝트 계획
> 현재 쉽게 찾을 수 있는 Image Detection 프로그램들은 대부분 양식을 찾는데 집중하고 있습니다. 한식만을 위한 Image Detection 프로그램을 개발하고자 프로젝트를 시작하게 되었습니다. 음식 사진을 찍으면 해당 음식의 칼로리와 영양소를 분석해서 제공하는데 목적을 두었습니다.

#### 구현할 목록
- Machine learning이 완료된 모델을 api처럼 활용하기
- QnA게시판, 공지사항게시판(로그인 했을경우에만 쓰기, 읽기, 삭제, 추천 가능)
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
* 프로젝트를 시작한 계기, 모델링 진행 및 애로사항 등을 소개
* 사진분석 링크 클릭시 FoodService(url 'photo:photo_form')실행
* 전체적인 화면구성을 bootstrap을 이용하여 반응형 웹과 내비바 등 기능 구현
* photo앱에서 구현
<img width="1440" alt="index" src="https://user-images.githubusercontent.com/86213046/128174324-6c257f2a-9d68-40d0-bec2-fe69271145fa.png">
<img width="616" alt="indexSmall" src="https://user-images.githubusercontent.com/86213046/128174383-bebc3023-0807-46c3-b026-7c428305074e.png">

2. Food Service
<img width="1440" alt="FoodService" src="https://user-images.githubusercontent.com/86213046/128175229-a7f1b26d-fb3f-4434-b060-ed21f1389c7e.png">
* 
3. Food List
4. 고객센터
5. 회원
