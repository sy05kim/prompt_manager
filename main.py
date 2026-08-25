import json
import os

# 파일 이름 설정
FILE_NAME = "prompts.json"

def load_data():
    """파일에서 데이터를 불러오거나, 없으면 기본 데이터 3개를 생성합니다."""
    # 1. 파일이 존재하는지 확인
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        # 2. 파일이 없으면 기본 데이터 3개를 리스트로 반환
        default_prompts = [
            {"title": "영어 번역기", "content": "입력받은 문장을 자연스러운 영어로 번역해줘.", "favorite": False},
            {"title": "코드 리뷰어", "content": "파이썬 코드를 분석해서 버그를 찾고 개선안을 제시해줘.", "favorite": True},
            {"title": "요약 봇", "content": "긴 글을 핵심 내용 3줄로 요약해줘.", "favorite": False}
        ]
        return default_prompts

def save_data(prompts):
    """데이터를 JSON 파일에 저장합니다."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=4)

def main():
    # 프로그램 시작 시 데이터 로드 (기본 데이터 3개 포함됨)
    prompts = load_data()
    
    # 처음 실행 시 파일이 없었다면 기본 데이터를 파일로 저장해둠
    if not os.path.exists(FILE_NAME):
        save_data(prompts)

    while True:
        print("\n--- 🚀 프롬프트 관리 프로그램 ---")
        print("1. 추가  2. 목록  3. 검색  4. 삭제  5. 즐겨찾기 토글  0. 종료")
        choice = input("선택: ")

        if choice == "1":
            title = input("제목: ")
            content = input("내용: ")
            prompts.append({"title": title, "content": content, "favorite": False})
            save_data(prompts)
            print("✅ 추가되었습니다!")

        elif choice == "2":
            print("\n[프롬프트 목록]")
            for i, p in enumerate(prompts, 1):
                fav = "★" if p.get("favorite") else "☆"
                print(f"{i}. {fav} {p['title']} : {p['content']}")

        elif choice == "3":
            keyword = input("검색어: ")
            found = [p for p in prompts if keyword in p['title']]
            for p in found:
                print(f"🔍 검색 결과: {p['title']} - {p['content']}")

        elif choice == "4":
            title = input("삭제할 제목: ")
            prompts = [p for p in prompts if p['title'] != title]
            save_data(prompts)
            print("🗑️ 삭제되었습니다.")

        elif choice == "5":
            title = input("즐겨찾기 상태를 바꿀 제목: ")
            for p in prompts:
                if p['title'] == title:
                    p['favorite'] = not p['favorite']
                    save_data(prompts)
                    print(f"✨ '{title}'의 즐겨찾기 상태가 변경되었습니다.")
                    break

        elif choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요! 👋")
            break
        else:
            print("❌ 잘못된 선택입니다.")

if __name__ == "__main__":
    main()

   # 브랜치 테스트 완료
   
