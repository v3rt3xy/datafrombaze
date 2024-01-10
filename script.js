async function postData(formProps) {
  const url = 'https://api.exolve.ru/messaging/v1/SendSMS';
  const data = { number: number, destination: destination, text: text };

  try {
    console.log(JSON.stringify(data));
    const response = await fetch(url, {
      method: "POST",
      body: JSON.stringify(formProps),
      headers: {
        "Authorization": "Код авторизации",
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
