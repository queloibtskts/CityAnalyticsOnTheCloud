/* eslint-disable no-unused-vars */
import React, { useEffect }from "react";
import clsx from 'clsx';
import * as apis from '../../apis/apis';
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Task from '../Dashboard/Task';
import Description2 from '../Dashboard/Description2';
import Link from '@material-ui/core/Link';
import Typography from '@material-ui/core/Typography';
import ColumnChart from '../Chart/Chart'

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit">
        CCC Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

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


const data = [
  ['State', 'TOP1', 'TOP2', 'TOP3'],
  ['WA', 127, 111, 10],
  ['QLD', 111, 100, 1],
  ['NT', 127, 111, 10],
  ['NSW', 127, 111, 10],
  ['VIC', 127, 111, 10],
  ['TAS', 127, 111, 10],
];

const Scenario2 = () => {
  const scenario2classes = useStyles();
  const fixedHeightPaper = clsx(scenario2classes.paper, scenario2classes.fixedHeight);
  // const [testData, setTestData] = useState();
  // useEffect(() => {
  //   const fetchData = async () => {
  //     const testNameResponse = await apis.getScenarioTwo();//test
  //     if (testNameResponse.status === 200) {
  //       setTestData(testNameResponse.data);
  //     }
  //   };
  //   fetchData();
  // }, []);
  return(
    <div>
      <Grid container spacing={3}>
        <Grid item xs={12} md={8} lg={9}>
          <Paper className={fixedHeightPaper}>
            <ColumnChart data={data}/>
          </Paper>
        </Grid>
        <Grid item xs={12} md={4} lg={3}>
          <Paper className={fixedHeightPaper}>
            <Task />
          </Paper>
        </Grid>
        <Grid item xs={12}>
          <Paper className={scenario2classes.paper}>
            <Description2 />
          </Paper>
        </Grid>
      </Grid>
      <Box pt={4}>
        <Copyright />
      </Box>
    </div>
  )
}

export default Scenario2;