# 프롬프트를 저장할 빈 리스트
prompts = []

# [함수 1] 프롬프트 추가 기능
def add_prompt(prompt_list):
    new_prompt = input("저장할 프롬프트를 입력하세요: ")
    prompt_list.append(new_prompt)
    print(f"\n[알림] '{new_prompt[:10]}...' 내용이 저장되었습니다.")

# [함수 2] 프롬프트 목록 보기 기능
def show_list(prompt_list):
    # [함수 3] 프롬프트 검색 기능
def search_prompt(prompt_list):
    keyword = input("검색할 단어를 입력하세요: ")
    found = [p for p in prompt_list if keyword in p]
    # [함수 4] 프롬프트 삭제 기능
def delete_prompt(prompt_list):
    show_list(prompt_list) # 목록을 먼저 보여줌
    if not prompt_list:
        return

    try:
        idx = int(input("\n삭제할 번호를 입력하세요: "))
        if 1 <= idx <= len(prompt_list):
            removed = prompt_list.pop(idx - 1)
            print(f"[삭제 완료] '{removed[:10]}...' 항목이 삭제되었습니다.")
        else:
            print("[오류] 유효한 번호가 아닙니다.")
    except ValueError:
        print("[오류] 숫자만 입력해주세요.")
    print(f"\n--- '{keyword}' 검색 결과 ---")
    if not found:
        print("검색 결과가 없습니다.")
    else:
        for i, p in enumerate(found, 1):
            print(f"{i}. {p}")
    print("\n--- 저장된 프롬프트 목록 ---")
    if not prompt_list:
        print("저장된 프롬프트가 없습니다.")
    else:
        for i, p in enumerate(prompt_list, 1):
            print(f"{i}. {p}")

# [메인 함수] 프로그램의 전체 흐름
def main():
    while True:
               print("1. 프롬프트 추가")
        print("2. 프롬프트 목록 보기")
        print("3. 프롬프트 검색")
        print("4. 프롬프트 삭제")  # 추가
        print("5. 종료")           # 번호 변경

        choice = input("\n메뉴를 선택하세요 (1~5): ")
        
        if choice == '1':
            add_prompt(prompts)
        elif choice == '2':
            show_list(prompts)
        elif choice == '3':
            search_prompt(prompts)
        elif choice == '4':        # 추가
            delete_prompt(prompts)
        elif choice == '5':        # 번호 변경
            print("프로그램을 종료합니다.")
            break
        
# 프로그램 시작점
if __name__ == "__main__":
    main()
