import uuid
import requests
import random
import string
import time


API_URL = 'http://127.0.0.1:8000/api/textid/'


def generate_random_string(length=16):
    """Генерирует случайную строку заданной длины."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def insert_records(api_url, num_records):
    """Добавляет случайное количество записей в базу данных через API."""
    records = [{"uuid": str(uuid.uuid4()), "text": generate_random_string()} for _ in range(num_records)]
    response = requests.post(api_url + 'new/', json=records)
    if response.status_code == 201:
        print(f"Добавлено {num_records} записей.")
    else:
        print(f"Ошибка при добавлении записей: {response.status_code}")


def retrieve_and_delete_records(api_url, num_records):
    """Запрашивает и удаляет указанное количество записей через API."""
    response = requests.get(api_url + f'count_offset/{num_records}/0/')
    if response.status_code == 200:
        records = response.json()
        for record in records:
            uuid = record.get("uuid")
            response = requests.delete(api_url + f'{uuid}/')
            if response.status_code == 204:
                print(f"Удалена запись с UUID {uuid}.")
            else:
                print(f"Ошибка при удалении записи с UUID {uuid}: {response.status_code}")
    else:
        print(f"Ошибка при запросе записей: {response.status_code}")


if __name__ == "__main__":
    while True:
        # Генерация случайного числа записей от 10 до 100
        num_records_to_insert = random.randint(10, 100)
        insert_records(API_URL, num_records_to_insert)

        # Запрос и удаление 10 записей
        retrieve_and_delete_records(API_URL, 10)

        print("\n--- Статистика ---")
        print(f"Время: {time.strftime('%H:%M:%S')}")
        time.sleep(10)  # Пауза 10 секунд перед следующей итерацией
