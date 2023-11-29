<h1 align="center"> 두뇌 체조 </h1>
<br/>

## 📝 목차

[프로젝트 개요](#item-one)

[기술 스택](#item-three)

[서버 아키텍처](#item-four)

[서비스 구현 화면](#item-five)

[개발 프로세스](#item-pro)

[팀원 소개](#item-two)

[느낀 점](#item-end)

<br/>

## 📖 프로젝트 개요

<a name="item-one"></a>

<div>

### <strong>진행 기간 </strong>: 2023.11.17 ~ 2023.11.22

### <strong>기획배경</strong>

<div align=center>

![슬라이드10.PNG](README_assets/17a66b8a30defc5c9ce8e8dbe432ac712352c777.PNG)

![슬라이드3.PNG](README_assets/1b0b6ffa51911131fe13f4f3a18e5bc5a068f590.PNG)

![슬라이드4.PNG](README_assets/3bea3844bea9882e7b7dc5e814e49c16d074d580.PNG)

![슬라이드5.PNG](README_assets/d29f20877d1236b612e6a96a5461c762373edb22.PNG)

![슬라이드6.PNG](README_assets/015dfe5eb73416dbc6f304bfc4845398bcaf6639.PNG)

![슬라이드7.PNG](README_assets/ac9eae5a3653a1059ce173b8b1e8218d6ed2e040.PNG)

![슬라이드8.PNG](README_assets/5c845e8444419614e611027e2fbe63106d16cb4d.PNG)

![슬라이드9.PNG](README_assets/05fad8f01f102dc2cd6cecce255aae9f2c1771a6.PNG)

</div>

<br/>

### <strong>목표</strong>

- 일상 생활 속에서 노년층이 치매를 예방하도록 서비스를 제공하는 뉴스 플랫폼

- 개인의 관심 키워드로 뉴스 추천

- 뉴스 내용을 기반으로 AI를 통해 문제 생성

- 퀴즈 결과를 CERAD-K 지표와 연결하여 치매 위험도 분석

</div>

<br/>

## 🛠️ 기술 스택

<br/>

<a name="item-three"></a>

## 💻 IDE

![VSCode](https://img.shields.io/badge/VisualStudioCode-007ACC?style=for-the-badge&logo=VisualStudioCode&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

<br/>

## 📱 Frontend

![React](https://img.shields.io/badge/react-61DAFB?style=for-the-badge&logo=react&logoColor=white)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![Tailwind](https://img.shields.io/badge/TailwindCSS-06B6D4?style=for-the-badge&logo=TailwindCSS&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![ANTD](https://img.shields.io/badge/antdesign-0170FE?style=for-the-badge&logo=antdesign&logoColor=white)

![Axios](https://img.shields.io/badge/axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white)

<br/>

## 💾 Backend

![MongoDB](https://img.shields.io/badge/mongoDB-47A248?style=for-the-badge&logo=MongoDB&logoColor=white)
![Mysql](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<br/>

## 🔃 DevOPS

![amazonec2](https://img.shields.io/badge/amazonec2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white)

<br/>

## ⚙️ Architecture

<a name="item-four"></a>

![아키텍처.png](README_assets/9cd8cf173c268b33a24b49d8c99046fd7ec96b85.png)

<br/>

## 🗂️ 프로젝트 파일 구조

<a name="item-five"></a>

<details>
<summary>FrontEnd</summary>

```
📦src
 ┣ 📂assets
 ┃ ┣ 📜art.png
 ┃ ┣ 📜bird.png
 ┃ ┣ 📜ear.png
 ┃ ┣ 📜hand.png
 ┃ ┣ 📜logo.png
 ┃ ┣ 📜main1.png
 ┃ ┣ 📜main2.png
 ┃ ┣ 📜main3.png
 ┃ ┣ 📜main4.png
 ┃ ┗ 📜path.jpg
 ┣ 📂components
 ┃ ┣ 📂quiz
 ┃ ┃ ┣ 📜J1.tsx
 ┃ ┃ ┣ 📜J2.tsx
 ┃ ┃ ┣ 📜J3.tsx
 ┃ ┃ ┣ 📜J4.tsx
 ┃ ┃ ┣ 📜J5.tsx
 ┃ ┃ ┣ 📜J6.tsx
 ┃ ┃ ┣ 📜J7.tsx
 ┃ ┃ ┣ 📜J8.tsx
 ┃ ┃ ┣ 📜J9.tsx
 ┃ ┃ ┣ 📜QuizStep.css
 ┃ ┃ ┗ 📜QuizStep.tsx
 ┃ ┣ 📂ui
 ┃ ┃ ┣ 📜backBtn.tsx
 ┃ ┃ ┣ 📜categoryBtn.tsx
 ┃ ┃ ┗ 📜titleBtn.tsx
 ┃ ┗ 📜Graph.tsx
 ┣ 📂pages
 ┃ ┣ 📜ListenNewsPage.tsx
 ┃ ┣ 📜ListenNewspaper.tsx
 ┃ ┣ 📜MainPage.tsx
 ┃ ┣ 📜ProfilePage.tsx
 ┃ ┣ 📜QuizPage.tsx
 ┃ ┣ 📜ReadNewsPage.tsx
 ┃ ┗ 📜ReadNewspaper.tsx
 ┣ 📂types
 ┃ ┗ 📜index.ts
 ┣ 📂utiles
 ┃ ┣ 📜api.ts
 ┃ ┗ 📜news.ts
 ┣ 📜App.css
 ┣ 📜App.test.tsx
 ┣ 📜App.tsx
 ┣ 📜index.css
 ┣ 📜index.tsx
 ┣ 📜react-app-env.d.ts
 ┣ 📜reportWebVitals.ts
 ┗ 📜setupTests.ts
```

</details>

<details>
<summary>Backend</summary>

```
📦back
 ┣ 📂tokenizer
 ┃ ┣ 📜merges.txt
 ┃ ┗ 📜vocab.json
 ┣ 📜.gitignore
 ┣ 📜app.py
 ┣ 📜category.json
 ┣ 📜clusters.py
 ┣ 📜db.py
 ┣ 📜dict.txt
 ┣ 📜models.py
 ┣ 📜question_generator.py
 ┣ 📜requirements.txt
 ┣ 📜score.py
 ┗ 📜tf-idf.py
```

</details>

<br/>

## 🖥️ 서비스 구현 화면

<a name="item-six"></a>

### 1. 메인페이지

<div align=center>

![main](README_assets/2023-11-29-15-38-51-image.png)

</div>

- 두뇌체조의 메인 페이지로, 뉴스 듣기, 뉴스 읽기, 퀴즈 풀기를 선택할 수 있습니다.

<br/>

### 2. 뉴스 주제 선택

<div align=center>

![category](README_assets/2023-11-29-15-39-15-image.png)

</div>

- 뉴스 듣기, 뉴스 보기를 선택한 후 뉴스 주제를 선택할 수 있습니다.
- 유저가 좋아하는 카테고리를 골라 듣거나 시청 가능합니다.
- 맞춤 카테고리는 유저가 즐겨 듣는 뉴스와 비슷한 뉴스를 추천해줍니다.

<br/>

### 3. 오늘의 문제

<div align=center>

![quiz1](README_assets/2023-11-29-15-39-36-image.png)

![quiz2](README_assets/2023-11-29-15-40-06-image.png)

![quiz3](README_assets/2023-11-29-15-40-44-image.png)

![quiz4](README_assets/2023-11-29-15-41-02-image.png)

![quiz5](README_assets/2023-11-29-15-41-21-image.png)

</div>

- 오늘 시청한 뉴스를 바탕으로 자동으로 퀴즈를 생성해 줍니다.

- 치매 검사인 CERAD-K에 맞춰서 퀴즈를 풀 수 있습니다.(J3, J4, J6, J7 해당)

- 퀴즈를 통해서 치매 예방과 검사가 가능합니다.

<br/>

### 4. 내 정보 확인하기

<div align=center>

![info1](README_assets/2023-11-29-15-41-46-image.png)

![info2](README_assets/2023-11-29-15-42-34-image.png)

</div>

- 날짜별로 내 퀴즈 점수를 볼 수 있습니다.

- 평균값과 나의 지수들을 비교할 수 있습니다.

<br/>

## 💡 개발 프로세스

<a name="item-pro"></a>

<div align=center>

![슬라이드15.PNG](README_assets/49dea48efba327bc1fb383d1846969931ab9caa1.PNG)

![슬라이드16.PNG](README_assets/75d091b515b877ecd8fa286286c3990419d436c9.PNG)

![슬라이드17.PNG](README_assets/a61fb27a0e8f449b0cba22a4e7e084fa28fbd36d.PNG)

![슬라이드18.PNG](README_assets/433777be4e839d023a8f858eacf6ac3e19bde4eb.PNG)

![슬라이드19.PNG](README_assets/e58ae102cc2b100d8f6a9ca6c822c23cb68080c8.PNG)

![슬라이드20.PNG](README_assets/ed20d4cc40a6ac20149ed5d720f6593ee5e87228.PNG)

![슬라이드21.PNG](README_assets/13bc5a12369cc7602631ac7ad32ff4e14236ad3b.PNG)

![슬라이드22.PNG](README_assets/21a13fd07faa2298e469eee87f89e07f447b8997.PNG)

</div>

<br/>

## 👥 팀원 소개

<a name="item-two"></a>

|   **Name**   |                                     김동현                                     |                                    윤자현                                    |                                이상훈                                |                                 최상익                                  |
| :----------: | :----------------------------------------------------------------------------: | :--------------------------------------------------------------------------: | :------------------------------------------------------------------: | :---------------------------------------------------------------------: |
| **Profile**  | ![loading-ag-2237](README_assets/5d0be8de6c3c95185823f70fd15d02dbc864ebad.png) | ![Group 148.png](README_assets/83329abbfb9b9a5089bf0abf483701b6a4469386.png) | ![1.jpg](README_assets/b2344f81373af71ffd83c9237d31d4386903b772.jpg) | ![파일.jpg](README_assets/19e8fee2a6958cfc0122d12f96d5eb8abff46962.jpg) |
| **Position** |                                   BE<br/>FE                                    |                                 팀장<br/>FE                                  |                              BE<br/>DB                               |                                BE<br/>FE                                |
| **Position** |               뉴스 추천 알고리즘 구현<br/>치매위험도 페이지 작성               |             메인 페이지 작성<br/><br/>뉴스 페이지 작성<br/>UX/UI             |          치매확률도 계산 구현<br/>RestApi 작성<br/>DB 관리           |                AI로 퀴즈 생성 구현<br/>퀴즈 페이지 작성                 |
|   **Git**    |                   [GitHub](https://github.com/dongdongx2x2)                    |                   [GitHub](https://github.com/YOONJAHYUN)                    |                  [GitHub](https://github.com/iri95)                  |                  [GitHub](https://github.com/csi9876)                   |

<br/>
