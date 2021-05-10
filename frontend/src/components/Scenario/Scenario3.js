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

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit">
        Your Website
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

const Scenario3 = () => {
  const scenario3classes = useStyles();
  const [scenarioData, setScenarioData] = useState();
  useEffect(() => {
    const fetchData = async () => {
      const scenarioResponse = await apis.getScenarioThree();
      if (scenarioResponse.status === 200) {
        setScenarioData(scenarioResponse.data.row_number);
      }
    };
    fetchData();
  }, []);
var json = `{
  "Victoria": [
    {
      "text": "vulgar1",
      "value": 100
    },
    {
      "text": "vulgar2",
      "value": 100
    }
  ],
  "Queensland": [
    {
      "text": "vulgar2",
      "value": 100
    },
    {
      "text": "vulgar2",
      "value": 100
    }
  ],
  "Western_Australia": [
    {
      "text": "vulgar2",
      "value": 100
    },
    {
      "text": "vulgar2",
      "value": 100
    }
  ],
  "New_South_Wales": [
    {
      "text": "vulgar2",
      "value": 100
    },
    {
      "text": "vulgar2",
      "value": 100
    }
  ],
  "Northern_Territory": [
    {
      "text": "vulgar2",
      "value": 100
    },
    {
      "text": "vulgar2",
      "value": 100
    }
  ]
}`;
const mockData = JSON.parse(json);
  const fixedHeightPaper = clsx(scenario3classes.paper, scenario3classes.fixedHeight);
  return(
    <div>
      <Grid container spacing={3}>
        <Grid item xs={12} md={8} lg={9}>
          <Paper className={fixedHeightPaper}>
            <WordCloud data={mockData.Northern_Territory} />
            <div>
              {scenarioData}
            </div>
          </Paper>
        </Grid>
        <Grid item xs={12} md={4} lg={3}>
          <Paper className={fixedHeightPaper}>
            <Title>Tasks</Title>
            <Button onClick>Western Australia</Button>
            <Button color="primary">Queensland</Button>
            <Button color="secondary">Northern Territory</Button>
            <Button>New South Wales</Button>
            <Button color="primary">Victoria</Button>
            <Button color="primary">Tasmania</Button>
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