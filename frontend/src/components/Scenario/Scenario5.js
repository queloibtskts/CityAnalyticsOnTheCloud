/* eslint-disable no-unused-vars */
import React from "react";
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Description5 from '../Dashboard/Description5';
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
    padding: theme.spacing(2),
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column',
  },
  fixedHeight: {
    height: 650,
  },
}));

const Scenario5 = () => {
  const scenario2classes = useStyles();

  const url5 = "https://public.tableau.com/views/top3vulgarWordsByState/2?:language=en";
  
  return(
    <div>
      <Tableau url={url5} />
      <Paper className={scenario2classes.paper}>
        <Description5 />
      </Paper>
    </div>
  )
}

export default Scenario5;