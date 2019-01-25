# 02 Web Page 구현

### 01_layout.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!-- bootstrap -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
    <!-- font awesome-->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- layout.css-->
    <link rel="stylesheet" href="01_layout.css">
    <!-- 구글 폰트 -->
    <link href="https://fonts.googleapis.com/css?family=Reenie+Beanie|Sacramento" rel="stylesheet">

    <title>영화추천사이트</title>
</head>
<style>
body{
    height: 2000px;
}
</style>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light sticky" style="z-index: 1;">
        <a class="navbar-brand" href="#">영화추천시스템</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
                <a class="nav-link" href="#">Home <span class="sr-only"></span></a>
            </li>
            <li class="nav-item">
                <p class="nav-link" >친구 평점 보러가기</p>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Log In
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <p class="dropdown-item">Log In</p>
                <p class="dropdown-item">Join Us</p>
                </div>
            </li>
            </ul>
        </div>
        </nav>
        <header id = "header">
            <div class="jumbotron jumbotron-fluid layout-background" style="background-size:contain;">
                <div class="container container_margin">
                    <h2 class="display-15 layout-text">당신에게 어울리는 영화를<br> 추천해드립니다.</h2><br>
                    <h4 class="layout_font">Recommend a Movie</h4>
                </div>
            </div>
        </header>


      <footer id= "footer">
          <div style="float: left;">
            <span style="font-size: 33px;">JungEun Lee</span>
          </div>
          <div style="float: right;margin-top: 10px;">
            <a href="#header" style="color: white;"><i class="fa fa-arrow-circle-up fa-2x"></i></a>
          </div>
      </footer>
</body>
</html>
```

### 01_layout.css

```css
.layout-background {
    background-image:url(assets/movie-918655_1920.jpg);
    height: 350px;
    margin-top: 60px;
  }

.layout-text{
    color: white;
    text-align: center; 
    background-color:rgba(37, 34, 34, 0.5);
}

.layout_font{
    /* font-family: 'Black Han Sans', sans-serif; */
    /* font-family: 'Poor Story', cursive; */
    color: rgb(252, 252, 252);
    font-family: 'Sacramento', cursive;
    text-align: center;

}

.sticky {
    position: fixed;
    top: 0;
    width: 100%;
}

#header{ 
    height:350px; 
    width:100%; 
    background-image:url(assets/movie-918655_1920.jpg);
} 

#footer{ 
    height:50px; 
    width:100%; 
    background-color: dimgrey;
    padding-left: 3rem;
    padding-right: 3rem;
    font-family: 'Reenie Beanie', cursive;
} 

