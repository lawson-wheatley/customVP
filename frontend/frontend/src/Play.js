import React, { useRef, useState} from "react";
import { useNavigate } from "react-router-dom";
export default function Play() {
    const videoRef = useRef(null);
    const queryParams = new URLSearchParams(Location.search);
    const [playing, setPlaying] = useState(false);
    const navigate = useNavigate();
    const [videoTime, setVideoTime] = useState(0);
    const [currentTime, setCurrentTime] = useState(0);
    const [progress, setProgress] = useState(0);
    const video = queryParams.get("id")
    const [cntrl, setCntrl] = useState("play");
    var elem = document.getElementById("pl");
    var timeout;
    document.onmousemove = function(){
      clearTimeout(timeout);
      document.getElementById("cc").style.display = "block";
      timeout = setTimeout(function(){document.getElementById("cc").style.display = "none";}, 5000);
    }
    function openFullscreen() {
        if (elem.requestFullscreen) {
          elem.requestFullscreen();
        } else if (elem.webkitRequestFullscreen) { /* Safari */
          elem.webkitRequestFullscreen();
        } else if (elem.msRequestFullscreen) { /* IE11 */
          elem.msRequestFullscreen();
        }
      }
    function toggleVideo(e){
        if (e.target == "hideplayer" || e.target =="cc"){
        if(cntrl === "play"){
            videoHandler(cntrl);
            setCntrl("pause");
        } else{
            videoHandler(cntrl);
            setCntrl("play");
        }
    }
    }
    const videoHandler = (control) => {
        if (control === "play") {
          videoRef.current.play();
          setPlaying(true);
          var vid = document.getElementById("player");
          setVideoTime(vid.duration);
        } else if (control === "pause") {
          videoRef.current.pause();
          setPlaying(false);
        }
      };
    function goBack(){
        navigate(-1);
    }
    const fastForward = () => {
        videoRef.current.currentTime += 5;
      };
    
      const revert = () => {
        videoRef.current.currentTime -= 5;
      };
    window.setInterval(function () {
        setCurrentTime(videoRef.current?.currentTime);
        setProgress((videoRef.current?.currentTime / videoTime) * 100);
      }, 1000);
    var item = JSON.parse('{"id":0,"title":"Was SCP-682 Really That Hard to Kill After All?","description":"SCP 682 is a Keter Class anomaly also known as Hard to Destroy Reptile.\\nSCP 173 is a Euclid Class anomaly also known as The Sculpture.\\n\\nSCP-682 is a large, vaguely reptile-like creature of unknown origin. It appears to be extremely intelligent, and was observed to engage in complex communication with SCP 079 during their limited time of exposure. SCP682 appears to have a hatred of all life, which has been expressed in several interviews during containment.\\n\\nSCP-173 is constructed from concrete and rebar with traces of Krylon brand spray paint. SCP173 is animate and extremely hostile. The object cannot move while within a direct line of sight. Line of sight must not be broken at any time with SCP-173. Personnel assigned to enter container are instructed to alert one another before blinking. Object is reported to attack by snapping the neck at the base of the skull, or by strangulation.","thumbnail":"/img/videos/scp/thumbnail.png","s1080":"img/videos/scp/size1080.mp4"}');
    return (<div id="pl">
        <div id="hideplayer" className="hideplayer" onClick={e => toggleVideo(e)}>
        <div className="videooverlay" id="cc" >
        <div className="getscotop">
            <img className="controlsIconc" src="/img/back.svg" onClick={() => goBack()} alt=""></img>
        </div>
        <div className="controlsContainer">
        <div className="getscobottom">

            <div className="timecontrols">
                <p className="controlsTime">
                    {Math.floor(currentTime / 60) + ":" + ("0" + Math.floor(currentTime % 60)).slice(-2)}
                </p>
                <div className="time_progressbarContainer">
                <div style={{ width: progress+"%" }} className="time_progressBar"></div>
                </div>
                <p className="controlsTime">
                    {Math.floor(videoTime / 60) + ":" + ("0" + Math.floor(videoTime % 60)).slice(-2)}
                </p>
            </div>
        <div className="controls">   
            {playing ? (
            <img
            onClick={() => videoHandler("pause")}
            className="controlsIcon--small"
            alt=""
            src="/pause.svg"
            />
        ) : (
            <img
            onClick={() => videoHandler("play")}
            className="controlsIcon--small"
            alt=""
            src="/img/play.svg"
            />
        )}
          <img onClick={revert} className="controlsIcon" alt="" src="/img/rewind.svg" />
          <img onClick={fastForward} className="controlsIcon" alt="" src="/img/fastforward.svg" />
          <img onClick={openFullscreen} className="controlsIcon" alt="" src="/img/fullscreen.svg" />
        </div>
        </div>
        </div>
    </div>
  </div><div className="player"><video ref={videoRef} className="videoplayer" id="player" control="false"><source src={item.s1080} type="video/mp4" /></video></div></div>

    );
  }