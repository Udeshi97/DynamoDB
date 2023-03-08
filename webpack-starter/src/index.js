import generateJoke from "./generateJoke"
import './styles/main.scss'
import laughing from './assets/laughing.svg'
import getData from "./get"
import invokeLambda from "./post"

const laughImg = document.getElementById('laughImg')
laughImg.src = laughing

const jokeBtn = document.getElementById('jokeBtn')
jokeBtn.addEventListener('click', function() {
    generateJoke();
    getData();
    invokeLambda();
});

generateJoke()
