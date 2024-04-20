import sqlite3

# Функция для получения отзывов из базы данных
def get_reviews():
    # Подключаемся к базе данных
    conn = sqlite3.connect('reviews.db')
    # Создаем курсор для выполнения запросов
    cursor = conn.cursor()
    # Выполняем запрос для получения всех отзывов
    cursor.execute("SELECT * FROM reviews")
    # Получаем все строки результата
    reviews = cursor.fetchall()
    # Закрываем соединение с базой данных
    conn.close()
    return reviews

# Генерируем HTML-код для отображения отзывов
def generate_reviews_html():
    # Получаем отзывы из базы данных
    reviews = get_reviews()
    # Начинаем формировать HTML-код для блоков отзывов
    html_code = "<div class='review-container'>\n"
    # Проходимся по каждому отзыву
    for review in reviews:
        # Извлекаем данные из отзыва
        author, content = review
        # Формируем HTML-код для отдельного отзыва
        review_html = f"<div class='review'><h3>{author}</h3><p>{content}</p></div>\n"
        # Добавляем HTML-код отзыва к общему HTML-коду
        html_code += review_html
    # Заканчиваем формировать HTML-код для блоков отзывов
    html_code += "</div>"
    return html_code

# Сохраняем сгенерированный HTML-код в файл
with open('reviews.html', 'w') as f:
    f.write(generate_reviews_html())