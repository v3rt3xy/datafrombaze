import asyncio
import json

import requests as requests
from google.oauth2 import service_account
from googleapiclient.discovery import build



async def send_message_client(data):
    url = 'https://api.exolve.ru/messaging/v1/SendSMS'
    # для сайта
    response = requests.post(url=url, headers={
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRV05sMENiTXY1SHZSV29CVUpkWjVNQURXSFVDS0NWODRlNGMzbEQtVHA0In0.eyJleHAiOjIwMDk3MjkwNDUsImlhdCI6MTY5NDM2OTA0NSwianRpIjoiYTA2NDg5YjItMjc4YS00MWQwLTg5NzktYzU3ZjNmM2NkZWI2IiwiaXNzIjoiaHR0cHM6Ly9zc28uZXhvbHZlLnJ1L3JlYWxtcy9FeG9sdmUiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYzM5OWY3MmMtOTBmOS00ZTYxLTg1ZjYtMGYxOGUxYjkzYWZkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiMWJkOGJmYzktNmExMi00Yjg0LTljZmUtYmEzNjNiYmQ1MjNlIiwic2Vzc2lvbl9zdGF0ZSI6ImI1MjliYjVhLTJiNzAtNDIzMS1hYTdiLWVhNzg4NzBlYjA0YSIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1leG9sdmUiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJleG9sdmVfYXBwIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJiNTI5YmI1YS0yYjcwLTQyMzEtYWE3Yi1lYTc4ODcwZWIwNGEiLCJ1c2VyX3V1aWQiOiJjOGNjNDgwNC03YmQ5LTQ2NWQtYTVmNC0xMjY1NjA0NGMzMmEiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImNsaWVudEhvc3QiOiIxNzIuMjAuMi4yMiIsImNsaWVudElkIjoiMWJkOGJmYzktNmExMi00Yjg0LTljZmUtYmEzNjNiYmQ1MjNlIiwiYXBpX2tleSI6dHJ1ZSwiYXBpZm9uaWNhX3NpZCI6IjFiZDhiZmM5LTZhMTItNGI4NC05Y2ZlLWJhMzYzYmJkNTIzZSIsImJpbGxpbmdfbnVtYmVyIjoiMTIwNDA3MyIsImFwaWZvbmljYV90b2tlbiI6ImF1dDRkYjc5MDFjLWMxMWYtNDFlYi1iYWE2LTVkNGI2MDA1MDY0YiIsInByZWZlcnJlZF91c2VybmFtZSI6InNlcnZpY2UtYWNjb3VudC0xYmQ4YmZjOS02YTEyLTRiODQtOWNmZS1iYTM2M2JiZDUyM2UiLCJjdXN0b21lcl9pZCI6IjI4ODQ5IiwiY2xpZW50QWRkcmVzcyI6IjE3Mi4yMC4yLjIyIn0.By1UabvoodzGQVwGFuRy3gv1iuf_YTeY4mbj-bP0LA5FhJ-Bp0TVFGUyv_WnOWNVN59SJbkSh3dxV0Ydo62uq7tKaQd3UF5fmfAHCacuGjH9CNARPgU8UeuR5XwHVDtlOYt9F2wGCSG09NO5x-YGaPJdu_qIAn45g_OV8bLdJhof7jXrS6DgDWWzxroo7D7g2UdpPk0xwU9Brj5Y3kUyxfIp9ZwPTTPnr-MGgJJHgQv8mWvsddKYvxW26MSeR4E3pFsU2_8GtaQXbX_g8rXPpb0yjwTfn_qExZlfG6eQXrOlKAFRUc7wMtZhGdJLbaOW7tBrXptCYmUmULaQApq8bw",
    }, json=data)
    print(type(response.json))
    print(response.json)
    print(response)
    return response


class GoogleSheetData:
    def __init__(self):
        # Путь к файлу JSON с учетными данными
        self.SERVICE_ACCOUNT_FILE = 'credentials.json'
        # Создание учетных данных из файла JSON
        self.creds = service_account.Credentials.from_service_account_file(
            self.SERVICE_ACCOUNT_FILE,
            scopes=[
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive',
            ]
        )
        # Создание клиента API
        self.service = build('sheets', 'v4', credentials=self.creds)
        # ID вашей таблицы Google Sheets
        self.spreadsheet_id = '11hZWaRehG1WMVHgJ-zIVi1it6RMKFOOTJHkwnfLrgtE'

    async def processing_google_sheet(self):
        try:
            # открываем файл JSON, читаем данные и записываем их в переменную 'data'
            # если файл не найден, создаем новую пустую переменную 'data'
            try:
                with open('data.json', "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = {1: ['Имя', 'Ваш заказ номер НН готов', 'подойдите туда-то', 'Номер']}
            # получаем номер строки с которым будем работать
            row = int(list(data.keys())[0]) + 1
            # Запрос на получение данных из таблицы Google Sheets(получаем определенную строку в range)
            response = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=f"Лист1!A{row}:E{row}",
            ).execute()
            # получаем строку с данными
            values = response.get('values', [])
            print(values)

            # проверяем на наличие данных
            if not values:
                print('No data found.')
            elif len(values[0]) >= 5 and '' not in values[0]:
                data_excel = {"number": values[0][4], "destination": values[0][0], "text": f"{values[0][1]}, Ваш заказ номер {values[0][2]} готов, подойдите {values[0][3]}"}
                print(data_excel)
                result_send_message = await send_message_client(data_excel)
                data = {row: values[0]}
                print(data)
                # записываем новые данные в файл 'data.json'
                with open('data.json', "w") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"An error occurred: {e}")




async def run_processing_google_sheet(google_sheet_req):
    while True:
        await google_sheet_req.processing_google_sheet()
        await asyncio.sleep(20)






if __name__ == "__main__":
    google_sheet_req = GoogleSheetData()
    asyncio.run(run_processing_google_sheet(google_sheet_req))
