#!/usr/bin/env python3
import os
import subprocess
import datetime

# 設定起始日期為 2024 年 6 月 2 日
def get_start_date():
    return datetime.date(2024, 6, 2)

# 這裡示範一個 7 行 × 10 列的矩陣 (7 天代表一週)
# 實際上你需要根據 I LOVE CODING 的點陣設計這個矩陣
# 例如：1 代表在該天產生 commit，0 則不產生
pattern = [
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],  # 星期日
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],  # 星期一
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],  # 星期二
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],  # 星期三
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],  # 星期四
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],  # 星期五
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],  # 星期六
]

def make_commit(commit_date, message):
    # 將日期格式化為 git commit 所需的格式，例如 "2024-06-02T12:00:00"
    date_str = commit_date.strftime("%Y-%m-%dT12:00:00")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    # 使用 --allow-empty 參數建立空 commit
    subprocess.run(["git", "commit", "--allow-empty", "-m", message], env=env, check=True)

def main():
    start_date = get_start_date()
    print("起始日期：", start_date)
    # 遍歷矩陣：每一列代表一週，每一行代表星期 (0: 星期日, …, 6: 星期六)
    for col in range(len(pattern[0])):
        for row in range(len(pattern)):
            if pattern[row][col] == 1:
                # 計算 commit 的日期：起始日期 + col 週 + row 天
                commit_date = start_date + datetime.timedelta(weeks=col, days=row)
                message = f"Pixel commit: Week {col}, Day {row} ({commit_date})"
                print(f"建立 commit: {commit_date} - {message}")
                make_commit(commit_date, message)
    # 所有 commit 完成後推送到遠端 repository
    subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    main()
