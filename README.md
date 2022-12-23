<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=waving&color=0:99CCFF,100:a82da&height=200&section=header&text=Welcome_to_JeJu-Do!&fontSize=60&animation=twinkling" />
</div>	
<div align=center>
	<a href="mailto:yunwltn98@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=flat&logo=Gmail&logoColor=white&link="mailto:yunwltn98@gmail.com" />
	<a href="https://coding-jisu.tistory.com/"><img src="https://img.shields.io/badge/Tistory-000000?style=flat&logo=Tistory&logoColor=white&link="https://coding-jisu.tistory.com" />
	<br>
	<br>
</div>	

<div align=center> 
	<h3> 📌프로젝트 명📌 <h3>
	<h4> Welcome to JeJu-Do! <h4>
	<h6> 제주도 관광지에 관한 정보를 보여주는 앱입니다 <h6>
	<h6> 관광지 조회수, 음식점 카드 매출수 정보를 통계해 차트와 데이터프레임으로 순위를 보여줍니다 <h6>
	<br>
	<h4>
		
👉웹대시보드 주소 <http://ec2-3-38-117-95.ap-northeast-2.compute.amazonaws.com:8503/>

</div>	
<div align=center> 
	<br>
	<br>
	<h3> 프로젝트 메뉴 구성📋 <h3>
	<h4> Home : 앱소개 + 사용한 데이터 정보
	<h4> Tourism : 최근 3개월 조회수 데이터로 제주도 관광지의 순위 통계
  <h4> Restaurant : 최근 3개월 카드사 제주도 식당내 매출 데이터로 제주도 내 음식점 순위 현지인과 외지인 소비 통계
	<br>
	<br>
	<br>
	<br>
	<h3> 사용한 데이터📂 <h3>
	<h4> 제주관광공사 비짓제주 홈페이지 내 관광지 검색 로그데이터(2022년 8월, 9월, 10월) <h4>
	<h4> 신한카드 제주도 내 음식점별 매출 변화량 데이터(2022년 8월, 9월, 10월) <h4>

<https://www.bigdata-culture.kr/bigdata/user/data_market/agency/detail.do?id=ijto_org>
</div>	
<div align=center>
	<br>
	<br>
	<h3> 사용한 컬럼📑 <h3>
	<h4> 관광지 검색 로그데이터의 분류, 관광지명, 주소, 8월, 9월, 10월 조회수 컬럼 <h4>
	<h4> 제주도 내 음식점별 카드매출의 음식점명, 시군구명, 행정동명, 지역명, 음식점 중,소분류, <h4>
	<h4> 8, 9, 10월의 각 현지인/외지인 매출 수, 매출금액 비율 컬럼 <h4>	
	<br>
	<br>
	<h3> 사용한 라이브러리✏️ <h3>	
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white" />
	<img src="https://img.shields.io/badge/NumPy-013243?style=flat&logo=NumPy&logoColor=white" />
	<img src="https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white" />
	<img src="https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=Plotly&logoColor=white" />
	<h3> 사용한 Tools🔨 <h3>
	<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=Jupyter&logoColor=white" />
	<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat&logo=Visual Studio Code&logoColor=white" />
	<img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white" />
	<br>
	<br>
</div>	

		
---


<h3>진행과정💬<h3>

<h4>Jupyter Notebook에서 데이터 분석<h4>
	
<h5> 1. 관광지 검색 로그데이터 파일 분석<h5>
	
- 관광지 검색 로그데이터 파일을 가져와서 사용할 컬럼만 엑세스한 후 컬럼명 변경
- 10월, 9월, 8월 각 데이터프레임을 하나로 만들어 사용
- nan값이 있는지 확인하고 nan값은 0으로 채워준다
- 10월, 9월, 8월 컬럼의 평균값을 만들어 새로운 컬럼을 만들어 저장
- 분류의 유니크 값별 전체조회수 조회가 가능할 수 있도록 엑세스
- 관광지명을 입력하면 주소를 볼 수 있게 데이터 엑세스
- 통합, 월별(8, 9, 10월)로 조회수가 높은 관광지를 볼 수 있게 데이터 엑세스

<h5> 2. 제주도 내 음식점별 카드매출 파일 분석<h5>
	
