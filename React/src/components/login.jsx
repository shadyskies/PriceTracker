import React from "react";
import logo from "../assets/images/default-monochrome-white.svg";

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: "" };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  handleSubmit(event) {
    alert("A name was submitted: " + this.state.value);
    event.preventDefault();
  }

  //elements

  render() {
    return (
      <div className="page">
        <div class="main-box">
          {/* <h2 class="name">Movie Recommender</h2> */}
          <div className="logo-box">
            <img className="logo" src={logo}></img>
          </div>

          <form action="" class="form-box" onSubmit={this.handleSubmit}>
            <div className="log-reg">
              <h3>Login</h3>
              <h3>Register</h3>
            </div>
            <h4>Login to access your account</h4>
            <div className="form-labels">
              <label>
                <input
                  type="text"
                  value={this.state.value}
                  onChange={this.handleChange}
                  name="name"
                  placeholder="Username"
                />
              </label>
              <label>
                <input type="text" name="password" placeholder="Password" />
              </label>
            </div>

            <input type="submit" value="Submit" />
            <div id="login">
              <a class="pass-reset" href="">
                Forgot Password
              </a>
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default Login;
