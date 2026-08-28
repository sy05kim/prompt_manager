# 🚀 파이썬 프롬프트 관리 프로그램 (Prompt Manager)

ChatGPT 등 AI 모델에게 사용할 나만의 프롬프트를 효율적으로 저장하고 관리하는 파이썬 프로그램입니다.

## 📌 주요 기능 (Functional Requirements)
- **프롬프트 추가**: 제목과 내용을 입력하여 새로운 프롬프트를 등록합니다.
- **목록 조회**: 저장된 모든 프롬프트의 제목을 한눈에 확인합니다.
- **프롬프트 검색**: 제목 키워드를 통해 특정 프롬프트를 빠르게 찾습니다.
- **프롬프트 삭제**: 더 이상 필요 없는 프롬프트를 삭제합니다.
- **데이터 영속화**: 입력한 데이터는 `prompts.json` 파일에 자동 저장되어 프로그램 종료 후에도 유지됩니다.

## 🛠 제약 사항 및 특징 (Constraints)
- **기본 데이터 포함**: 프로그램 실행 시 '민지' 프롬프트를 포함한 3개의 기본 데이터가 내장되어 있습니다.
- **버전 관리**: Git을 사용하여 10개 이상의 세밀한 커밋(Commit) 로그를 남겼습니다.
- **브랜치 전략**: `main` 브랜치 외에 별도의 브랜치를 생성하여 작업 후 병합(Merge)하는 과정을 거쳤습니다.
- **환경**: Python 3.14 버전에서 개발 및 테스트되었습니다.

## 💻 실행 방법
1. 저장소를 클론합니다.
   ```bash
   git clone [본인의 저장소 URL]

## 📂 파일 구조
**main.py**: 프로그램 메인 로직 및 메뉴 인터페이스
**prompts.json**: 프롬프트 데이터 저장 파일
**README.md**: 프로젝트 설명서

## 프로그램 환경 설정 확인

<img width="1080" height="474" alt="image" src="https://github.com/user-attachments/assets/7be93583-2be5-498d-a02b-0f508e2757bf" />

## JSON 파일 데이터

<img width="2136" height="894" alt="image" src="https://github.com/user-attachments/assets/9b5f4669-ace1-43b6-9f37-7d65d46ac8bf" />


## 프로그램 실행
<img width="1106" height="806" alt="image" src="https://github.com/user-attachments/assets/a8124196-7d1a-47ba-b795-24b49b0f6504" />
<img width="1096" height="442" alt="image" src="https://github.com/user-attachments/assets/300c2fd3-f54e-44c1-bf9a-24c9438c2871" />
<img width="1108" height="1018" alt="image" src="https://github.com/user-attachments/assets/94ed2a19-babb-455d-b597-216443dc806f" />
<img width="1102" height="398" alt="image" src="https://github.com/user-attachments/assets/4b75e3b4-bdce-415b-a498-1f8f926bcd12" />

## Git 커밋 히스토리

<img width="1104" height="1276" alt="image" src="https://github.com/user-attachments/assets/fef78e12-777d-438a-a081-ec9f0da26815" />

## Git clone 로그

<img width="1120" height="342" alt="image" src="https://github.com/user-attachments/assets/61645769-c0fd-476d-9269-82c094352695" />

