import Api from './Api';

export default {
    login(params) {
        console.log(params)
        return Api().post('/api/user_connection', params);
    },
    get_users(params) {
        return Api().get('/api/user', params);
    },
    create_user(params) {
        return Api().post('/api/user', params)
    },
    user_transaction(params) {
        return Api().post('/api/user_transaction', params)
    }
};
