import React from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Title from './Title';

function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles((theme) => ({
  seeMore: {
    marginTop: theme.spacing(3),
  },
}));

export default function Description() {
  const descriptionClasses = useStyles();
  return (
    <React.Fragment>
      <Title>Description and Analysis</Title>
        <Typography variant="body1" paragraph>
        The first scenario is computing the percentage of explicit tweets in each state. The explicit tweets represent the tweets which have vulgar words, and the clean tweets mean the tweets which do not have vulgar words. As the figures shown above, the left one is a bar chart which shows the number of the clean tweets and explicit tweets respectively. From the bar chart, it infers that the number of explicit tweets for each state is commonly small. In addition, the right figure is a geomap which can suggest the percentage of explicit tweets in each state. From this graph, it can be seen that the state with the highest percentage is Victoria (1.77%) and the lowest one is ACT (0.84%). It can be concluded that people send tweets with swear words much less frequently than that without swear words. This shows that people rarely use swear words when communicating on the Internet.
        </Typography>
      <div className={descriptionClasses.seeMore} align="center">
        <Link color="primary" href="#" onClick={preventDefault} >
          See more analysis
        </Link>
      </div>
    </React.Fragment>
  );
}