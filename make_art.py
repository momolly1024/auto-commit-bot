#!/usr/bin/env python3
import os
import subprocess
import datetime

# --- 字母的 5x7 點陣定義 ---
# 每個矩陣有 7 列，內部數字 1 表示要 commit（點亮），0 表示空白

# 字母 I
I = [
    [1,1,1,1,1],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [1,1,1,1,1]
]

# 字母 L
L = [
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,1,1,1,1]
]

# 字母 O
O = [
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
]

# 字母 V
V = [
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,0,1,0,0]
]

# 字母 E
E = [
    [1,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,1,1,1,1]
]

# 空白（間隔）：單一一欄全 0
space = [
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0]
]

# 字母 C
C = [
    [0,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [0,1,1,1,1]
]

# 字母 D
D = [
    [1,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,0]
]

# 字母 N
N = [
    [1,0,0,0,1],
    [1,1,0,0,1],
    [1,0,1,0,1],
    [1,0,0,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1]
]

# 字母 G
G = [
    [0,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
]

# --- 將各字母矩陣水平拼接 ---
def combine_letters(letter_list):
    """
    將多個 7xN 的矩陣水平拼接成一個 7x(total N) 的矩陣。
    """
    rows = 7
    combined = [[] for _ in range(rows)]
    for letter in letter_list:
        for i in range(rows):
            combined[i].extend(letter[i])
    return combined

# 依照「I LOVE CODING」的順序拼接字母：
# 序列：I, 空白, L, O, V, E, 空白, C, O, D, I, N, G
letters = [I, space, L, O, V, E, space, C, O, D, I, N, G]
pattern = combine_letters(letters)

# 可選：列印出點陣矩陣來檢查結果（1 顯示為 #，0 為空格）
def print_pattern(matrix):
    for row in matrix:
        print("".join("#" if pixel else " " for pixel in row))

if __name__ == "__main__":
    # 例如，檢查最終產生的點陣
    print("I LOVE CODING 的點陣圖：")
    print_pattern(pattern)

    # 設定起始日期（可自行調整，此例設定為 2024-06-02）
    start_date = datetime.date(2024, 6, 2)
    print("起始日期：", start_date)

    # 依據點陣圖產生 commit：
    # 每個週為一欄，每一行對應星期 (0: 星期日, ... , 6: 星期六)
    for col in range(len(pattern[0])):
        for row in range(len(pattern)):
            if pattern[row][col] == 1:
                commit_date = start_date + datetime.timedelta(weeks=col, days=row)
                message = f"Pixel commit: Week {col}, Day {row} ({commit_date})"
                print(f"建立 commit: {commit_date} - {message}")
                # 設定 commit 的日期
                date_str = commit_date.strftime("%Y-%m-%dT12:00:00")
                env = os.environ.copy()
                env["GIT_AUTHOR_DATE"] = date_str
                env["GIT_COMMITTER_DATE"] = date_str
                subprocess.run(["git", "commit", "--allow-empty", "-m", message], env=env, check=True)

    # 推送 commit（確保已配置好 Git 使用者資訊及憑證）
    subprocess.run(["git", "push"], check=True)
