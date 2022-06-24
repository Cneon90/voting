## Gender party 
### Система голосования 
:black_square_button:Мальчик    :black_square_button:Девочка 


**Запуск**
`python manage.py runserver`

#### Схема переходов
```mermaid
  flowchart TB
   Main_page --> Success --> Chart
   
```

#### Главная страница
`http://127.0.0.1:8000/`
 
  На данной странице необходимо ввести свое имя и выбрать кандидата

<p align="center">
  <img src="https://github.com/Cneon90/voting/blob/master/Voite/scren/main.png" width="550" title="hover text">
  <img src="https://github.com/Cneon90/voting/blob/master/Voite/scren/main_2.png" width="550" alt="accessibility text">
</p>

#### После голосования
`http://127.0.0.1:8000/succeess`

После голосования вы попадаете на страницу где отображается ваше имя, и есть ссылка для просмотра графика

<p align="center">
  <img src="https://github.com/Cneon90/voting/blob/master/Voite/scren/Finish.png" width="550" title="hover text">
</p>

#### График

`http://127.0.0.1:8000/chart`

Данная страница отправляет ajax запрос в фоне на сервер, ответ изменяет график в реальном времени, по этому нет необходимости в перезагрузке страницы для получения новых данных
<p align="center">
  <img src="https://github.com/Cneon90/voting/blob/master/Voite/scren/chart.png" width="550" title="hover text">
</p>

____

# Администраторская



**Результаты**

`http://127.0.0.1:8000/result`

Тут можно посмотреть кто голосовал так же можно удалить голоса (страница обновляется самостоятельно)

*Для удаления голоса нужно ввести pin 5828* 
<p align="center">
  <img src="https://github.com/Cneon90/voting/blob/master/Voite/scren/Result.png" width="550" title="hover text">
</p>
















