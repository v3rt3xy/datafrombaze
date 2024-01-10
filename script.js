async function postData(formProps) {
  const url = 'https://api.exolve.ru/messaging/v1/SendSMS';
  const data = { number: number, destination: destination, text: text };

  try {
    console.log(JSON.stringify(data));
    const response = await fetch(url, {
      method: "POST",
      body: JSON.stringify(formProps),
      headers: {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRV05sMENiTXY1SHZSV29CVUpkWjVNQURXSFVDS0NWODRlNGMzbEQtVHA0In0.eyJleHAiOjIwMDk3MjkwNDUsImlhdCI6MTY5NDM2OTA0NSwianRpIjoiYTA2NDg5YjItMjc4YS00MWQwLTg5NzktYzU3ZjNmM2NkZWI2IiwiaXNzIjoiaHR0cHM6Ly9zc28uZXhvbHZlLnJ1L3JlYWxtcy9FeG9sdmUiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYzM5OWY3MmMtOTBmOS00ZTYxLTg1ZjYtMGYxOGUxYjkzYWZkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiMWJkOGJmYzktNmExMi00Yjg0LTljZmUtYmEzNjNiYmQ1MjNlIiwic2Vzc2lvbl9zdGF0ZSI6ImI1MjliYjVhLTJiNzAtNDIzMS1hYTdiLWVhNzg4NzBlYjA0YSIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1leG9sdmUiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJleG9sdmVfYXBwIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJiNTI5YmI1YS0yYjcwLTQyMzEtYWE3Yi1lYTc4ODcwZWIwNGEiLCJ1c2VyX3V1aWQiOiJjOGNjNDgwNC03YmQ5LTQ2NWQtYTVmNC0xMjY1NjA0NGMzMmEiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImNsaWVudEhvc3QiOiIxNzIuMjAuMi4yMiIsImNsaWVudElkIjoiMWJkOGJmYzktNmExMi00Yjg0LTljZmUtYmEzNjNiYmQ1MjNlIiwiYXBpX2tleSI6dHJ1ZSwiYXBpZm9uaWNhX3NpZCI6IjFiZDhiZmM5LTZhMTItNGI4NC05Y2ZlLWJhMzYzYmJkNTIzZSIsImJpbGxpbmdfbnVtYmVyIjoiMTIwNDA3MyIsImFwaWZvbmljYV90b2tlbiI6ImF1dDRkYjc5MDFjLWMxMWYtNDFlYi1iYWE2LTVkNGI2MDA1MDY0YiIsInByZWZlcnJlZF91c2VybmFtZSI6InNlcnZpY2UtYWNjb3VudC0xYmQ4YmZjOS02YTEyLTRiODQtOWNmZS1iYTM2M2JiZDUyM2UiLCJjdXN0b21lcl9pZCI6IjI4ODQ5IiwiY2xpZW50QWRkcmVzcyI6IjE3Mi4yMC4yLjIyIn0.By1UabvoodzGQVwGFuRy3gv1iuf_YTeY4mbj-bP0LA5FhJ-Bp0TVFGUyv_WnOWNVN59SJbkSh3dxV0Ydo62uq7tKaQd3UF5fmfAHCacuGjH9CNARPgU8UeuR5XwHVDtlOYt9F2wGCSG09NO5x-YGaPJdu_qIAn45g_OV8bLdJhof7jXrS6DgDWWzxroo7D7g2UdpPk0xwU9Brj5Y3kUyxfIp9ZwPTTPnr-MGgJJHgQv8mWvsddKYvxW26MSeR4E3pFsU2_8GtaQXbX_g8rXPpb0yjwTfn_qExZlfG6eQXrOlKAFRUc7wMtZhGdJLbaOW7tBrXptCYmUmULaQApq8bw",
      },
    });
    const json = await response.json();
    console.log("Успех:", JSON.stringify(json));
  } catch (error) {
    console.error("Ошибка:", error);
  }
}


function logSubmit(event) {
  event.preventDefault();
  const formData = new FormData(event.target);
  const formProps = Object.fromEntries(formData);

  postData(formProps);
}

const form = document.getElementById("form");
form.addEventListener("submit", logSubmit);