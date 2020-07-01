# seoul metro boarding
Elasticsearch, Kibana를 이용한 서울 지하철 승하차 인원 모티너링, 분석하는 토이 프로젝트

## output
+ 데이터 실시간 시각화
![crawling_march](https://user-images.githubusercontent.com/44857109/86195600-38253700-bb8c-11ea-8eeb-e3ab6a1fec6a.gif)
+ 2020-02-03 ~ 2020-06-25 까지의 지하철 승하차 인원에 대한 대시보드
![dash1](https://user-images.githubusercontent.com/44857109/86195587-32c7ec80-bb8c-11ea-8c85-ea0d8d651d7d.PNG)

## crawling
서울시 공공데이터 open api 데이터를 크롤링
```sh
python3 ./crawl/run.py YYYY-MM-DD
```
or
```sh
python3 ./crawl/run.py # today data
```