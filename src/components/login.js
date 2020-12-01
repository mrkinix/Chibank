import React from 'react';
import './login.css';
import API from '../service/service';
import { Redirect } from "react-router-dom";


class Login extends React.Component {
	constructor () {
		super();
	  	this.state = {
            _view: 'menu',
            fname: '',
            lname: '',
            email: '',
            pwd: '',
            rpath: null
        };
        this.createAccount = this.createAccount.bind(this)
        this.login = this.login.bind(this)
    }

    myChangeHandler = (event) => {
        let nam = event.target.name;
        let val = event.target.value;
        this.setState({[nam]: val});
    }

    set_view(p) {
        if (p == 1) this.setState({_view: 'login'})
        else if (p == 2) this.setState({_view: 'signin'})
        else this.setState({_view: 'menu'})
    }

    view() {
        switch(this.state._view) {
            case 'menu': return (
            <div class="btns">
                <div class="btn b1" onClick={() => this.set_view(1)}>Log in</div>
                <div class="btn b2" onClick={() => this.set_view(2)}>Register</div>
            </div>)
            case 'login': return (
                <form onSubmit={this.login} >
                    <label for="email">Email: </label>
                    <input onChange={this.myChangeHandler} type="email" id="fname" name="email"/><br/>
                    <label for="pwd">Password: </label>
                    <input onChange={this.myChangeHandler} type="password" id="lname" name="pwd"/><br/>
                    <input type="submit" id="btn" value="Submit"/>
                    <h4 onClick={() => this.set_view(3)}>Back</h4>
                </form> 
            )
            case 'signin': return(
                <form onSubmit={this.createAccount} >
                    <label for="fname">First name:</label>
                    <input onChange={this.myChangeHandler} type="text" id="fname" name="fname"/><br/>
                    <label for="lname">Last name:</label>
                    <input onChange={this.myChangeHandler} type="text" id="lname" name="lname"/><br/>
                    <label for="email">Email:</label>
                    <input onChange={this.myChangeHandler} type="email" name="email"/><br/>
                    <label for="pwd">Password:</label>
                    <input onChange={this.myChangeHandler} type="password" name="pwd"/><br/>
                    <input type="submit" id="btn" value="Submit"/>
                    <h4 onClick={() => this.set_view(3)}>Back</h4>
                </form> 
            )
        }
    }
    
    txt() {
        switch(this.state._view) {
            case 'login': return 'Login'
            case 'signin': return 'Create an account'
            case 'menu': return 'Please log in to access your dashboard!'
        }
    }

    async login(event) {

        const body = {
            "email": this.state.email,
            "password": this.state.pwd
        }
        event.preventDefault();
        const responce = await API.login(body)
        localStorage.setItem('data', JSON.stringify(responce.data));
        this.setState({rpath: '/'});
    }

    async createAccount(event) {
        const BODY = {
            "first_name": this.state.fname,
            "last_name": this.state.lname,
            "email": this.state.email,
            "password": this.state.pwd,
            "balance": 5000,
            "login": false
        }
        const DATA = {
            first_name: this.state.fname,
            last_name: this.state.lname,
            email: this.state.email,
            balance: 5000,
        }
        event.preventDefault();
        await API.create_user(BODY)
        localStorage.setItem('data', JSON.stringify(DATA));
        this.setState({rpath: '/'});
    }
  
	render () {
        if(this.state.rpath){
            return <Redirect to={this.state.rpath}/>
        }
        return (
			<div className="main-container">
                <h1 style={{fontSize: '50px', margin: 0, padding: 0}}>Chibank</h1>
                <h3 style={{color: 'white'}}>
                    { this.txt() }
                </h3>
                {this.view()}
            </div>
        )
    }
}

export default Login;