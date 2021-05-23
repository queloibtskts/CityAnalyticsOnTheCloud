/* eslint-disable no-unused-vars */
import React from "react";
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Description2 from '../Dashboard/Description2';
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

const Scenario2 = () => {
  const scenario2classes = useStyles();

  const url2 = "https://public.tableau.com/views/rankVulgarWords/2?:language=en";
  
  return(
    <div>
      <Tableau url={url2} />
      <Paper className={scenario2classes.paper}>
        <Description2 />
      </Paper>
    </div>
  )
}

export default Scenario2;