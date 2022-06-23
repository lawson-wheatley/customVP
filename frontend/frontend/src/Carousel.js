import React from "react";
import Movie from "./Movie";
export default function Carousel(props) {
    var item = JSON.parse('{"id":0,"title":"SCP-682","description":"SCP 682 is a Keter Class anomaly also known as Hard to Destroy Reptile.\\nSCP 173 is a Euclid Class anomaly also known as The Sculpture.\\n\\nSCP-682 is a large, vaguely reptile-like creature of unknown origin. It appears to be extremely intelligent, and was observed to engage in complex communication with SCP 079 during their limited time of exposure. SCP682 appears to have a hatred of all life, which has been expressed in several interviews during containment.\\n\\nSCP-173 is constructed from concrete and rebar with traces of Krylon brand spray paint. SCP173 is animate and extremely hostile. The object cannot move while within a direct line of sight. Line of sight must not be broken at any time with SCP-173. Personnel assigned to enter container are instructed to alert one another before blinking. Object is reported to attack by snapping the neck at the base of the skull, or by strangulation.","thumbnail":"/img/videos/scp/thumbnail.png","1080":"/videos/scp/size1080.mp4"}');
    var items = [item, item, item, item, item, item, item, item]
    var pages = []
    var page = 0;
    const maxInPage = 4
    var iterpage = 0;
    var isShifting = false
    function changePage(val){
        page += val;
    }
    function processPages(){
        var tmppages = []
        for(var i = 0; i < items.length; i++){
            tmppages.push(items[i]);
            if (i%maxInPage ==(maxInPage - 1)){
                pages.push(tmppages);
                tmppages = [];
            }
        }
    }
    processPages();
    function shiftCarousel(val){
            console.log(document.getElementById("carousel"+props.name).style.marginLeft);
            page += val;
            console.log(document.getElementById(props.name+"pg"+page).offsetLeft);
            document.getElementById(props.name+"pg"+page).style.pointerEvents = "auto";
            var pgprev = page - val;
            document.getElementById(props.name+"pg"+pgprev).style.pointerEvents = "none";
            if(page == 0){
                document.getElementById("left"+props.name).style.opacity = 0;
            } else{
                document.getElementById("left"+props.name).style.opacity = 1;
            }
            if (page == pages.length - 1){
                document.getElementById("right"+props.name).style.opacity = 0;
            } else{
                document.getElementById("right"+props.name).style.opacity = 1;
            }
            document.getElementById("carousel"+props.name).scrollTo(document.getElementById(props.name+"pg"+page).offsetLeft-40, 0, "smooth");
    }
    console.log(pages);
    return (
        <div className="bigCarousel">
            <button className="leftCarouselButton" style = {{opacity: 0}} id = {"left"+props.name} onClick={e=> shiftCarousel(-1)}></button>
            <div id = {"carousel"+props.name} className="carousel">
                {
                pages.map(function(element){
                    iterpage += 1;
                    var xc = iterpage-1
                    var hasEvents = "none";
                    if (xc == 0){
                        hasEvents = "auto";
                    }
                    return (<div className = "page" style={{pointerEvents: hasEvents}} id = {props.name+"pg"+xc}>
                        {element.map(elem => Movie(elem))}
                        </div>)

                })}
                <div className="page" >

                </div>
            </div>
            <button className="rightCarouselButton" id = {"right"+props.name} onClick={e=> shiftCarousel(1)}></button>

        </div>
    );
  }