export const initLoginForm = () => {
  const formLogin = document.querySelector('.login__form')
  const inputLogin = formLogin.querySelector('.login__input--login');
  const inputPassword = formLogin.querySelector('.login__input--password');

  const onFormLoginSubmit = (evt) => {
    evt.preventDefault();
    const loginValue = inputLogin.value;
    const loginPassword = inputPassword.value;
    login(loginValue,loginPassword);
  }
  formLogin.addEventListener('submit', onFormLoginSubmit);
}

