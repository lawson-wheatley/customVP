import React from "react";
export default function Login({ setToken }) {

    function convert(){
        document.getElementById("login").className = "loginclicked"
    }
    function register(){
        document.getElementById("confemail").style.display = "block";
        document.getElementById("confpassword").style.display = "block";
        document.getElementById("login").style.height = "600px";
        document.getElementById("register").style.display = "none";
        document.getElementById("body").classList.add("bodyb");
    }

    return (<div>
        <div className="center-container vertical">
        <div className="center-container horizontal">
      <div id="login" className="login" onClick={e => convert()}>
            <div className="word">
                Login
            </div>
            <div className="loginform">
                <form className="lf">
                    <input className="textinput" type="email" name="email" placeholder="Email"></input>
                    <input id="confemail" className="textinput" type="email" placeholder="Confirm Email" style={{display:"none"}}></input>
                    <input className="textinput" type="password" name="password" placeholder="Password"></input>
                    <input id="confpassword" className="textinput" type="password" placeholder="Confirm Password" style={{display:"none"}}></input>
                    <input className="buttoninput" id="sub" type="button" value="Submit"></input>
                    <input className = "buttoninput" id="register" type="button" value="Register?" onClick={e => register()}></input>
                    <div id="error" style={{display: "none"}} className="errorMsg"></div>
                </form>

                <span className="fp" > Forgot password? </span>
            </div>
        </div>
        </div>
        </div>
        </div>
    );
  }