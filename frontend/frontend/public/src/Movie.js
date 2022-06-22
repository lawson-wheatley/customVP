import React from "react";
import { useNavigate } from "react-router-dom";
export default function Movie(item) {
    let navigate = useNavigate();
    function play(){
        navigate("/play?id="+item.id)
    }
    return (
        <div className="movieholder">
            <div className="movie">
                <img className="thumbnail" src={item.thumbnail}></img>
                <div className="moviebottom">
                    <div className="moviebuttons">
                        <button className="moviebutton" onClick={e=> play()}><img className="moviepos" src="/img/play.svg"></img></button>
                        </div>
                </div>
            </div>

        </div>
    );
  }