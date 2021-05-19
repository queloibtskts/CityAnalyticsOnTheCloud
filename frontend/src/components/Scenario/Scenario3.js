import React, { useState, useEffect } from "react";
import * as apis from '../../apis/apis';
import WordCloud from "../Chart/WordCloud"
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Title from '../Dashboard/Title';
import Button from '@material-ui/core/Button';
import Description3 from '../Dashboard/Description3';
import Link from '@material-ui/core/Link';
import Typography from '@material-ui/core/Typography';
import TimePickers from '../Dashboard/TimePickers'

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
  button:{
    marginTop: '50px',
  },
}));

const Scenario3 = () => {
  const scenario3classes = useStyles();
  const [scenarioData, setScenarioData] = useState([]);
  const [scenarioAllData, setScenarioAllData] = useState({});
  const [testData, setTestData] = useState();
  useEffect(() => {
    const fetchData = async () => {
      const scenarioResponse = await apis.getScenarioThree();// then change to getScenarioThree
      if (scenarioResponse.status === 200) {
        setScenarioAllData(scenarioResponse.data);
      }
    };
    fetchData();
  }, []);
  useEffect(() => {
    const fetchData = async () => {
      const testNameResponse = await apis.getSamples();//testget
      if (testNameResponse.status === 200) {
        setTestData(testNameResponse.data.dbname);
      }
    };
    fetchData();
  }, []);
  const WA = ()  => (setScenarioData(scenarioAllData.WA));
  const QL = () => (setScenarioData(scenarioAllData.QL));
  const NT = () => (setScenarioData(scenarioAllData.NT));
  const NSW = () => (setScenarioData(scenarioAllData.NSW));
  const VIC = () => (setScenarioData(scenarioAllData.VIC));
  const TAS = () => (setScenarioData(scenarioAllData.TAS));
  const fixedHeightPaper = clsx(scenario3classes.paper, scenario3classes.fixedHeight);
  return(
    <div>
      <Grid container spacing={3}>
        <Grid item xs={12} md={8} lg={9}>
          <Paper className={fixedHeightPaper}>
            <WordCloud data={scenarioData} />
            <div>{testData}</div>
          </Paper>
        </Grid>
        <Grid item xs={12} md={4} lg={3}>
          <Paper className={fixedHeightPaper}>
            <Title>Tasks</Title>
            <TimePickers />
            <Button onClick={WA} className={scenario3classes.button}>Western Australia</Button>
            <Button onClick={QL} color="primary">Queensland</Button>
            <Button onClick={NT} color="secondary">Northern Territory</Button>
            <Button onClick={NSW}>New South Wales</Button>
            <Button onClick={VIC} color="primary">Victoria</Button>
            <Button onClick={TAS} color="primary">Tasmania</Button>
          </Paper>
        </Grid>
        <Grid item xs={12}>
          <Paper className={scenario3classes.paper}>
            <Description3 />
          </Paper>
        </Grid>
      </Grid>
      <Box pt={4}>
        <Copyright />
      </Box>
    </div>
  )
}

export default Scenario3;