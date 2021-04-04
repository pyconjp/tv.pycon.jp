"""
YouTubeのもくじに書いたところを読み込んで、reStructuredTextの箇条書きにする

目次ファイルの形式
----
https://www.youtube.com/watch?v=FSdri26yNdo ←1行目にYouTubeのURL
0:00:00 開始 ←2行目以降に「時間」と「タイトル」
0:00:25 PyCon JP TV 配信開始
0:01:23 メッセージ募集(PyCon JP 2014-2016の思い出)
0:03:27 PyCon JP TVステッカーのお披露目
"""

import sys


def generate_timeline(url: str, time_str: str, title: str) -> str:
    """reSTの箇条書きの1行分を生成して返す"""
    # 時間を秒にする
    hour, min, sec = time_str.split(":")
    seconds = int(hour) * 3600 + int(min) * 60 + int(sec)
    s = f"* `{time_str} <{url}&t={seconds}s>`_ {title}"
    return s


def main(filename: str) -> None:
    """ファイルからタイムテーブル情報を読み込んでreST形式を出力する"""
    with open(filename) as f:
        url = f.readline().strip()
        for line in f:
            time_str, title = line.strip().split(maxsplit=1)
            print(generate_timeline(url, time_str, title))


if __name__ == "__main__":
    # Usage: python3 timetable2rest.py timetable.txt
    main(sys.argv[1])
