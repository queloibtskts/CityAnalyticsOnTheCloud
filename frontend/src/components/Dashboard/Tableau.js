/* eslint-disable react-hooks/exhaustive-deps */
import React, {useRef, useEffect} from "react";
const { tableau } = window;

const Tableau  = ({url}) => {

  const ref = useRef(null);

  const options = {
    device: "desktop",
  }
  const initViz = () => {
    new tableau.Viz(ref.current, url, options);
  }

  useEffect(() => {
    initViz();
  }, [])

  return(
      <div ref ={ref} />
  )
}

export default Tableau;