.container_margin{
    padding: 60px 0px;

}
```



### head 사이

- bootstrap link,script 넣기

- font awesome 넣기

- 해당 css파일 link rel 연결

- 구글폰트 link 넣기

  

### navbar 를 제일 위로 놓기

`style="z-index: 1;"` z인덱스를 최상위로!



### navbar 고정시키기

```css
.sticky {
    position: fixed;
    top: 0;
    width: 100%;
}
```



### navbar item 오른쪽,왼쪽 정렬하기

`<ul class="navbar-nav ml-auto">`

`<ul class="navbar-nav mr-auto">`



### 배경이미지 넣기

`background-image:url(assets/movie-918655_1920.jpg);`



### 왼쪽 오른쪽 정렬하기

div를 나눠

`<div style="float: left;"><div>`

`<div style="float: right;"><div>`



---

---

### 02_movie.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!-- bootstrap -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
    <!-- font awesome-->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- movie.css-->
    <link rel="stylesheet" href="02_movie.css">
    <!-- 구글 폰트 -->
    <link href="https://fonts.googleapis.com/css?family=Reenie+Beanie|Sacramento" rel="stylesheet">

    <title>영화추천사이트</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light sticky" style="z-index: 1;">
        <a class="navbar-brand" href="#">영화추천시스템</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
                <a class="nav-link" href="#">Home <span class="sr-only"></span></a>
            </li>
            <li class="nav-item">
                <p class="nav-link" >친구 평점 보러가기</p>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Log In
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <p class="dropdown-item">Log In</p>
                <p class="dropdown-item">Join Us</p>
                </div>
            </li>
            </ul>
        </div>
        </nav>
      <header id = "header">
        <div class="jumbotron jumbotron-fluid layout-background" style="background-size:contain;">
            <div class="container container_margin">
                <h2 class="display-15 layout-text">당신에게 어울리는 영화를<br> 추천해드립니다.</h2><br>
                <h4 class="layout_font">Recommend a Movie</h4>
            </div>
            </div>
      </header>


        <!-- container 생성 -->
        <div class="container">
            <h3 class="movie_subtitle">영화 목록</h3>
            <hr style="width: 70px;">
            <!-- row 생성 -->
            <div class="row mt-5 justify-content-center">
                <div class="card col-sm-5 col-md-4 col-lg-3 card-margin">
                    <img src="assets/20184105.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다.">
                    <div class="card-body text-left" style="padding-right: 5px;padding-left: 5px;">
                        <h4>말모이&nbsp;<span class="badge badge-info">9.04</span></h4><hr>
                        <p class="card-text card-text1">드라마</p>
                        <p class="card-text card-text1">개봉일: 2019.01.09.</p>
                        <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=167699">
                            <button type="button" class="btn btn-success" style="font-size: 14px;margin-top:5px;">영화정보 보러가기</button>
                        </a>
                    </div>
                </div>
                <div class="card col-sm-5 col-md-4 col-lg-3 card-margin">
                    <img src="assets/20176251.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다.">
                    <div class="card-body text-left" style="padding-right: 5px;padding-left: 5px;">
                        <h4>내안의 그놈&nbsp;<span class="badge badge-dark">8.69</span></h4><hr>
                        <p class="card-text card-text1">판타지</p>
                        <p class="card-text card-text1">개봉일: 2019.01.09.</p>
                        <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=164172">
                            <button type="button" class="btn btn-success" style="font-size: 14px;margin-top:5px;">영화정보 보러가기</button>
                        </a>
                    </div>
                </div>
                <div class="card col-sm-5 col-md-4 col-lg-3 card-margin">
                    <img src="assets/20182544.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다.">
                    <div class="card-body text-left" style="padding-right: 5px;padding-left: 5px;">
                        <h4>글래스&nbsp;<span class="badge badge-dark">7.69</span></h4><hr>
                        <p class="card-text card-text1">드라마</p>
                        <p class="card-text card-text1">개봉일: 2019.01.17.</p>
                        <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=163826">
                            <button type="button" class="btn btn-success" style="font-size: 14px;margin-top:5px;">영화정보 보러가기</button>
                        </a>
                    </div>
                </div>

                <div class="card col-sm-5 col-md-4 col-lg-3 card-margin">
                    <img src="assets/20189463.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다.">
                    <div class="card-body text-left" style="padding-right: 5px;padding-left: 5px;">
                        <h4>주먹왕 랄프2&nbsp;<span class="badge badge-dark">8.76</span></h4><hr>
                        <p class="card-text card-text1">애니메이션</p>
                        <p class="card-text card-text1">개봉일: 2019.01.03.</p>
                        <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=152632">
                            <button type="button" class="btn btn-success" style="font-size: 14px;margin-top:5px;">영화정보 보러가기</button>
                        </a>
                    </div>
                </div>
                
                <div class="card col-sm-5 col-md-4 col-lg-3 card-margin">
                    <img src="assets/20180290.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다.">
                    <div class="card-body text-left" style="padding-right: 5px;padding-left: 5px;">
                        <h4>아쿠아맨&nbsp;<span class="badge badge-dark">8.39</span></h4><hr>
                        <p class="card-text card-text1">액션</p>
                        <p class="card-text card-text1">개봉일: 2018.12.19.</p>
                        <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=151153">
                            <button type="button" class="btn btn-success" style="font-size: 14px;margin-top:5px;">영화정보 보러가기</button>
                        </a>
                        </div>
                </div>

                <div class="card col-sm-5 col-md-4 col-lg-3 card-margin">
                    <img src="assets/20186324.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다.">
                    <div class="card-body text-left" style="padding-right: 5px;padding-left: 5px;">
                        <h4>언더독&nbsp;<span class="badge badge-dark">9.49</span></h4><hr>
                        <p class="card-text card-text1">애니메이션</p>
                        <p class="card-text card-text1">개봉일: 2019.01.16.</p>
                        <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=144318">
                            <button type="button" class="btn btn-success" style="font-size: 14px;margin-top:5px;">영화정보 보러가기</button>
                        </a>
                        </div>
                </div>
                    
                    
            </div>
        </div>


      <footer id= "footer">
          <div style="float: left;">
            <span style="font-size: 33px;">JungEun Lee</span>
          </div>
          <div style="float: right;margin-top: 10px;">
            <a href="#header" style="color: white;"><i class="fa fa-arrow-circle-up fa-2x"></i></a>
          </div>
      </footer>
</body>
</html>
```

