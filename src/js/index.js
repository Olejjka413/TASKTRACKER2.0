import axios from "axios";

const INPUT_ERROR_CLASS = "login__input--error";
const formLogin = document.querySelector('.login__form')
const inputLogin = formLogin.querySelector('.login__input--login');
const inputPassword = formLogin.querySelector('.login__input--password');
const repeatPassword = formLogin.querySelector('.login__input--password-repeat')

const ApiInformation = {
    BASE_URL: "http://task-tracker.std-1677.ist.mospolytech.ru",
    TIMEOUT: 5000
  };

  const createAPI = () => {
    const api = axios.create({
      baseURL: ApiInformation.BASE_URL,
      timeout: ApiInformation.TIMEOUT
    });

    const onSuccess = (response) => response;

    const onFail = (err) => {
      const {response} = err;
      throw err;
    };

    api.interceptors.response.use(onSuccess, onFail);

    return api;
  };

  const api = createAPI();


  const login = (login, password) => {
    console.log(login, password)
    api.post('/user/login/', {login, password})
    .then((response) => console.log(response))
    .catch((err) => console.log(err));
  };
  const onFormSubmit = (evt) => {
    evt.preventDefault();

    if (repeatPassword){
      const loginValue = inputLogin.value;
      const passwordValue = inputPassword.value;
      const repeatPasswordValue = repeatPassword.value;

      if (passwordValue === repeatPasswordValue){
        console.log('Пароли совпадают')
      } else {
        console.log('Пароли не совпадают');
        const input = formLogin.querySelectorAll('input');
        input.forEach((element) => {
          element.classList.add(INPUT_ERROR_CLASS)
        })
      }

    } else {
      const loginValue = inputLogin.value;
      const passwordValue = inputPassword.value;
      login(loginValue, passwordValue);
    }
  }
  formLogin.addEventListener('submit', onFormSubmit);




