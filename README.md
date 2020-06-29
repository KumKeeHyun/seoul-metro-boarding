# seoul metro boarding
Elasticsearch, Kibana를 이용한 서울 지하철 승하차 인원 모티너링, 분석하는 토이 프로젝트

## output
+ 2020-02-03 ~ 2020-06-25 까지의 지하철 승하차 인원에 대한 대시보드
![dashboard1](https://user-images.githubusercontent.com/44857109/85985255-705e3580-ba25-11ea-998e-b9851923182a.png)
+ 2020년 2월 중에서 1호선, 2호선, 7호선의 데이터
![dashboard2](https://user-images.githubusercontent.com/44857109/85985302-85d35f80-ba25-11ea-83f3-5228400a50be.png)

## crawling
서울시 공공데이터 open api 데이터를 크롤링
```sh
python3 ./crawl/run.py YYYY-MM-DD
```
or
```sh
python3 ./crawl/run.py # today data
```