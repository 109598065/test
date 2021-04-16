# wagtail
## Docker 指令
```bash
docker build -t wagtail .
docker run -dp 3000:8000 wagtail
```
## 帳密
- 帳號 : test
- 密碼 : test
## 網址
- http://localhost:3000/
    - 點擊右下的 Admin Interface 進入 Wagtail 使用頁面
- http://localhost:3000/coverage-app
    - Coverage report 頁面
    - 很慢
- http://localhost:3000/coverage-app/object
    - Coverage JSON 格式頁面
    - 很慢
- http://localhost:3000/coverage-app/reset
    - Coverage 重置頁面
## 目前修改檔案
- wagtail_test/wsgi.py
- coverage_app/url.py
- coverage_app/views.py
- coverage_app/coverage_data/.coveragerc
