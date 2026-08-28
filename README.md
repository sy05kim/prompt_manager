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

## Git Version 확인

<img width="2120" height="552" alt="image" src="https://github.com/user-attachments/assets/ed5af914-f3b8-4870-b1da-8c34716aa6cc" />


## 프로그램 환경 설정 확인

<img width="1080" height="474" alt="image" src="https://github.com/user-attachments/assets/7be93583-2be5-498d-a02b-0f508e2757bf" />

## JSON 파일 데이터

<img width="2136" height="894" alt="image" src="https://github.com/user-attachments/assets/9b5f4669-ace1-43b6-9f37-7d65d46ac8bf" />


## 프로그램 실행
<img width="1106" height="806" alt="image" src="https://github.com/user-attachments/assets/a8124196-7d1a-47ba-b795-24b49b0f6504" />
<img width="1098" height="318" alt="image" src="https://github.com/user-attachments/assets/a8e32a31-7062-4448-85cb-c9926e75bad5" />
<img width="1096" height="442" alt="image" src="https://github.com/user-attachments/assets/300c2fd3-f54e-44c1-bf9a-24c9438c2871" />
<img width="1108" height="1018" alt="image" src="https://github.com/user-attachments/assets/94ed2a19-babb-455d-b597-216443dc806f" />
<img width="1102" height="398" alt="image" src="https://github.com/user-attachments/assets/4b75e3b4-bdce-415b-a498-1f8f926bcd12" />

## Git 커밋 히스토리

### 🌿 브랜치 관리 및 워크플로우 실습
- `feature` 브랜치에서 기능을 개발하고 `main` 브랜치에 병합(Merge)하는 과정을 실습했습니다

<img width="1104" height="1276" alt="image" src="https://github.com/user-attachments/assets/fef78e12-777d-438a-a081-ec9f0da26815" />

## Git clone 로그

<img width="1120" height="342" alt="image" src="https://github.com/user-attachments/assets/61645769-c0fd-476d-9269-82c094352695" />

## 🛠 트러블슈팅 (Troubleshooting)

### 1. 함수 인자 전달 오류 (TypeError)
- **문제**: 메뉴에서 '추가' 기능을 선택했을 때 `TypeError: add_prompt() takes 0 positional arguments but 1 was given` 에러 발생.
- **원인**: `main()` 함수에서 `add_prompt(prompts)`와 같이 데이터를 전달하며 호출했으나, 실제 함수 정의부(`def add_prompt()`)에서는 매개변수를 받도록 설정되어 있지 않아 발생한 불일치 문제.
- **해결**: 함수 정의 시 매개변수를 추가하여 리스트 데이터를 정상적으로 전달받도록 수정하였습니다.
  ```python
  # 수정 전
  def add_prompt():
  
  # 수정 후
  def add_prompt(prompts):


## 📊 데이터 구조 선택 및 비교 (List & Dictionary)

본 프로젝트에서는 프롬프트 데이터를 관리하기 위해 **'리스트(List) 내에 딕셔너리(Dictionary)가 포함된 구조'**를 선택하였습니다.

### 1. 데이터 구조 선택 이유
- **리스트(List)**: 프롬프트 목록은 순서가 중요하며, 새로운 프롬프트를 추가하거나 전체를 순회하며 출력하기에 가장 적합한 구조입니다.
- **딕셔너리(Dictionary)**: 하나의 프롬프트가 가지는 다양한 속성(제목, 내용, 카테고리, 즐겨찾기 여부)을 'Key-Value' 형태로 관리하여 코드의 가독성을 높이고 데이터 접근을 용이하게 하기 위해 선택했습니다.

### 2. 리스트와 딕셔너리의 장단점 비교

| 구분 | 리스트 (List) | 딕셔너리 (Dictionary) |
| :--- | :--- | :--- |
| **장점** | - 데이터를 순서대로 저장하고 관리하기 쉬움<br>- 인덱스를 통한 빠른 접근 가능 | - 키(Key)를 통해 데이터의 의미를 즉시 파악 가능<br>- 대량의 데이터에서 특정 키값 검색 시 속도가 매우 빠름 |
| **단점** | - 특정 값을 찾으려면 처음부터 끝까지 검색해야 함 (O(n))<br>- 데이터의 의미를 인덱스 번호로만 판단해야 함 | - 리스트에 비해 상대적으로 메모리 사용량이 많음<br>- 키(Key)의 중복을 허용하지 않음 |

### 3. 프로젝트에서의 활용 예시
- **전체 데이터**: `prompts = [ {prompt1}, {prompt2}, ... ]` (리스트 활용)
- **개별 데이터**: `{"title": "파이썬 도우미", "content": "...", "category": "학습", "favorite": True}` (딕셔너리 활용)
- **결론**: 데이터의 추가/삭제가 빈번하고 순차적인 조회가 필요한 목록 기능에는 **리스트**를, 각 데이터의 세부 속성을 명확하게 정의하고 관리하는 데는 **딕셔너리**를 조합하여 최적의 효율을 냈습니다.

### 🔍 검색 로직 및 예외 처리 (Search Logic)
- **검색 대상 확대**: 사용자가 입력한 키워드가 프롬프트의 **제목(Title)**뿐만 아니라 **내용(Content)**에 포함되어 있어도 검색 결과에 노출되도록 구현하였습니다.
  - 로직: `if keyword in p['title'] or keyword in p['content']`
- **예외 처리 규칙**:
  - 검색 결과가 없을 경우: "검색 결과가 없습니다."라는 안내 메시지를 출력하여 사용자 혼란을 방지했습니다.
  - 빈 키워드 입력 시: 모든 목록을 보여주는 대신, 키워드를 입력하라는 경고 문구를 출력하도록 처리했습니다.

 ### 🌿 브랜치 관리 및 협업 워크플로우
본 프로젝트는 기능별로 브랜치를 분리하여 개발을 진행하였습니다.

- **브랜치 분리 기준**: 
  - **기능 단위 분리**: 새로운 기능을 개발할 때마다 독립된 브랜치를 생성했습니다. (예: `feature/favorite` - 즐겨찾기 기능, `feature/search` - 검색 기능 강화)
  - **이유**: 메인 코드(`main` 브랜치)의 안정성을 유지하면서, 특정 기능에서 발생한 에러가 전체 프로그램에 영향을 주지 않도록 하기 위함입니다.
- **병합(Merge) 의사결정 시점**:
  - 각 브랜치에서 구현하려는 기능이 **단위 테스트(Unit Test)를 통과**하고, 기존 기능들과 **충돌(Conflict)이 없음**을 확인했을 때 `main` 브랜치로 병합을 진행하였습니다.
  - 병합 후에는 해당 브랜치를 삭제하거나 유지하며 이력을 관리했습니다.
 
  ### 🛠 추가 운영 및 유지보수 가이드

1. **중복 방지 정책**
   - 동일한 제목의 프롬프트 등록을 차단하여 데이터 중복을 방지합니다.

2. **병합 충돌 해결 절차**
   - `충돌 위치 확인` -> `코드 수동 수정` -> `정상 작동 테스트` -> `최종 커밋` 순으로 해결합니다.

3. **카테고리 기능 수정 지점**
   - 카테고리 변경 시 `prompts.json` 구조와 `add_prompt`, `search_prompt`, `show_by_category` 함수를 함께 수정해야 합니다.
