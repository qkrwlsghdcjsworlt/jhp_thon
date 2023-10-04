


## 지역 저장소(내 컴퓨터)에 커밋하기

1. git init
2. git config user.name "<깃허브 username>"
3. git config user.email "<깃허브 이메일 주소>"
4. touch README.md
5. 깃과 깃허브 첫 실습 을 README.md 에 작성
6. git add README.md
7. git commit -m "저장소 설명 추가"

## 원격 저장소에 커밋 등록하기

1. New repository 선택하여 원격 저장소 생성
2. 원격 저장소 주소 복사
3. git remote add origin <원격 저장소 주소:https (x), ssh (o)>
4. git push origin main

~~하면 에러가 발생할 것임.~~
이 방법으로 하면 괜찮음. 


## n번째 컴퓨터에서 ssh 연결하기

ssh config --global user.name "<깃허브 username>"
git config --global user.email "<깃허브 이메일 주소>"

eval `ssh-agent`
ssh-add ~/.ssh/id_rsa
ssh -vT git@github.com
ssh -T git@github.com