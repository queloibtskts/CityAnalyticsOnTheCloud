import React from "react";
import ReactWordcloud from "react-wordcloud";
import Title from '../Dashboard/Title';

const WordCloud = ({
  data,
  title,
  size
})  => (
  <>
  <Title>{title}</Title>
  <ReactWordcloud
    words={data}
    size={size} />
  </>
)
export default WordCloud;