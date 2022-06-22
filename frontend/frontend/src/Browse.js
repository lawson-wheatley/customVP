import React from "react";
import Nav from "./Nav";
import Carousel from "./Carousel";
export default function Browse() {

    return (<div>
        <Nav />
        <div className="titlemovie"></div>
        <div className="carousels">
        <div id="continue-watching" className="genre">
            <div className="genretext">Continue Watching</div>
            <Carousel from="/get/continue"/>
        </div>
        <div id="horror" className="genre">
            <div className="genretext">Horror</div>
            <Carousel from="/get/horror"/>
        </div>
        </div>
        </div>
    );
  }