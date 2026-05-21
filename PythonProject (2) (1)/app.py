from flask import Flask, render_template, abort

app = Flask(__name__)

ELEMENTS = {

    "axel": {
        "name": "Аксель",
        "category": "Прыжки",
        "description": "Аксель — единственный прыжок, исполняющийся с движения вперёд, поэтому в нём не целое число оборотов. Назван в честь норвежского фигуриста и конькобежца Акселя Паульсена. Он впервые исполнил этот прыжок в 1882 году на международном турнире в Вене. Самый сложный из шести стандартных прыжков.",
        "photo": "/static/images/i.webp",
        "video_url": "https://yandex.ru/video/preview/2104274747333688162"
    },
    "salchow": {
        "name": "Сальхов",
        "category": "Прыжки",
        "description": "Сальхов — рёберный прыжок с заходом с левой ноги назад-внутрь. Назван в честь шведского фигуриста Ульриха Сальхова. Он впервые продемонстрировал этот прыжок в 1909 году. Относится к числу базовых прыжков.",
        "photo": "/static/images/1ebc458822609f6078fda13a2aad5314.jpg",
        "video_url": "https://ya.ru/video/preview/18131252718479167249"
    },
    "toeloop": {
        "name": "Тулуп",
        "category": "Прыжки",
        "description": "Тулуп — зубцовый прыжок, выполняемый с правой ноги назад-наружу с толчком зубцом левой ноги. Название произошло от английского toe loop — «петля на носке». Американский фигурист Брюс Мейпс впервые исполнил этот прыжок в 1920 году. Часто используется в каскадах",
        "photo": "/static/images/a762b8919ac892fa884e1da968425270.jpg",
        "video_url": "https://yandex.ru/video/preview/14077377470388599545"
    },
    "loop": {
        "name": "Риттбергер",
        "category": "Прыжки",
        "description": "Риттбергер — рёберный прыжок, выполняемый с правой ноги назад-наружу. Назван в честь Вернера Риттбергера. Он впервые исполнил этот прыжок в 1910 году.",
        "photo": "/static/images/500x150@3.webp",
        "video_url": "https://yandex.ru/video/preview/6062819783786820473"
    },
    "flip": {
        "name": "Флип",
        "category": "Прыжки",
        "description": "Флип — зубцовый прыжок с левой ноги назад-внутрь, толчок зубцом правой ноги. Назван не в честь конкретного человека, а от английского слова flip, что означает «щелчок». Впервые данный прыжок был исполнен канадским фигуристом Монтгомери (Бад) Уилсоном в 1930-х годах. Требует хорошего контроля рёбер.",
        "photo": "/static/images/pk.webp",
        "video_url": "https://yandex.ru/video/preview/5299970212422068511"
    },
    "lutz": {
        "name": "Лутц",
        "category": "Прыжки",
        "description": "Лутц — зубцовый прыжок с левой ноги назад-наружу, толчок зубцом правой ноги. Назван в честь австрийского фигуриста Алоиза Лутца. Он впервые исполнил этот прыжок в 1913 году. Самый сложный из зубцовых прыжков из-за противонаправленности рёбер.",
        "photo": "/static/images/grafika-6-lutz-upr.jpg",
        "video_url": "https://yandex.ru/video/preview/1646487963866611849"
    },

    "upright_spin": {
        "name": "Винт",
        "category": "Вращения стоя",
        "description": "Классическое вращение стоя на одной ноге с вертикальным положением корпуса. Свободная нога скрещена спереди или отведена в сторону. Основа для большинства усложнённых позиций.",
        "photo": "/static/images/Karel_Zelenka_Spin_-_2007_Europeans.jpg",
        "video_url": "https://yandex.ru/video/preview/11307230437380546362"
    },
    "layback_spin": {
        "name": "Заклон",
        "category": "Вращения стоя",
        "description": "Эффектное вращение с прогибом корпуса назад и свободной ногой, поднятой назад. Требует гибкости спины и устойчивости. Часто используется в женском одиночном катании.",
        "photo": "/static/images/2012_WFSC_07d_843_Polina_Korobeynikova.JPG",
        "video_url": "https://yandex.ru/video/preview/8928063760330042019"
    },

    "sit_spin": {
        "name": "Волчок",
        "category": "Вращения сидя",
        "description": "Базовое вращение в положении сидя (пистолетик). Опорная нога согнута, свободная вытянута вперёд параллельно льду. Ценится скорость вращения и глубина посадки.",
        "photo": "/static/images/fizkulturnaiaazbukakuchiebnikufizichieskaiakulturaviliakh14klass_78.jpeg",
        "video_url": "https://yandex.ru/video/preview/5413402096523255622"
    },
    "cannonball": {
        "name": "Складка",
        "category": "Вращения сидя",
        "description": "Вращение сидя, в котором свободная нога согнута и прижата к опорной, а корпус наклонён вперёд. Напоминает позу «пушечное ядро». Развивает чувство баланса.",
        "photo": "/static/images/gbryf.webp",
        "video_url": "https://yandex.ru/video/preview/12331979055549603442"
    },
    "side_sit_spin": {
        "name": "Боковой волчок",
        "category": "Вращения сидя",
        "description": "Вращение сидя с корпусом, наклонённым вбок, и свободной ногой, вытянутой в сторону параллельно льду. Очень красивое и сложное вращение, демонстрирующее контроль рёбер.",
        "photo": "/static/images/5faa894802e8bd0ed91cdefa.jpg",
        "video_url": "https://yandex.ru/video/preview/17139901861882164085"
    },

    "camel_spin": {
        "name": "Либела",
        "category": "Вращения стоя",
        "description": "Вращение в ласточке: корпус параллелен льду, свободная нога вытянута назад и находится на уровне бедра или выше. Классическая позиция для комбинированных вращений.",
        "photo": "/static/images/504d81845eeaa424a1f7489376d8419e.jpg",
        "video_url": "https://yandex.ru/video/preview/10684421574819347759"
    },
    "rooster_spin": {
        "name": "Петушок",
        "category": "Вращения стоя",
        "description": "Вращение стоя с захватом свободной ноги сзади. Корпус остаётся вертикальным. Создаёт эффектную, напряжённую позу.",
        "photo": "/static/images/7d83b259cfd23a1f4837a04c32b301fa.jpg",
        "video_url": "https://yandex.ru/video/preview/2580462624733941376"
    },
    "ring_spin": {
        "name": "Кольцо",
        "category": "Вращения стоя",
        "description": "Вращение в положении «бильманн»: свободная нога поднята над головой, захват за лезвие конька двумя руками. Требует исключительной гибкости позвоночника и плечевых суставов.",
        "photo": "/static/images/scale_1200.jpg",
        "video_url": "https://yandex.ru/video/preview/2003973888183082490"
    },

    "step_sequence": {
        "name": "Дорожка шагов",
        "category": "Дорожки",
        "description": "Последовательность разнообразных шагов, поворотов и смен направления, выполняемых под музыку. Оценивается сложность, глубина рёбер и музыкальность.",
        "photo": "/static/images/1180x665.jpg",
        "video_url": "https://yandex.ru/video/preview/16893266988533333120?from_type=vast&parent-reqid=1776279664757124-5163681845100946855-balancer-l7leveler-kubr-yp-sas-221-BAL&text"
    },
    "spiral": {
        "name": "Спираль",
        "category": "Дорожки",
        "description": "Длительное скольжение на одной ноге с поднятой свободной ногой выше уровня бедра. Классический элемент, требующий гибкости и устойчивости.",
        "photo": "/static/images/Miki_Ando_(271085208).jpg",
        "video_url": "https://yandex.ru/video/preview/4451168810570160463?from_type=vast&parent-reqid=1776279734135032-4760602469305940961-balancer-l7leveler-kubr-yp-sas-221-BAL&reqid=1776279664757124-5163681845100946855-balancer-l7leveler-kubr-yp-sas-221-BAL&suggest_reqid=397619272171653268896670635941535&text"
    }
}

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/element/<element_id>')
def show_element(element_id):

    element = ELEMENTS.get(element_id)
    if not element:
        abort(404)

    similar_elements = []
    for key, value in ELEMENTS.items():
        if value['category'] == element['category'] and key != element_id:
            similar_elements.append({
                'id': key,
                'name': value['name']
            })

    return render_template('element.html', element=element, similar_elements=similar_elements)

if __name__ == '__main__':
    app.run(debug=True)