### 02_movie.css

```css
.card-text1{
    font-size: 13px;
    margin-bottom: 0px;
}
.card-margin{
    margin-top: 1rem;
    margin-bottom: 1rem;
}
.movie_subtitle{
    text-align: center;
    margin: 3rem;
    margin-bottom: 18px;
}

.layout-background {
    background-image:url(assets/movie-918655_1920.jpg);
    height: 350px;
    margin-top: 60px;
  }

.layout-text{
    color: white;
    text-align: center; 
    background-color:rgba(37, 34, 34, 0.5);
}

.layout_font{
    /* font-family: 'Black Han Sans', sans-serif; */
    /* font-family: 'Poor Story', cursive; */
    color: rgb(252, 252, 252);
    font-family: 'Sacramento', cursive;
    text-align: center;

}

.sticky {
    position: fixed;
    top: 0;
    width: 100%;
}

#header{ 
    height:350px; 
    width:100%; 
    background-image:url(assets/movie-918655_1920.jpg);
} 

#footer{ 
    height:50px; 
    width:100%; 
    background-color: dimgrey;
    padding-left: 3rem;
    padding-right: 3rem;
    font-family: 'Reenie Beanie', cursive;
} 

.container_margin{
    padding: 60px 0px;

}
```



### contanier card

- 576px 미만 : 1개 

- 576px 이상 768px 미만 : 2개 

- 768px 이상 992px 미만 : 3개 

- 992px 이상 : 4개

`class="card col-sm-5 col-md-4 col-lg-3"`



---

---

### 03_detail_view.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!-- bootstrap -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
    <!-- font awesome-->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- movie.css-->
    <link rel="stylesheet" href="02_movie.css">
    <!-- 구글 폰트 -->
    <link href="https://fonts.googleapis.com/css?family=Reenie+Beanie|Sacramento" rel="stylesheet">
    <!-- href 경로는 꼭 확인하세요! --> 
    <link rel="icon" type="image/png" sizes="96x96" href="assets/favicon96x96.png">
    
    <title>영화추천사이트</title>
