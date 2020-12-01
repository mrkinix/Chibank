
import axios from 'axios';

const environment = process.env.NODE_ENV; // development


export default () => axios.create({ baseURL: 'http://localhost:8080/' });
