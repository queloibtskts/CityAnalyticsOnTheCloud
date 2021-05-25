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

export default function Description5() {
  const descriptionClasses = useStyles();
  return (
    <div>
       <Title>Description and Analysis</Title>
      <Typography variant="body1" paragraph>
      The final scenario is about the relationship between swear words frequency and average of annual personal income. From the figure above, different symbols represent different states. The x-axis represents average personal income and the y-axis represents percentage of vulgar words. Among these states, ACT and Northern Territory have very small numbers of tweets, and the small sample size may cause inaccurate results. If the two records of ACT and Northern are eliminated, it can be seen that Tasmania has the lowest value with both vulgar percentage and average personal income,  Victoria, Queensland, New South Wales and Western Australia have the highest vulgar percentage, however the average personal income for these 4 states are different. It can be predicted that the percentage of tweets with swear words may increase with the increasing of average personal income. When the average personal income increases to a certain value, the percentage of swear words may be stable and no longer continue to increase significantly. Additionally, the percentage of tweets with swear words may be influenced by other factors. A deeper research can be done in the future.
      </Typography>
      <div className={descriptionClasses.seeMore} align="center">
        <Link color="primary" href="#" onClick={preventDefault} >
          See more analysis
        </Link>
      </div>
    </div>
  );
}