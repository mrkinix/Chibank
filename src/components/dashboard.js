import React from 'react';
import '../App.css';
import API from '../service/service';
import { Redirect } from "react-router-dom";
import Transaction from './transaction';

class Dashboard extends React.Component {
	constructor () {
		super();
	  	this.state = {
			balance: 0,
			email: '',
			name: '',
            rpath: null,
			transactions: [],
			transaction: false
		};
		this.log_out = this.log_out.bind(this)
		this.switch_transaction = this.switch_transaction.bind(this)
		this.render_activity = this.render_activity.bind(this)
	}

  
	async componentDidMount () {
		let login_info = JSON.parse(localStorage.getItem('data'))
		login_info.login = true
		const RESPONCE = await API.create_user(login_info)
		if (RESPONCE) {
			this.setState({
				balance: RESPONCE.data[0].balance,
				email: RESPONCE.data[0].email,
				name: RESPONCE.data[0].last_name,
				transactions: RESPONCE.data[0].transactions.reverse( )
			})
		}
	}

	log_out () {
		localStorage.clear()
        this.setState({rpath: '/login'});
	}

	switch_transaction() {
		if (this.state.transaction) this.setState({transaction: false}) 
		else this.setState({transaction: true})
	}
  
	render_transaction() {
		if (this.state.transaction) return <Transaction
		onClose={this.switch_transaction}></Transaction>
	}

	render_activity () {
		return (
			this.state.transactions.map((value, index) => {
				return (
					<div key={index}
					class="res-container1">
						{value}
					</div>
				)
			})
		)
	}

	render () {
		if(this.state.rpath){
            return <Redirect to={this.state.rpath}/>
        }
		return (
			<div className="main-container" style={{display: 'block'}}>    
				{this.render_transaction()}
 				<div className="top-bar">
					<h1>Chibank</h1>
					<div style={{marginRight: '2.5%', display: 'flex'}}>
						<h4 style={{lineHeight: '5rem'}} onClick={this.log_out}>logout</h4>
						<h2 id="name">{this.state.name}</h2>
						<div class="img"></div>
					</div>
				 </div>
				<div className="line">
					<div className="balance">
						<h2>Wallet Balance:</h2>
						<h1>{this.state.balance + ' €'}</h1>
					</div>
					<div className="welcome">
						<h2 style={{paddingLeft: '2.5%'}}>Hey {this.state.name}!</h2>
						<div className="mt" onClick={this.switch_transaction}>Make transaction</div>
					</div>
				</div>
				<div className="activity">
					<h2 style={{paddingLeft: '2.5%', paddingTop: '12px'}}>Activity:</h2>
					{this.render_activity()}
				</div>
			</div>
		)
	}
}
  


export default Dashboard;
