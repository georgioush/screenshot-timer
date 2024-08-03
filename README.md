# スクリーンショットツール

このプロジェクトは、1分ごとにスクリーンショットを撮影し、実行ファイルのあるディレクトリに保存するPythonスクリプトです。

## 必要条件

- Python 3.x
- `pyautogui`
- `schedule`
- `pywin32`
- `pyinstaller`

## セットアップ

1. **リポジトリをクローンします:**

    ```sh
    git clone https://github.com/georgioush/screenshot-taker.git
    cd screenshot-taker
    ```

1-1. **仮想環境を生成します**

    ```sh
    python -m venv venv
    source venv\Scripts\activate
    ```

1. **必要なPythonパッケージをインストールします:**

    ```sh
    pip install -r requirements.txt
    ```

2. **スクリプトを実行可能ファイルに変換します:**

    ```sh
    pip install pyinstaller
    pyinstaller --onefile --noconsole screenshot.py
    ```

## 使い方

1. `pyinstaller`コマンドを実行すると、`dist`ディレクトリに実行可能ファイルが生成されます。

2. 実行可能ファイル（`screenshot.exe`）を任意の場所に移動します。

3. 実行ファイルをダブルクリックして実行します。1分ごとにスクリーンショットを撮影し、実行ファイルと同じディレクトリにある`screenshots`フォルダに保存されます。

