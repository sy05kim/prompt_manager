import json
import os

# 1. 파일 이름 설정 (데이터가 저장될 파일)
DB_FILE = "prompts.json"

# 2. 파일에서 데이터 불러오는 함수
def load_data():
    if os.path.exists(DB_FILE): # 만약 파일이 있으면
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f) # 파일 내용을 읽어서 가져옴
    return [] # 파일이 없으면 빈 리스트 반환

# 3. 파일에 데이터를 저장하는 함수
def save_data(prompts):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=4)

# [함수 1] 프롬프트 추가
def add_prompt(prompt_list):
    title = input("제목: ")
    content = input("내용: ")
    prompt_list.append({"title": title, "content": content})
    save_data(prompt_list) # <--- 추가하자마자 파일에 저장!
    print("✅ 저장되었습니다.")

# [함수 2] 프롬프트 목록 보기
def show_list(prompt_list):
    if not prompt_list:
        print("비어 있습니다.")
        return
    for i, p in enumerate(prompt_list):
        print(f"{i+1}. {p['title']}")

# [함수 3] 프롬프트 검색
def search_prompt(prompt_list):
    keyword = input("검색어: ")
    for p in prompt_list:
        if keyword in p['title'] or keyword in p['content']:
            print(f"제목: {p['title']}\n내용: {p['content']}")

# [함수 4] 프롬프트 삭제
def delete_prompt(prompt_list):
    show_list(prompt_list)
    try:
        idx = int(input("삭제할 번호: ")) - 1
        if 0 <= idx < len(prompt_list):
            del prompt_list[idx]
            save_data(prompt_list) # <--- 삭제하자마자 파일에 저장!
            print("🗑️ 삭제되었습니다.")
        else:
            print("잘못된 번호입니다.")
    except:
        print("숫자를 입력해주세요.")

# 메인 실행부
def main():
    # 프로그램 시작할 때 파일에서 데이터를 불러옵니다.
    prompts = load_data()
    
    while True:
        print("\n--- 프롬프트 관리자 ---")
        print("1. 추가, 2. 목록, 3. 검색, 4. 삭제, 5. 종료")
        choice = input("선택: ")
        
        if choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            show_list(prompts)
        elif choice == "3":
            search_prompt(prompts)
        elif choice == "4":
            delete_prompt(prompts)
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    main()
    