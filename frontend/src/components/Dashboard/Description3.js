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

export default function Description3() {
  const descriptionClasses = useStyles();
  return (
    <div>
       <Title>Description and Analysis</Title>
      <Typography variant="body1" paragraph>
        This scenario is making a word cloud to find out which swear words are more commonly used in  Australia. As the figure shown above, this is a word cloud which consists of the vulgar words that are more commonly used in Australia. From the word cloud, it suggests that the word “fuck” and its derivatives are the most commonly used words Australia, it also confirms the phenomenon in scenario two.
      </Typography>
      <div className={descriptionClasses.seeMore} align="center">
        <Link color="primary" href="#" onClick={preventDefault} >
          See more analysis
        </Link>
      </div>
    </div>
  );
}