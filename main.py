def main():
    # 프롬프트를 저장할 빈 리스트를 만듭니다.
    prompts = []

    while True:
        print("\n--- 파이썬 프롬프트 관리자 ---")
        print("1. 프롬프트 추가")
        print("2. 프롬프트 목록 보기")
        print("3. 종료")
        
        choice = input("\n메뉴를 선택하세요 (1~3): ")

        if choice == '1':
            # 사용자로부터 프롬프트 내용을 입력받습니다.
            new_prompt = input("저장할 프롬프트를 입력하세요: ")
            prompts.append(new_prompt) # 리스트에 추가
            print(f"\n[알림] '{new_prompt[:10]}...' 내용이 저장되었습니다.")

        elif choice == '2':
            print("\n--- 저장된 프롬프트 목록 ---")
            # 리스트가 비어있는지 확인합니다.
            if not prompts:
                print("저장된 프롬프트가 없습니다.")
            else:
                # 번호와 함께 목록을 출력합니다.
                for i, p in enumerate(prompts, 1):
                    print(f"{i}. {p}")

        elif choice == '3':
            print("\n[안내] 프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
            break
        else:
            print("\n[오류] 잘못된 선택입니다. 1~3 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()
    