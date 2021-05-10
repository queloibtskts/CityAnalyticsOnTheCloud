import React from "react";
import ReactWordcloud from "react-wordcloud";

const size = [800, 600];

const WordCloud = ({data}) => (
  <ReactWordcloud
    words={data}
    size={size} />
)
export default WordCloud;