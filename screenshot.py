import pyautogui
import schedule
import time
import os
from datetime import datetime
import sys

# 実行ファイルのディレクトリを取得
if getattr(sys, 'frozen', False):
    # PyInstallerによってパッケージ化された実行ファイルの場合
    script_dir = os.path.dirname(sys.executable)
else:
    # 通常のPythonスクリプトとして実行される場合
    script_dir = os.path.dirname(os.path.abspath(__file__))

# スクリーンショットを保存するディレクトリ
output_dir = os.path.join(script_dir, "screenshots")
os.makedirs(output_dir, exist_ok=True)

def take_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(output_dir, f"screenshot_{timestamp}.png")
    pyautogui.screenshot(filename)
    print(f"Screenshot saved to {filename}")

# 1分ごとにスクリーンショットを撮るスケジュール
schedule.every(1).minutes.do(take_screenshot)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
