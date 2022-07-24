**Добавление разрешенных адресов в файл для сервера nginx**

Требует отдельного файла со списком адресов в формате:

*allow 192.168.0.0/24;*

*deny all;*

Путь к файлу с разрешенными адресами указывается в *settings.py*

**Настройка авторизации**

Требует настройки nginx на просмотр внутренних адресов (на серый IP)

*apt install apache2-utils*

*htpasswd -c /etc/nginx/.htpasswd user1*

*server {\
    ...
    auth_basic "Restricted Area";\
    auth_basic_user_file /etc/nginx/.htpasswd;\
    ...
}*

**Настройка сервисов**

- Установить: python3-venv
- Создать venv в текущей директории: *python -m venv venv*
- Установить gunicorn: *pip install gunicorn*
- Установить Flask: *pip install flask*

- Модифицировать и подложить: gunicorn/allowip.service
в /etc/systemd/system

- Модифицировать и подложить: nginx/allowip
в /etc/nginx/sites-available и не забыть сделать симлинк

