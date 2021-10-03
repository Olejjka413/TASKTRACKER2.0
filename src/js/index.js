import axios from "axios";
const url = 'http://task-tracker.std-1677.ist.mospolytech.ru';

const api = axios.create({
  baseURL: url,
  timeout: 5000,
  withCredentials: false,
})

const onSuccess = (response) => response;
const onFail = (error) => {
  const {response} = error
  throw error;
}

const fetchUser = () => {
  api.get('/user')
  .then(({data})=>{
    console.log(data);
  })
}

// const login = (login="olga01", password="12345") => {
//   const userData = {
//     "login":login,"password":password
//   };
//   api.post('/user/login/', JSON.stringify(userData))
//   .then((response) => {
//     console.log(response)
//   })
//   .catch((error)=>{
//     console.log(error)
//   })
// }


function login(id =5,login ="olga01", password="12345") {
  const request = axios({
      headers: {
          'content-type': 'application/json'
      },
      method: 'post',
      url: "http://task-tracker.std-1677.ist.mospolytech.ru/user/login/",
      params: {
          "id":id,
          "login":login,
          "password":password
      }
  })
  .then((response) => console.log(response.data))
  .catch((error) => console.log(error));

}

login()

