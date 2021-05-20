import React from "react";
import ReactWordcloud from "react-wordcloud";
import Typography from '@material-ui/core/Typography';

const size = [800, 600];

const WordCloud = ({
  data,
  title
})  => (
  <>
  <Typography>{title}</Typography>
  <ReactWordcloud
    words={data}
    size={size} />
  </>
)
export default WordCloud;