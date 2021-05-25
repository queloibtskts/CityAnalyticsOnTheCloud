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

export default function Description2() {
  const descriptionClasses = useStyles();
  return (
    <div>
       <Title>Description and Analysis</Title>
      <Typography variant="body1" paragraph>
      The second scenario is to find out the top 3 commonly used vulgar words in each state and count out the frequency of these words being used. From the figure above, different colors represent each state. It can be easy to point out that Victoria, New South Wales and Queensland are the three states which have higher vulgar words used frequency. Perhaps this phenomenon is related to the populations. Because these three states have larger populations than other states, then the frequency of using swear words will be relatively higher. Furthermore, from the figure, in each state, the top three words in the frequency of swear words have “fuck” and its derivatives “fucking”, and the rest one of the top 3 vulgar words  for each state may have some differences. It explains that word “fuck” and its derivatives become the most popular vulgar words in the whole Australia. For the differences between the rest of the top 3 vulgar words for each state, it may be caused by the local dialect or the age of the population being different in each state.

      </Typography>
      <div className={descriptionClasses.seeMore} align="center">
        <Link color="primary" href="#" onClick={preventDefault} >
          See more analysis
        </Link>
      </div>
    </div>
  );
}