import React from "react";
export default function Play() {
    const queryParams = new URLSearchParams(Location.search);
    const video = queryParams.get("id")
    var item = JSON.parse('{"id":0,"title":"Was SCP-682 Really That Hard to Kill After All?","description":"SCP 682 is a Keter Class anomaly also known as Hard to Destroy Reptile.\\nSCP 173 is a Euclid Class anomaly also known as The Sculpture.\\n\\nSCP-682 is a large, vaguely reptile-like creature of unknown origin. It appears to be extremely intelligent, and was observed to engage in complex communication with SCP 079 during their limited time of exposure. SCP682 appears to have a hatred of all life, which has been expressed in several interviews during containment.\\n\\nSCP-173 is constructed from concrete and rebar with traces of Krylon brand spray paint. SCP173 is animate and extremely hostile. The object cannot move while within a direct line of sight. Line of sight must not be broken at any time with SCP-173. Personnel assigned to enter container are instructed to alert one another before blinking. Object is reported to attack by snapping the neck at the base of the skull, or by strangulation.","thumbnail":"/img/videos/scp/thumbnail.png","s1080":"img/videos/scp/size1080.mp4"}');
    return (<div>
        <div className="topInfo"></div>
        <div className="player"><video className="videoplayer" id="player" src={item.s1080}></video></div>
        <div className="controls"></div>
        </div>
    );
  }