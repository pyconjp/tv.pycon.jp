# tv.pycon.jp

PyCon JP TV Webサイト

* GitHub: https://github.com/pyconjp/tv.pycon.jp
* URL: https://tv.pycon.jp/

## Links

* YouTube: [PyCon JPチャンネル](https://www.youtube.com/user/PyConJP)
* Twitter: [@pyconjptv](https://twitter.com/pyconjptv)
* Disord: [Python.jp Discord](https://www.python.jp/pages/pythonjp_discord.html)の `#pyconjp-tv` チャンネル
* Googleフォーム: [PyCon JP TVお便りコーナー](https://docs.google.com/forms/d/e/1FAIpQLSfvL4cKteAaG_czTXjofR83owyjXekG9GNDGC6-jRZCb_2HRw/viewform)

## build

```bash
$ git clone https://github.com/pyconjp/tv.pycon.jp.git
$ cd www.pycon.jp
$ python3.11 -m venv env
$ . env/bin/activate
(env)$ pip install -r requirements.txt
(env)$ make html
(env)$ open build/html/index.html
```
