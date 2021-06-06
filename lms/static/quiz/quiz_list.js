console.log('Start Quiz Y/N')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
        <div class="h5 mb-3">"<b>${name}</b>"：現在開始練習嗎？</div>
        <div class="text-primary">
            <ul>
                <li>難度: <b>${difficulty}</b></li>
                <li>題目數量: <b>${numQuestions}</b></li>
                <li>合格數量: <b>${scoreToPass}%</b></li>
                <li>時間: <b>${time} 分鐘</b></li>
            </ul>
        </div>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))