- 제주도 내 음식점별 카드매출 파일을 가져와서 사용할 컬럼만 엑세스한 후 컬럼명 변경
- 10월, 9월, 8월 각 데이터프레임을 하나로 만들어 사용
- nan값이 있는지 확인하고 nan값은 0으로 채워준다
- 10월, 9월, 8월 컬럼의 평균값을 만들어 새로운 컬럼을 만들어 저장
- 현지인과 외지인별로 소비가 많은 음식점들 순위를 현지인/외지인 매출금액비율 컬럼 절렬로 엑세스
- 3개월동안 사람들이 많이 방문한 음식점 순위를 3개월전체매출수 컬럼 정렬로 엑세스
- 각 월별로 현지인/외지인이 가장 많이 소비한 음식점 데이터 엑세스
- 중분류와 소분류의 유니크한 값으로 조회수가 높은 순위로 조회 가능하게 데이터 엑세스

<h4>Visual Studio Code에서 Streamlit 라이브러리로 작업<h4>

<h5>1. 메인 앱 화면 생성<h5>

- 앱을 대표하는 이미지와 무슨 앱인지 소개하는 글 작성
- 사용한 데이터프레임의 기본 정보를 볼 수 있게 데이터 프레임 입력
- 사이드바 메뉴에 이미지와 관광지명으로 주소 검색하는 기능 설정
		
<h5>2. 파일을 새로 만들어 분석한 제주도 조회수별 관광지 순위 파일 작업<h5>
		
- 무슨 데이터를 사용했는지 설명과 이미지, 데이터프레임 삽입
- 3개월간 조회수가 가장 높은 관광지 10개를 데이터프레임과 plotly bar 차트로 표현
- 월별(8, 9, 10월) 조회수가 많은 관광지 10개를 월별 각각 데이터프레임과 plotly bar 차트로 표현
- 관광지 분류별로 조회할 수 있게 분류선택기능 추가
- 선택한 분류별로 해당 데이터프레임을 보여주고 해당 분류의 조회수 1위를 표시
- 분류별로 나온 데이터프레임 상위 10개를 plotly bar 차트로 볼 수 있게 체크박스 설정

<h5>3. 파일을 새로 만들어 분석한 제주도 카드사 매출별 음식점 정보 파일 작업<h5>
		
- 무슨 데이터를 사용했는지 설명과 이미지, 데이터프레임 삽입
- 3개월간 매출이 가장 많은 음식점 20개를 데이터프레임과 plotly bar 차트로 표현
- 현지인소비/외지인소비가 높은 음식점을 상위 10개를 각각 데이터프레임과 plotly bar 차트로 표현
- 음식점의 중분류별 소비순위를 조회할 수 있게 분류선택기능 추가
- 선택한 분류별로 해당 데이터프레임을 보여주고 해당 분류의 조회수 1위를 표시
- 중분류를 선택한 음식점의 소분류별 소비순위를 조회할 수 있게 분류선택기능 추가
- 선택한 중분류 + 소분류별로 해당 데이터프레임을 보여주고 해당 분류의 조회수 1위를 표시

	
---
	
	
![1](https://user-images.githubusercontent.com/120348555/209072456-1566d8f7-5b55-44e3-94e2-f03f44ba97ea.PNG)
![2](https://user-images.githubusercontent.com/120348555/209072462-66876d71-489c-4035-81ac-5d398cabe02c.PNG)
![3](https://user-images.githubusercontent.com/120348555/209072465-426be302-8fc9-43e6-be28-62f36b867d34.PNG)
![4](https://user-images.githubusercontent.com/120348555/209072468-e3e24bc4-ab54-4818-83b4-02d65b6f264a.PNG)
![5](https://user-images.githubusercontent.com/120348555/209072469-3b0af687-2fb0-4502-bd6e-1d86db49b579.PNG)
![6](https://user-images.githubusercontent.com/120348555/209072472-5b380e3f-7f0c-43c2-b5d8-8e8bf6144bb8.PNG)

<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=cylinder&color=0:99CCFF,100:a82da&height=100&section=header&text=Thank you&fontSize=50&animation=twinkling" />
</div>	
