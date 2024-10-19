# Используем базовый образ Python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Обновляем pip
RUN pip install --upgrade pip

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y supervisor

# Устанавливаем зависимости напрямую, без виртуального окружения
RUN pip install -r requirements.txt

# Копируем конфигурацию supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Открываем необходимые порты
EXPOSE 8000

# Запускаем supervisor для управления процессами
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
