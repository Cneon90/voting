function delete_post(id) {
    let isBoss = confirm("Удалить голос id="+id+"?");

    if (isBoss == true) {
        let pass = prompt("Пароль:","");
            if (pass == 5828) {
                
                    const request = new XMLHttpRequest();
                const url = "/delete/" + id;
                request.open('GET', url);
                request.setRequestHeader('Content-Type', 'application/x-www-form-url');
                request.addEventListener("readystatechange", () => {
                    if (request.readyState === 4 && request.status === 200) {

                        // выводим в консоль то что ответил сервер
                        console.log(request.responseText);
                    }
                });
                // Выполняем запрос
                request.send();
                location.reload();
            }
    }




}