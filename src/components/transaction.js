import React from 'react';
import './transaction.css'
import API from '../service/service'

class Transaction extends React.Component {
	constructor () {
		super();
	  	this.state = {
			receiver: '',
			results: [],
			selected: null,
			amount: 0
		};
		this.switch_view = this.switch_view.bind(this)
		this.get_users = this.get_users.bind(this) 
		this.handleChange = this.handleChange.bind(this) 
		this.make_transaction = this.make_transaction.bind(this) 
	}

	search_result () {
		return (
			this.state.results.map((value, index) => {
				return (
					<div key={index}
					class={value.email === this.state.selected ? 
						"selected-res" : "res-container" }
					onClick={() => this.select_user(value.email, value.first_name + ' ' + value.last_name)}>
						{value.first_name + ' ' + value.last_name}
					</div>
				)
			})
		)
	}

	select_user(email, name) {
		this.setState({
			selected: email,
			receiver: name
		})
	}

	async make_transaction(event) {
		let login_info = JSON.parse(localStorage.getItem('data'))
        event.preventDefault();
		const DATA = {
			email: login_info.email,
			amount: Math.abs(parseInt(this.state.amount)),
			destination: this.state.selected,
			receiver: this.state.receiver,
			sender: login_info.first_name + ' ' + login_info.last_name
		}
		const RESPONCE = await API.user_transaction(DATA)
		login_info.balance = RESPONCE.data.balance
        localStorage.setItem('data', JSON.stringify(login_info));
		window.location.reload()
	}

	switch_view() {
		this.props.onClose()
	}

	async get_users() {
		const RESPONCE = await API.get_users()
		let res = []
		for (let item of RESPONCE.data) {
			if (item.first_name.concat(' ' + item.last_name).includes(this.state.receiver)) {
				res.push(item)
			}
		}
		this.setState({results: []})
		this.setState({results: res})
	}

	handleChange(event) {
        let nam = event.target.name;
		let val = event.target.value;
        this.setState({[nam]: val});
	}
  
	render () {
        return (
			<div>
				<div class="close" onClick={this.switch_view}/>
            	<form class="transaction-container"  onSubmit={this.make_transaction}>
					<label for="receiver">To: </label>
					<input id="pl" placeholder="Search" name="receiver" 
					value={this.state.receiver} onChange={(e) => 
					{this.handleChange(e);this.get_users(e)}} />
					<div class="search-result">
						{this.search_result()}
					</div>
					<label for="amount">Amount: </label>
					<input type="number" id="pl" placeholder="amount" name="amount"
					value={this.state.amount} onChange={this.handleChange}/><br/>
					<input type="submit" id="btn-transaction" value="Submit"/>
            	</form>
            </div>
        )
    }
}

export default Transaction;