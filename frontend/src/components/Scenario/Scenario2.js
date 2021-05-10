import React, {useState, useEffect} from "react";
import * as apis from '../../apis/apis';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import WordCloud from '../Chart/WordCloud';
import Task2 from '../Dashboard/Task2';
import Description2 from '../Dashboard/Description2';
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

const Scenario2 = () => {
  const scenario2classes = useStyles();
  const fixedHeightPaper = clsx(scenario2classes.paper, scenario2classes.fixedHeight);
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
  const mockCloudData = [
    {
      text: 'Scenario2',
      value: 164,
    },
    {
      text: 'mistake',
      value: 11,
    },
    {
      text: 'thought',
      value: 16,
    },
    {
      text: 'bad',
      value: 17,
    },
    {
      text: 'correct',
      value: 10,
    },
    {
      text: 'day',
      value: 54,
    },
    {
      text: 'prescription',
      value: 12,
    },
    {
      text: 'time',
      value: 77,
    },
    {
      text: 'thing',
      value: 45,
    },
    {
      text: 'left',
      value: 19,
    },
    {
      text: 'pay',
      value: 13,
    },
    {
      text: 'people',
      value: 32,
    },
    {
      text: 'month',
      value: 22,
    },
    {
      text: 'again',
      value: 35,
    },
    {
      text: 'review',
      value: 24,
    },
    {
      text: 'call',
      value: 38,
    },
    {
      text: 'doctor',
      value: 70,
    },
    {
      text: 'asked',
      value: 26,
    },
    {
      text: 'finally',
      value: 14,
    },
    {
      text: 'insurance',
      value: 29,
    },
    {
      text: 'week',
      value: 41,
    },
    {
      text: 'called',
      value: 49,
    },
    {
      text: 'problem',
      value: 20,
    },
    {
      text: 'going',
      value: 59,
    },
    {
      text: 'help',
      value: 49,
    },
    {
      text: 'felt',
      value: 45,
    },
    {
      text: 'discomfort',
      value: 11,
    },
    {
      text: 'lower',
      value: 22,
    },
    {
      text: 'severe',
      value: 12,
    },
    {
      text: 'free',
      value: 38,
    },
    {
      text: 'better',
      value: 54,
    },
    {
      text: 'muscle',
      value: 14,
    },
    {
      text: 'neck',
      value: 41,
    },
    {
      text: 'root',
      value: 24,
    },
    {
      text: 'adjustment',
      value: 16,
    },
    {
      text: 'fuck',
      value: 78,
    },
    {
      text: 'injury',
      value: 20,
    },
    {
      text: 'excruciating',
      value: 10,
    },
    {
      text: 'chronic',
      value: 13,
    },
    {
      text: 'chiropractor',
      value: 35,
    },
    {
      text: 'treatment',
      value: 59,
    },
    {
      text: 'tooth',
      value: 32,
    },
    {
      text: 'chiropractic',
      value: 17,
    },
    {
      text: 'dr',
      value: 77,
    },
    {
      text: 'relief',
      value: 19,
    },
    {
      text: 'shoulder',
      value: 26,
    },
    {
      text: 'nurse',
      value: 17,
    },
    {
      text: 'room',
      value: 22,
    },
    {
      text: 'hour',
      value: 35,
    },
    {
      text: 'wait',
      value: 38,
    },
    {
      text: 'hospital',
      value: 11,
    },
    {
      text: 'eye',
      value: 13,
    },
    {
      text: 'test',
      value: 10,
    },
    {
      text: 'appointment',
      value: 49,
    },
    {
      text: 'medical',
      value: 19,
    },
    {
      text: 'question',
      value: 20,
    },
    {
      text: 'office',
      value: 64,
    },
    {
      text: 'care',
      value: 54,
    },
    {
      text: 'minute',
      value: 29,
    },
    {
      text: 'waiting',
      value: 16,
    },
    {
      text: 'patient',
      value: 59,
    },
    {
      text: 'health',
      value: 49,
    },
    {
      text: 'alternative',
      value: 24,
    },
    {
      text: 'holistic',
      value: 19,
    },
    {
      text: 'traditional',
      value: 20,
    },
    {
      text: 'symptom',
      value: 29,
    },
    {
      text: 'internal',
      value: 17,
    },
    {
      text: 'prescribed',
      value: 26,
    },
    {
      text: 'acupuncturist',
      value: 16,
    },
    {
      text: 'pain',
      value: 64,
    },
    {
      text: 'integrative',
      value: 10,
    },
    {
      text: 'herb',
      value: 13,
    },
    {
      text: 'sport',
      value: 22,
    },
    {
      text: 'physician',
      value: 41,
    },
    {
      text: 'herbal',
      value: 11,
    },
    {
      text: 'eastern',
      value: 12,
    },
    {
      text: 'chinese',
      value: 32,
    },
    {
      text: 'acupuncture',
      value: 45,
    },
    {
      text: 'prescribe',
      value: 14,
    },
    {
      text: 'medication',
      value: 38,
    },
    {
      text: 'western',
      value: 35,
    },
    {
      text: 'sure',
      value: 38,
    },
    {
      text: 'work',
      value: 64,
    },
    {
      text: 'smile',
      value: 17,
    },
    {
      text: 'teeth',
      value: 26,
    },
    {
      text: 'pair',
      value: 11,
    },
    {
      text: 'wanted',
      value: 20,
    },
    {
      text: 'frame',
      value: 13,
    },
    {
      text: 'lasik',
      value: 10,
    },
    {
      text: 'amazing',
      value: 41,
    },
    {
      text: 'fit',
      value: 14,
    },
    {
      text: 'happy',
      value: 22,
    },
    {
      text: 'feel',
      value: 49,
    },
    {
      text: 'glasse',
      value: 19,
    },
    {
      text: 'vision',
      value: 12,
    },
    {
      text: 'pressure',
      value: 16,
    },
    {
      text: 'find',
      value: 29,
    },
    {
      text: 'experience',
      value: 59,
    },
    {
      text: 'year',
      value: 70,
    },
    {
      text: 'massage',
      value: 35,
    },
    {
      text: 'best',
      value: 54,
    },
    {
      text: 'mouth',
      value: 20,
    },
    {
      text: 'staff',
      value: 64,
    },
    {
      text: 'gum',
      value: 10,
    },
    {
      text: 'chair',
      value: 12,
    },
    {
      text: 'ray',
      value: 22,
    },
    {
      text: 'dentistry',
      value: 11,
    },
    {
      text: 'canal',
      value: 13,
    },
    {
      text: 'procedure',
      value: 32,
    },
    {
      text: 'filling',
      value: 26,
    },
    {
      text: 'gentle',
      value: 19,
    },
    {
      text: 'cavity',
      value: 17,
    },
    {
      text: 'crown',
      value: 14,
    },
    {
      text: 'cleaning',
      value: 38,
    },
    {
      text: 'hygienist',
      value: 24,
    },
    {
      text: 'dental',
      value: 59,
    },
    {
      text: 'charge',
      value: 24,
    },
    {
      text: 'cost',
      value: 29,
    },
    {
      text: 'charged',
      value: 13,
    },
    {
      text: 'spent',
      value: 17,
    },
    {
      text: 'paying',
      value: 14,
    },
    {
      text: 'pocket',
      value: 12,
    },
    {
      text: 'dollar',
      value: 11,
    },
    {
      text: 'business',
      value: 32,
    },
    {
      text: 'refund',
      value: 10,
    },
  ]
  return(
    <div>
      <Grid container spacing={3}>
        <Grid item xs={12} md={8} lg={9}>
          <Paper className={fixedHeightPaper}>
          <WordCloud data={mockCloudData} />
          <div>
              {scenarioData}
            </div>
          </Paper>
        </Grid>
        <Grid item xs={12} md={4} lg={3}>
          <Paper className={fixedHeightPaper}>
            <Task2 />
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