</head>
<body>
      <nav class="navbar navbar-expand-lg navbar-light bg-light sticky" style="z-index: 1;">
        <a class="navbar-brand" href="#">영화추천시스템</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
                <a class="nav-link" href="#">Home <span class="sr-only"></span></a>
            </li>
            <li class="nav-item">
                <p class="nav-link" >친구 평점 보러가기</p>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Log In
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <p class="dropdown-item">Log In</p>
                <p class="dropdown-item">Join Us</p>
                </div>
            </li>
            </ul>
        </div>
        </nav>
      <header id = "header">
        <div class="jumbotron jumbotron-fluid layout-background" style="background-size:contain;">
            <div class="container container_margin">
                <h2 class="display-15 layout-text">당신에게 어울리는 영화를<br> 추천해드립니다.</h2><br>
                <h4 class="layout_font">Recommend a Movie</h4>
            </div>
            </div>
      </header>


        <!-- container 생성 -->
      <section>
        <div class="container">
            <h3 class="movie_subtitle">영화 목록</h3>
            <hr style="width: 70px;">
            <!-- row 생성 -->
            <div class="row mt-5 justify-content-center">
                <div class="card col-sm-5 col-md-4 col-lg-3 card-margin">
                    <img src="assets/20184105.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다."
                    data-target="#movie-1-modal" data-toggle="modal">
                    <!-- 모달창 -->
                    <div id="movie-1-modal" class="modal" >
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                <h5 class="modal-title">말모이, MAL·MO·E: The Secret Mission </h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                                </div>
                                <div class="modal-body">
                                    <img src="assets/20184105-1.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다.">
                                <br><br><p>12세이상관람가</p>
                                <p>누적 관객수: 2,224,910</p>
                                <hr>
                                <p>"까막눈 판수, 우리말에 눈뜨다! vs 조선어학회 대표 정환, ‘우리’의 소중함에 눈뜨다!<br><br>
                                        1940년대 우리말이 점점 사라져가고 있는 경성. 얼마 남지 않은 시간, 바짝 조여오는 일제의 감시를 피해 ‘말모이’를 끝내야 하는데… 우리말이 금지된 시대, 말과 마음이 모여 사전이 되다."</p>
                                </div>
                                <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="card-body text-left" style="padding-right: 5px;padding-left: 5px;">
                        <h4>말모이&nbsp;<span class="badge badge-info">9.04</span></h4><hr>
                        <p class="card-text card-text1">드라마</p>
                        <p class="card-text card-text1">개봉일: 2019.01.09.</p>
                        <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=167699">
                            <button type="button" class="btn btn-success" style="font-size: 14px;margin-top:5px;">영화정보 보러가기</button>
                        </a>
                    </div>
                </div>
                <div class="card col-sm-5 col-md-4 col-lg-3 card-margin">
                    <img src="assets/20176251.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다."
                    data-target="#movie-2-modal" data-toggle="modal">
                    <!-- 모달창 -->
                    <div id="movie-2-modal" class="modal" >
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                <h5 class="modal-title">내안의 그놈, The Dude in Me </h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                                </div>
                                <div class="modal-body">
                                    <img src="assets/20176251-1.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다.">
                                <br><br><p>15세이상관람가</p>
                                <p>누적 관객수: 1,597,263</p>
                                <hr>
                                <p>"나 너니? 너 나니?? 제대로 바뀐 아재와 고딩, 웃음 대환장 파티!<br>
                                        엘리트 아재 판수(박성웅)를 우연히 옥상에서 떨어진 고등학생 동현(진영)이 덮치면서 제대로 바뀐다.  게다가 판수는 동현의 몸으로 첫사랑 미선(라미란)과 존재도 몰랐던 딸 현정(이수민)을 만나게 되는데…  대유잼의 향연, 넌 이미 웃고 있다!"</p>
                                </div>
                                <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="card-body text-left" style="padding-right: 5px;padding-left: 5px;">
                        <h4>내안의 그놈&nbsp;<span class="badge badge-dark">8.69</span></h4><hr>
                        <p class="card-text card-text1">판타지</p>
                        <p class="card-text card-text1">개봉일: 2019.01.09.</p>
                        <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=164172">
                            <button type="button" class="btn btn-success" style="font-size: 14px;margin-top:5px;">영화정보 보러가기</button>
                        </a>
                    </div>
                </div>
                <div class="card col-sm-5 col-md-4 col-lg-3 card-margin">
                    <img src="assets/20182544.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다."
                    data-target="#movie-3-modal" data-toggle="modal">
                    <!-- 모달창 -->
                    <div id="movie-3-modal" class="modal" >
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                <h5 class="modal-title">글래스, Glass </h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                                </div>
                                <div class="modal-body">
                                    <img src="assets/20182544-1.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다.">
                                <br><br><p>15세이상관람가</p>
                                <p>누적 관객수: 339,707</p>
                                <hr>
                                <p>
                                        "24개의 인격ㆍ강철 같은 신체ㆍ천재적 두뇌<br>
                                        통제불가한 24번째 인격 비스트를 깨운 케빈, <br>
                                        강철 같은 신체 능력을 지닌 의문의 남자 던, <br>
                                        천재적 두뇌를 지닌 미스터리한 설계자 미스터 글래스, <br>
                                        마침내 그들이 한 자리에 모이게 되고 이들의 존재가 세상에 드러나면서 예상치 못한 일이 벌어지는데……."
                                </p>
                                </div>
                                <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                </div>
                            </div>
                        </div>
                    </div>            

                    <div class="card-body text-left" style="padding-right: 5px;padding-left: 5px;">
                        <h4>글래스&nbsp;<span class="badge badge-dark">7.69</span></h4><hr>
                        <p class="card-text card-text1">드라마</p>
                        <p class="card-text card-text1">개봉일: 2019.01.17.</p>
                        <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=163826">
                            <button type="button" class="btn btn-success" style="font-size: 14px;margin-top:5px;">영화정보 보러가기</button>
                        </a>
                    </div>
                </div>

                <div class="card col-sm-5 col-md-4 col-lg-3 card-margin">
                    <img src="assets/20189463.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다."
                    data-target="#movie-4-modal" data-toggle="modal">
                    <!-- 모달창 -->
                    <div id="movie-4-modal" class="modal" >
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                <h5 class="modal-title">주먹왕 랄프2, Ralph Breaks the Internet </h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                                </div>
                                <div class="modal-body">
                                    <img src="assets/20189463-1.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다.">
                                <br><br><p>전체관람가</p>
                                <p>누적 관객수: 1,606,967</p>
                                <hr>
                                <p>
                                    "오락실 게임 세상에 이어 이번엔 인터넷 세상이 발칵 뒤집힌다?!<br>
                                    지금껏 경험한 적 없는 엄청난 스케일과 새로운 재미에 흠뻑 빠진 ‘랄프’와<br>
                                        ‘바넬로피’는 랜섬웨어급 사고로 인터넷 세상을 혼란에 빠뜨리는데…<br>
                                    과연, 이들은 무사히 집에 돌아갈 수 있을까?"   
                                </p>
                                </div>
                                <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                </div>
                            </div>
                        </div>
                    </div> 

                    <div class="card-body text-left" style="padding-right: 5px;padding-left: 5px;">
                        <h4>주먹왕 랄프2&nbsp;<span class="badge badge-dark">8.76</span></h4><hr>
                        <p class="card-text card-text1">애니메이션</p>
                        <p class="card-text card-text1">개봉일: 2019.01.03.</p>
                        <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=152632">
                            <button type="button" class="btn btn-success" style="font-size: 14px;margin-top:5px;">영화정보 보러가기</button>
                        </a>
                    </div>
                </div>
                
                <div class="card col-sm-5 col-md-4 col-lg-3 card-margin">
                    <img src="assets/20180290.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다."
                    data-target="#movie-5-modal" data-toggle="modal">
                    <!-- 모달창 -->
                    <div id="movie-5-modal" class="modal" >
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                <h5 class="modal-title">아쿠아맨, AQUAMAN</h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                                </div>
                                <div class="modal-body">
                                    <img src="assets/20180290-1.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다.">
                                <br><br><p>12세이상관람가</p>
                                <p>누적 관객수: 5,019,236</p>
                                <hr>
                                <p>
                                    땅의 아들이자 바다의 왕, 심해의 수호자인 슈퍼히어로 아쿠아맨의 탄생을 그린 액션 블록버스터  
                                </p>
                                </div>
                                <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                </div>
                            </div>
                        </div>
                    </div> 


                    <div class="card-body text-left" style="padding-right: 5px;padding-left: 5px;">
                        <h4>아쿠아맨&nbsp;<span class="badge badge-dark">8.39</span></h4><hr>
                        <p class="card-text card-text1">액션</p>
                        <p class="card-text card-text1">개봉일: 2018.12.19.</p>
                        <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=151153">
                            <button type="button" class="btn btn-success" style="font-size: 14px;margin-top:5px;">영화정보 보러가기</button>
                        </a>
                        </div>
                </div>

                <div class="card col-sm-5 col-md-4 col-lg-3 card-margin">
                    <img src="assets/20186324.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다."
                    data-target="#movie-6-modal" data-toggle="modal">
                    <!-- 모달창 -->
                    <div id="movie-6-modal" class="modal" >
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                <h5 class="modal-title">언더독, Underdog</h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                                </div>
                                <div class="modal-body">
                                    <img src="assets/20186324-1.jpg" class="card-img-top" alt="이미지를 읽을 수 없습니다.">
                                <br><br><p>전체관람가</p>
                                <p>누적 관객수: 122,479</p>
                                <hr>
                                <p>
                                    "견생역전을 꿈꾸는 댕댕이들의 위대한 모험이 시작된다!<br>
                                    하루아침에 운명이 바뀐 강아지 ‘뭉치’는 우연히 만난 <br>
                                    거리 생활의 고참 ‘짱아’ 일당을 만나 목숨을 구하게 된다.<br>
                                    차츰 ‘짱아’ 무리의 스트릿 라이프에 적응하던 찰나 그들의 <br>
                                    소중한 아지트가 사라질 위기에 처하고,<br>
                                    마침내 그들은 진정한 자유를 찾기 위한 모험을 떠나기로 결심하는데…"
                                </p>
                                </div>
                                <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                </div>
                            </div>
                        </div>
                    </div> 

                    <div class="card-body text-left" style="padding-right: 5px;padding-left: 5px;">
                        <h4>언더독&nbsp;<span class="badge badge-dark">9.49</span></h4><hr>
                        <p class="card-text card-text1">애니메이션</p>
                        <p class="card-text card-text1">개봉일: 2019.01.16.</p>
                        <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=144318">
                            <button type="button" class="btn btn-success" style="font-size: 14px;margin-top:5px;">영화정보 보러가기</button>
                        </a>
                        </div>
                </div>       
            </div>
        </div>
    </section>

      <footer id= "footer">
          <div style="float: left;">
            <span style="font-size: 33px;">JungEun Lee</span>
          </div>
          <div style="float: right;margin-top: 10px;">
            <a href="#header" style="color: white;"><i class="fa fa-arrow-circle-up fa-2x"></i></a>
          </div>
      </footer>
