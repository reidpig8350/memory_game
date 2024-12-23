import pygame
import random
import time

# 初始化 pygame
pygame.init()

# 畫面設定
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("記憶數字遊戲")

# 顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 字型設定
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# 遊戲變數
numbers = []  # 已顯示的數字
user_input = ""  # 使用者輸入暫存
current_number = None  # 畫面上顯示的當前數字
next_number_time = time.time() + 2  # 下一個數字的時間
running = True
error_count = 0  # 錯誤次數
max_numbers = 13  # 最大數字數量
show_all = False  # 是否顯示所有數字

# 遊戲主迴圈
while running:
    screen.fill(WHITE)

    # 在遊戲結束後顯示所有數字
    if show_all:
        for i, number in enumerate(numbers):
            text = font.render(str(number), True, BLACK)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 50 * (i + 1)))
        
        # 添加提示文字
        exit_text = small_font.render("按任意鍵結束遊戲", True, RED)
        screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT - 50))
        
        pygame.display.flip()

        # 處理事件（允許退出）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:  # 任意鍵結束遊戲
                running = False
        continue

    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # 按下 Return 鍵提交答案
                if user_input.isdigit():
                    if int(user_input) == current_number:
                        print("正確!")
                    else:
                        error_count += 1
                        print(f"錯誤! 目前錯誤次數: {error_count}")
                    user_input = ""  # 清空輸入暫存
                else:
                    print("請輸入有效的數字！")
            elif event.unicode.isdigit():  # 累加數字到暫存
                if len(user_input) < 3:  # 限制最多三位數
                    user_input += event.unicode

    # 時間到，顯示下一個數字
    if time.time() >= next_number_time and len(numbers) < max_numbers:
        current_number = random.randint(100, 999)
        numbers.append(current_number)
        print(f"新增數字: {current_number}")  # 除錯用
        next_number_time = time.time() + 2

    # 如果達到最大數字數量，結束遊戲並顯示所有數字
    if len(numbers) == max_numbers:
        show_all = True
        print("遊戲結束！以下是所有的數字：")
        print(numbers)

    # 顯示當前數字
    if current_number is not None:
        text = font.render(str(current_number), True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # 顯示使用者輸入欄位
    input_display = font.render(f"輸入: {user_input}", True, RED if error_count > 0 else BLACK)
    screen.blit(input_display, (WIDTH // 2 - input_display.get_width() // 2, HEIGHT - 100))

    pygame.display.flip()

pygame.quit()