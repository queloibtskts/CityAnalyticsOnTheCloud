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

export default function Description4() {
  const descriptionClasses = useStyles();
  return (
    <div>
       <Title>Description and Analysis</Title>
      <Typography variant="body1" paragraph>
      This scenario is talking about the word cloud of hashtags with swear words tweets and that without swear words tweets in each state. There are two figures for each state, the left one is the word cloud of hashtags with swear words in tweets, the right one is the word cloud of hashtags without swear words in tweets. From this scenario, it can infer the topics which may make people send vulgar words when talking about them. Furthermore, the emotions of people can be inferred when they are talking about some topics with swear words, it can also show people's attitudes towards this topic. From these graphs, it can be seen that the few states have less hashtags with vulgar words. The reason is because the total number of tweets in these states are quite small, it should take more time to get a large number of tweets to solve this problem.

      </Typography>
      <div className={descriptionClasses.seeMore} align="center">
        <Link color="primary" href="#" onClick={preventDefault} >
          See more analysis
        </Link>
      </div>
    </div>
  );
}