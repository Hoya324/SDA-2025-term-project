# KBO 타자의 타격 일관성 분석

일별 타격 기록으로 변동계수(CV)를 계산해 장타력과 안정성의 관계, 포지션·경력별 차이, 성적 예측 가능성을 살펴본 통계 분석 프로젝트입니다.

## 한눈에 보기
- 핵심 질문: 장타형이 안타형보다 변동성이 큰가? 포지션·경력이 일관성에 영향을 주는가? CV로 성적을 예측할 수 있는가?
- 주요 결과: 장타형 CV가 유의미하게 더 큼(p=0.023), 포지션별 차이는 없음, 베테랑이 신인보다 안정적(p=0.008). CV 단독 예측력은 낮지만 OPS 다중 회귀는 R²≈0.67.
- 산출물: 노트북 4개(전처리→EDA→가설검정→회귀), 그래프/CSV는 `outputs/`, 최종 보고서는 `report/최종_보고서.md`.

## 프로젝트 구조
```
SDA-2025-term-project/
├── notebooks/01_preprocessing.ipynb      # 데이터 전처리
├── notebooks/02_eda.ipynb                # 탐색적 분석 + 시각화
├── notebooks/03_hypothesis_testing.ipynb # 가설 검정
├── notebooks/04_regression.ipynb         # 회귀 모델링
├── outputs/                              # 그래프 및 중간 산출물
└── report/최종_보고서.md                 # 최종 보고서 (이미지 포함)
```

## 데이터
- 위치: `data/` (노트북에서 절대경로 `/Users/hoyana/Desktop/01_sideproject/SDA-2025-term-project/data/`로 참조)
- 주요 파일: `Regular_Season_Batter.csv`, `Regular_Season_Batter_Day_by_Day_b4.csv`, `Pre_Season_Batter.csv`, `submission.csv`
- 핵심 지표: `avg`, `OPS`, `HR`, `AB`, `H`, `position`, 계산된 `CV`