</body>
</html>
```



### 03_detail_view.css

```css
.card-text1{
    font-size: 13px;
    margin-bottom: 0px;
}
.card-margin{
    margin-top: 1rem;
    margin-bottom: 1rem;
}
.movie_subtitle{
    text-align: center;
    margin: 3rem;
    margin-bottom: 18px;
}

.layout-background {
    background-image:url(assets/movie-918655_1920.jpg);
    height: 350px;
    margin-top: 60px;
  }

.layout-text{
    color: white;
    text-align: center; 
    background-color:rgba(37, 34, 34, 0.5);
}

.layout_font{
    /* font-family: 'Black Han Sans', sans-serif; */
    /* font-family: 'Poor Story', cursive; */
    color: rgb(252, 252, 252);
    font-family: 'Sacramento', cursive;
    text-align: center;

}

.sticky {
    position: fixed;
    top: 0;
    width: 100%;
}

#header{ 
    height:350px; 
    width:100%; 
    background-image:url(assets/movie-918655_1920.jpg);
} 

#footer{ 
    height:50px; 
    width:100%; 
    background-color: dimgrey;
    padding-left: 3rem;
    padding-right: 3rem;
    font-family: 'Reenie Beanie', cursive;
} 

.container_margin{
    padding: 60px 0px;

}
```



### 모달창 띄우기

`data-target="#movie-1-modal" data-toggle="modal"`

data-target -> id값 -> 이 id를 가진 div를 만들어야함 

ex)    `<div id="movie-1-modal" class="modal" >`

