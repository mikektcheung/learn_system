console.log('Quiz Start')
const url = window.location.href

const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')

// Timer
const activateTimer = (time) => {
    if (time.toString().length < 2) {
        timerBox.innerHTML = `<b>0${time}:00</b>`
    } else {
        timerBox.innerHTML = `<b>${time}:00</b>`
    }

    let minutes = time - 1
    let seconds = 60
    let displaySeconds
    let displayMinutes

    const timer = setInterval(()=>{
        seconds --
        if (seconds < 0) {
            seconds = 59
            minutes --
        }
        if (minutes.toString().length < 2) {
            displayMinutes = '0'+minutes
        } else {
            displayMinutes = minutes
        }
        if(seconds.toString().length < 2) {
            displaySeconds = '0' + seconds
        } else {
            displaySeconds = seconds
        }
        if (minutes === 0 && seconds === 0) {
            timerBox.innerHTML = "<b>00:00</b>"
            setTimeout(()=>{
                clearInterval(timer)
                alert('Time over')
                sendData()
            }, 500)
        }

        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
    }, 1000)
}

//AJAX to display the questions basing on the JSON response
$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        const data = response.data
        data.forEach(el => {
            id = el.id
            question = el.question
            console.log(question)
            quizBox.innerHTML += `
                <div class="col-md-12">
                    <hr>
                    <h4><b>Q: ${question}</b></h4>
                </div>
            `
            const answers = el.answers
            answers.forEach(answer=>{
                quizBox.innerHTML += `
                    <div class="col-md-12">
                        <input type="radio" class="ans" id="${id}" name="${id}" value="${answer}" style="height:18px; width:18px;">
                        <label for="${question}" style="font-size:24px"> ${answer}</label>
                    </div>
                `
            })
        });
        activateTimer(response.time)
        
    },
    error: function(error){
        console.log(error)
    }
})

//Get the post data and submit to the view
const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


const sendData = () => { 
    //extra the data
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })
    
    //display the current answer
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        
        success: function(response){

            const url = response.url
            
            /*
            quizForm.classList.add('not-visible')

            scoreBox.innerHTML = `${response.passed ? 'Congratulations! ' : 'Ups..:( '}Your result is ${response.score.toFixed(2)}%`

            results.forEach(res=>{
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)){

                    resDiv.innerHTML += question
                    const cls = ['container', 'p-3', 'text-light', 'h6']
                    resDiv.classList.add(...cls)

                    if (resp=='not answered') {
                        resDiv.innerHTML += '- not answered'
                        resDiv.classList.add('bg-danger')
                    }
                    else {
                        const answer = resp['answered']
                        const correct = resp['correct_answer']

                        if (answer == correct) {
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += ` answered: ${answer}`
                        } else {
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += ` | correct answer: ${correct}`
                            resDiv.innerHTML += ` | answered: ${answer}`
                        }
                    }
                }
                resultBox.append(resDiv)   
            }
            */
            window.location.replace(url)
        },
        
        error: function(error){
            console.log(error)
        }
    })
    

}

quizForm.addEventListener('submit', e=>{
    e.preventDefault()

    sendData()
})