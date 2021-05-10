/* eslint-disable react-hooks/exhaustive-deps */
import React, {useRef, useEffect} from "react";
import Description1 from "../Dashboard/Description1";
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
const { tableau } = window;

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  content: {
    flexGrow: 1,
    height: '100vh',
    overflow: 'auto',
  },

  paper: {
    marginTop: theme.spacing(3),
    padding: theme.spacing(2),
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column',
  },
  fixedHeight: {
    height: 650,
  },
}));
const Scenario1 = () => {

  const scenario2classes = useStyles();

  const url = "https://public.tableau.com/views/choropleth_vulgarTweetPercentage/2?:language=en";

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
    <div>
      <div ref ={ref} ></div>
      <Paper className={scenario2classes.paper}>
        <Description1 />
      </Paper>
    </div>
  )
}

export default Scenario1;