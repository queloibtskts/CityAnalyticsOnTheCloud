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
import Description4 from '../Dashboard/Description4';
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

const Scenario4 = () => {
  const scenario4classes = useStyles();
  const [scenarioVulgarData, setScenarioVulgarData] = useState([]);
  const [scenarioAllVulgarData, setScenarioAllVulgarData] = useState({});
  const [scenarioCleanData, setScenarioCleanData] = useState([]);
  const [scenarioAllCleanData, setScenarioAllCleanData] = useState({});
  useEffect(() => {
    const fetchData = async () => {
      const scenarioCleanResponse = await apis.getScenarioFourClean();
      const scenarioVulgarResponse = await apis.getScenarioFourVulgar();
      if (scenarioCleanResponse.status === 200) {
        setScenarioAllCleanData(scenarioCleanResponse.data);
      }
      if (scenarioVulgarResponse.status === 200) {
        setScenarioAllVulgarData(scenarioVulgarResponse.data);
      }
    };
    fetchData();
  }, []);

  const WA = ()  => {setScenarioVulgarData(scenarioAllVulgarData.WA); setScenarioCleanData(scenarioAllCleanData.WA)};
  const QLD = () => {setScenarioVulgarData(scenarioAllVulgarData.QLD); setScenarioCleanData(scenarioAllCleanData.QLD)};
  const NT = () => {setScenarioVulgarData(scenarioAllVulgarData.NT); setScenarioCleanData(scenarioAllCleanData.NT)};
  const NSW = () => {setScenarioVulgarData(scenarioAllVulgarData.NSW); setScenarioCleanData(scenarioAllCleanData.NSW)};
  const VIC = () => {setScenarioVulgarData(scenarioAllVulgarData.VIC); setScenarioCleanData(scenarioAllCleanData.VIC)};
  const TAS = () => {setScenarioVulgarData(scenarioAllVulgarData.TAS); setScenarioCleanData(scenarioAllCleanData.TAS)};
  const fixedHeightPaper = clsx(scenario4classes.paper, scenario4classes.fixedHeight);
  return(
    <div>
      <Grid container spacing={3}>
        <Grid item xs={12} md={8} lg={9}>
          <Paper className={fixedHeightPaper}>
            <WordCloud data={scenarioVulgarData} title={'vuglar_viewHashtagFreq'}/>
            <WordCloud data={scenarioCleanData} title={'clean_viewHashtagFreq'}/>
          </Paper>
        </Grid>
        <Grid item xs={12} md={4} lg={3}>
          <Paper className={fixedHeightPaper}>
            <Title>Tasks</Title>
            <TimePickers />
            <Button onClick={WA} className={scenario4classes.button}>Western Australia</Button>
            <Button onClick={QLD} color="primary">Queensland</Button>
            <Button onClick={NT} color="secondary">Northern Territory</Button>
            <Button onClick={NSW}>New South Wales</Button>
            <Button onClick={VIC} color="primary">Victoria</Button>
            <Button onClick={TAS} color="primary">Tasmania</Button>
          </Paper>
        </Grid>
        <Grid item xs={12}>
          <Paper className={scenario4classes.paper}>
            <Description4 />
          </Paper>
        </Grid>
      </Grid>
      <Box pt={4}>
        <Copyright />
      </Box>
    </div>
  )
}

export default Scenario4;