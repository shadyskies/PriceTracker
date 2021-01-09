import React from "react";
import ReactDom from "react-dom";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";

//components import
import Login from "./components/login";
import Error404 from "./components/404";
import Home from "./components/home";

//styles import
import "./styles/app.scss";

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/home" component={Home} />
        <Route exact path="/" component={Login} />
        <Route component={Error404} />
      </Switch>
    </Router>
  );
}

export default App;
