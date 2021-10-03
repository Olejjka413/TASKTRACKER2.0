import axios from "axios";

export const initApi
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
