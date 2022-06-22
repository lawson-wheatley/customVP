import React from "react";
import { useNavigate } from "react-router-dom";
export default function SearchBar() {
    const navigate = useNavigate();
    function toggleSidebar(bool){
        console.log("HA");
        if(bool){
            document.getElementById("sidebar").style.display = "block";
            document.getElementById("body").style.overflowY = "hidden";
        } else{
            document.getElementById("sidebar").style.display = "none";
            document.getElementById("body").style.overflowY = "scroll";
        }
    }
    function nav(){
        navigate("/browse");
    }
    return (<div className="searchnavbar">
        <div className="leftnav">
            <div className="leftsidebarOpener"><button className="sidebaropen" onClick={e => toggleSidebar(true)}><img src="/img/sidebaropen.svg" className="sidebaritem"></img></button>
                <div id="sidebar" className="sidebar" style={{display: "none"}}>
                    <div className="sidebaroverarch">
                        <div className="sidebarselector">
                            <button className="sidebaropen wid25" onClick={e=> toggleSidebar(false)}>
                                <img className="sidebaritem" src="/img/exit.svg"></img>
                            </button>
                            <a className="active" href="/browse">
                                Home
                            </a>
                            <a href="/movies">
                                Movies
                            </a>
                            <a href="/series">
                                Series
                            </a>
                            <div className="line"></div>
                            <a href="/nosearch?by=horror">
                                Horror
                            </a>
                            <a href="/nosearch?by=action">
                                Action
                            </a>
                            <a href="/nosearch?by=animation">
                                Animation
                            </a>
                            <a href="/nosearch?by=comedy">
                                Comedy
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div className="searchbar"><button className="sidebaropen" onClick={e => nav()}><img src="/img/exit.svg" className="sidebaritem"></img></button><input type="text" className="searchbarinput" placeholder="What are you looking for?"></input></div>
        </div>
        <div className="profnav"><div className="circ"></div>User 1</div>
        </div>
    );
  }