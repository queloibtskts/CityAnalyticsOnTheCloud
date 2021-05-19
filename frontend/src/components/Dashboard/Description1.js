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
        <Typography variant="body1" gutterBottom>
          第一个是地图：每个州vulgar percentage对比每个州的平均收入
        </Typography>
      <div className={descriptionClasses.seeMore} align="center">
        <Link color="primary" href="#" onClick={preventDefault} >
          See more analysis
        </Link>
      </div>
    </React.Fragment>
  );
}