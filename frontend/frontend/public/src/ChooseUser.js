import React from "react";
export default function SubUserSelect() {

    function convert(){
        document.getElementById("login").className = "loginclicked"
    }
    return (
        <div className="center-container vertical">
            <div className="whoswatch">Who is watching?</div>
            <div className="center-container horizontal">
                <div className = "allowBig">
                    <div className = "alb">
                    <a id="subuser" className="subuser" href="/browse">
                            U
                        </a>
                        <div className="word">User1</div>
                    </div>
                </div>
                <div className = "allowBig">
                    <div className = "alb">
                    <a id="subuser" className="subuser" href="/browse">
                            U
                        </a>
                        <div className="word">User2</div>
                    </div>
                </div>
                <div className = "allowBig">
                    <div className = "alb">
                        <a id="subuser" className="subuser" href="/browse">
                            U
                        </a>
                        <div className="word">User3</div>
                    </div>
                </div>
                <div className = "allowBig">
                    <div className = "alb">
                        <div id="subuser" className="subuser">
                        +
                        </div>
                        <div className="word">Add User</div>
                    </div>
                </div>
            </div>
        </div>
    );
  }