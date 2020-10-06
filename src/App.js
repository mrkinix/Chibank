import React from 'react';
import Dashboard from './components/dashboard'
import Login from './components/login'
import { BrowserRouter as Router, Route } from 'react-router-dom';

class App extends React.Component {
	render () {
		return (
			<Router>
				<Route exact path="/">
					<Dashboard></Dashboard>
				</Route>
			<Route path="/login">
					<Login></Login>
				</Route>
		  	</Router>
		)
	}
}
  


export default App;

/*
TODO:
	* Add send transactions to available profiles
	* List activity
	* Add mobile support
*/