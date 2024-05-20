import axios from 'axios';
import Cookies from 'js-cookie'
axios.defaults.xsrfCookieName='csrftoken'
axios.defaults.xsrfHeaderName='X_CSRFTOKEN'
axios.defaults.withCredentials = true
const api = axios.create({
  baseURL: 'https://dagudusai.pythonanywhere.com/', // Change this to your API base URL
  headers: {
    'Content-Type': 'application/json',
    // Function to get CSRF token from cookies
    'X-CSRFToken': Cookies.get('csrftoken')
}
});

export default api;
