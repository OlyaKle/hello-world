Тег div - пустой контейнер, своего рода «перенос» содержания на новую строку (вроде разрыва страницы или разрыва строки в текстовых редакторах)
```
<div>Teachable Machine Audio Model</div>
```
Кнопка "Начать" работу с моделью (рисунок 1)
```
<button type="button" onclick="init()">Start</button>
```
Элемент label текстовый компонент, отображающий статический текст либо значение атрибута сущности
```
<div id="label-container"></div> 
```
Если JavaScript-кода много – его выносят в отдельный файл, который подключается в HTML
```
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"></script> //Если JavaScript-кода много – его выносят в отдельный файл, который подключается в HTML
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/speech-commands@0.4.0/dist/speech-commands.min.js"></script>
```
Браузер понимает, что содержимое тега <script> должно быть интерпретировано как код на JavaScript, и выполняет его соответствующим образом
```
<script type="text/javascript"> 
```
Ключевое слово async перед функцией гарантирует, что эта функция в любом случае вернёт промис(как я поняла это, что-то вроде def, а промис это - return <значение>),

В функции: создаём константы - модель топологии, модель метадата
```
const checkpointURL = URL + "model.json"; 
const metadataURL = URL + "metadata.json";
```
Соберём функцию:
```
    async function createModel() { 
        const checkpointURL = URL + "model.json"; 
        const metadataURL = URL + "metadata.json";
```
Функция которая будет распознавать речь с помощью web speech API, в которой

тип преобразования Фурье, для спектрального анализа звуковых данных:
```
"BROWSER_FFT"
```
функция словаря речевых команд, не имеющих пользу для модели:
```
undefined
```
Тогда функция будет выглядеть так
```
        const recognizer = speechCommands.create( 
            "BROWSER_FFT", 
            undefined, 
            checkpointURL,
            metadataURL);
```
        // убедимся, что модель и метаданные загружаются через HTTPS-запросы.
        await recognizer.ensureModelLoaded();

        return recognizer;
    }

    async function init() {
        const recognizer = await createModel(); //await приостанавливает выполнение функции async и ожидает ответа от переданного Promise, затем возобновляя выполнение функции async и возвращая полученное значение
        const classLabels = recognizer.wordLabels(); // получим метки классов
        const labelContainer = document.getElementById("label-container");
        for (let i = 0; i < classLabels.length; i++) { //видимо для каждого созданного контейнера создаём свою метку классов
            labelContainer.appendChild(document.createElement("div"));
        }

        // функция listen() принимает 2 аргумента:
        // 1. Функция обратного вызова, которая вызывается каждый раз, когда распознается слово
        // 2. Объект конфигурации с настраиваемыми полями
	// этой функцией мы можем количественно оценить ошибку модели: чем меньшую вероятность модель назначает верному элементу, тем сильнее ошибка
        recognizer.listen(result => {
            const scores = result.scores; // вероятность предсказания для каждого класса(вместо одного числа модель должна предсказывать распределение вероятностей на множестве)
            // визуализировать оценки вероятности для каждого класса (зависимость между исходными данными и целевыми данными)
            for (let i = 0; i < classLabels.length; i++) {  // Таким образом мы позволим модели "сомневаться" в предсказании
                const classPrediction = classLabels[i] + ": " + result.scores[i].toFixed(2);
                labelContainer.childNodes[i].innerHTML = classPrediction;
            }
        }, {
            includeSpectrogram: true, //  в случае, если прослушивание должно вернуть result.spectrogram
            probabilityThreshold: 0.75, //порог вероятности
            invokeCallbackOnNoiseAndUnknown: true, (1 в listen())
            overlapFactor: 0.50 // вероятно, нужно от 0,5 до 0,75
        });

        // Остановите распознавание за 5 секунд
        // setTimeout(() => recognizer.stopListening(), 5000); ??? не поняла про какую функцию речь
    }
</script>

Рассмотрим библиотеку, которую составила программа:

<div>Teachable Machine Audio Model - p5.js and ml5.js</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.9.0/p5.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.9.0/addons/p5.dom.min.js"></script>
<script src="https://unpkg.com/ml5@latest/dist/ml5.min.js"></script>
<script type="text/javascript">
  // Глобальная переменная для хранения классификатора
let classifier;

// заведём метку
let label = 'listening...';

// Teachable Machine model URL:
let soundModel = 'https://teachablemachine.withgoogle.com/models/C95zKtD-T/';


function preload() {
  // загрузим модель
  classifier = ml5.soundClassifier(soundModel + 'model.json');
}

function setup() {
  createCanvas(320, 240);
  // начнём классификацию
  // звуковая модель будет постоянно слушать микрофон
  classifier.classify(gotResult);
}

function draw() {
  background(0);
  // Нарисуем метку на холсте? далее её параметры
  fill(255);
  textSize(32);
  textAlign(CENTER, CENTER);
  text(label, width / 2, height / 2);
}


// Модель, распознающая звук, вызовет это событие.
function gotResult(error, results) { //обработка при ошибках
  if (error) {
    console.error(error);
    return;
  }
  // Результаты представляют собой упорядоченный массив
  // console.log(results[0]);
  label = results[0].label;
}
</script>

