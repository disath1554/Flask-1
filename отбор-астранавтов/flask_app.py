from flask import Flask, request
from flask import url_for

app = Flask(__name__)


@app.route('/')
def f():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    arr = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
           'Присоединяйся!']
    return '</br>'.join(arr)


@app.route('/image_mars')
def show_image():
    return '''
    <head>
        <title>Привет, Марс!</title>
        <h1>Жди нас, Марс!</h1>
        <img src=static/data/mars_planet.png>
        
    </head>
    
    '''


@app.route('/promotion_image')
def promotion_image():
    return f'''
       <head>
           <meta charset="utf-8">
           <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
           <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
           <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}" />
           <title>Колонизация</title>
           <h1>Жди нас, Марс!</h1>
           <img src=static/data/mars_planet.png>
       </head>
       <body>
          <div class="alert alert-primary" role="alert" >
                      Человечество вырастает из детства
                    </div>
         <div class="alert alert-secondary" role="alert" >
                      Илон Маск сосаааааааааат
                    </div>
        <div class="alert alert-warning" role="alert" >
                      Роскосмос лууууууучшееееееее
                    </div>
        <div class="alert alert-danger" role="alert" >
                     Займы без документов 88005555335
                    </div>

       </body>
       '''


@app.route('/bootstrap_sample')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>
                    <div class="alert alert-primary" role="alert">
                      А мы тут компонентами Bootstrap балуемся
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename=
        'css/form_style.css')}" /> 
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анекта претендента</h1>
                            <h2>улететь на Марс</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="password" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <label for="classSelect">  </label>
                                    <input type="password" class="form-control" id="password" placeholder="Введите email" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Нема</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у вас профессии</label>
                                        <div class="form-check">
                                         <input type="checkbox" class="form-check-input" id="profession" name="prof">
                                          <label class="form-check-label" for="Ingeneer">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="profession" name="prof">
                                          <label class="form-check-label" for="Pilot">
                                            Пилот
                                          </label>
                                        </div>
                                         <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="profession" name="prof">
                                          <label class="form-check-label" for="RadioProtect">
                                            Cпециалист по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input"id="profession" name="prof">
                                          <label class="form-check-label" for="else">
                                            Что-то другое 
                                          </label>
                                        </div>
                                    </div>
                                     <label for="classSelect">  </label>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male">
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <label for="classSelect">  </label>
                                    <div class="form-group">
                                        <label for="about">Зачем тебе это, одумойся</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <label for="classSelect">  </label>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="=Volonteer" name="Volonteer">
                                        <label class="form-check-label" for="acceptRules">Готов ли остаться на Марсе?</label>
                                    </div>
                                    <button  type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def planet_choice(planet_name):
    return f'''
       <head>
           <meta charset="utf-8">
           <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
       </head>
       <body>
       <h1>Мое предложение:{planet_name}</h1>
          <div class="alert alert-primary" role="alert" >
                      Эта планета рядом с Землей
                    </div>
         <div class="alert alert-secondary" role="alert" >
                      На ней много ресурсов
                    </div>
        <div class="alert alert-warning" role="alert" >
                      На ней есть магнитное поле
                    </div>
        <div class="alert alert-danger" role="alert" >
                     Ну она красивая тоже, даааа
                    </div>

       </body>
       '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
