import React from "react";
import Nav from "./Nav";
import Carousel from "./Carousel";
export default function Browse() {
    return (<div>
        <Nav />
        <div className="titlemovie"></div>
        <div id="continue-watching" className="genre">
            <div className="genretext">Continue Watching</div>
            <Carousel from="/continue"/>
        </div>
        </div>
    );
  }