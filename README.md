<h1 align="center"> 두뇌 퍼즐 </h1>

## 📝 목차

[프로젝트 개요](#item-one)

[기술 스택](#item-three)

[서버 아키텍처](#item-four)

[서비스 구현 화면](#item-five)

[팀원 소개](#item-two)

[느낀 점](#item-end)

## 📖 프로젝트 개요

<a name="item-one"></a>

<div>

<strong>진행 기간 </strong>: 2023.11.17 ~ 2023.11.22

<strong>목표</strong>

- 일상 생활 속에서 노년층이 치매를 예방하도록 서비스를 제공하는 뉴스 플랫폼

- 개인의 관심 키워드로 뉴스 추천

- 뉴스 내용을 기반으로 AI를 통해 문제 생성

- 퀴즈 결과를 CERAD-K 지표와 연결하여 치매 위험도 분석

</div>

<br/>

## 🛠️ 기술 스택

<a name="item-three"></a>

## 💻 IDE

![VSCode](https://img.shields.io/badge/VisualStudioCode-007ACC?style=for-the-badge&logo=VisualStudioCode&logoColor=white)
![IntelliJ](https://img.shields.io/badge/intellijidea-000000?style=for-the-badge&logo=intellijidea&logoColor=white)

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

<br/>

## 👥 팀원 소개

<a name="item-two"></a>

| **Name**     | 김동현                                       | 윤자현                                     | 이상훈                                  | 최상익                                  |
|:------------:|:-----------------------------------------:|:---------------------------------------:|:------------------------------------:|:------------------------------------:|
| **Profile**  |                                           |                                         |                                      |                                      |
| **Position** | BE<br/>FE                                 | 팀장<br/>FE                               | BE<br/>DB                            | BE<br/>FE                            |
| **Position** | 뉴스 추천 알고리즘 구현<br/>치매위험도 페이지 작성            | 메인 페이지 작성<br/><br/>뉴스 페이지 작성<br/>UX/UI  | 치매확률도 계산 구현<br/>RestApi 작성<br/>DB 관리 | AI로 퀴즈 생성 구현<br/>퀴즈 페이지 작성           |
| **Git**      | [GitHub](https://github.com/dongdongx2x2) | [GitHub](https://github.com/YOONJAHYUN) | [GitHub](https://github.com/iri95)   | [GitHub](https://github.com/csi9876) |

<br/>
