/* eslint-disable react-hooks/exhaustive-deps */
import React from "react";
import Description1 from "../Dashboard/Description1";
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Tableau from '../Dashboard/Tableau'

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

  const scenario1classes = useStyles();

  const url1 = "https://public.tableau.com/views/choropleth_vulgarTweetPercentage/2?:language=en";

  return(
    <div>
      <Tableau url={url1} />
      <Paper className={scenario1classes.paper}>
        <Description1 />
      </Paper>
    </div>
  )
}

export default Scenario1;