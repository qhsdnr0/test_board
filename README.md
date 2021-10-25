# Readme
## 1. Endpoint
- User(사용자)<br>
/users/signup : 회원가입<br>
/users/signin : 로그인
- Post(게시글)<br>
/posts : 게시글 등록 및 조회<br>
/posts/\<int:post_id\> : 게시글 삭제 및 수정
## 2. API INFO
### 2-1. User
2-1-1. 회원가입<br>
- method : post
- path : /users/signup
- request & response : body : {name :, account :, password :}<br> 
성공 <br>![성공](https://user-images.githubusercontent.com/80999321/138622559-9f224679-640b-4f06-b7c9-65b6801d9507.png)<br>
계정중복<br>![image](https://user-images.githubusercontent.com/80999321/138622670-1dbcab8c-42ec-4a20-a479-36cf2cf27959.png)<br>
계정형식 오류(6~15자, 문자, 숫자 기호는 -만 사용가능)<br>![image](https://user-images.githubusercontent.com/80999321/138623505-c5c95b1f-240b-4a65-b7f5-9689e3572078.png)<br>
비밀번호 형식 오류(8자리 이상, 문자 숫자 특수문자 중 2종류 이상)<br>![image](https://user-images.githubusercontent.com/80999321/138623250-bad2007f-13d7-46e1-a8f4-0ab2d0021f0e.png)<br>
필수 값 미입력<br>![image](https://user-images.githubusercontent.com/80999321/138623373-5fdd3f72-f3ae-4eb6-b76f-27bb8795cf11.png)
- db에 저장되는 데이터 : ![image](https://user-images.githubusercontent.com/80999321/138622762-b0c82c18-d7f9-46c0-ae5c-3a563498583b.png)

2-1-2. 로그인<br>
- method : post
- path : /users/signin
- request & response : body : {name :, account :, password :}<br> 
성공<br>![image](https://user-images.githubusercontent.com/80999321/138623422-4f15d4af-ee65-40d6-b19d-39fd4217a390.png)<br>
필수 값 미입력<br>![image](https://user-images.githubusercontent.com/80999321/138629875-aa49c46b-0220-4376-9cc2-ec8734d4cfa4.png)<br>
계정정보 없음<br>![image](https://user-images.githubusercontent.com/80999321/138629929-d96d50bd-a216-4bc7-aa66-bffd4ea4b7ff.png)<br>
비밀번호 미일치<br>![image](https://user-images.githubusercontent.com/80999321/138629964-26fcaf5a-3d06-4bd6-99ba-0aaa505202ca.png)

### 2-2. Post
2-2-1. 게시물 등록
- method : post
- path : /posts
- request & response : headers : {Authorization : access_token}, body : {title :, content :}<br>
성공<br>![image](https://user-images.githubusercontent.com/80999321/138630125-ce3d1158-da37-4443-b2b3-dfa3419fddda.png)<br>
필수 값 미입력<br>![image](https://user-images.githubusercontent.com/80999321/138630151-9ed60a71-d8cc-4474-a66c-28c0f4aeefaa.png)<br>

2-2-2. 게시물 조회
- method : get
- path : /posts
- request & response : <br>성공<br> pagination 기능 적용으로 4개씩 조회가능<br>![image](https://user-images.githubusercontent.com/80999321/138631006-fa75ccbc-8ac8-461b-a70f-b9c5ade824b1.png)

2-2-3. 게시물 삭제
- method : delete
- path : /posts/\<int:post_id\>
- request & response : headers : {Authorizaion : access_token}<br>
성공<br>![image](https://user-images.githubusercontent.com/80999321/138631110-25564e39-2913-4d77-92a0-f064cedc5e00.png)<br>
게시물 없음<br>![image](https://user-images.githubusercontent.com/80999321/138631037-c324d3ca-d9bb-4aa5-9a88-324ca411b93f.png)<br>
해당 유저의 게시물이 아닐경우<br>![image](https://user-images.githubusercontent.com/80999321/138631073-74c7eedd-679e-4cab-be76-6595a0b645bc.png)

2-2-4. 게시물 수정
- method : put
- path : /posts/\<int:post_id\>
- request & response : headers : headers : {Authorization : access_token}, body : {title :, content :}<br>
성공<br>![image](https://user-images.githubusercontent.com/80999321/138631259-777831cc-1983-4447-bfbb-8666d785f57c.png)<br>
게시물 없음<br>![image](https://user-images.githubusercontent.com/80999321/138631037-c324d3ca-d9bb-4aa5-9a88-324ca411b93f.png)<br>
해당 유저의 게시물이 아닐경우<br>![image](https://user-images.githubusercontent.com/80999321/138631073-74c7eedd-679e-4cab-be76-6595a0b645bc.png)
