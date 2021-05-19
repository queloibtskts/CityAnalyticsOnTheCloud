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
      <Typography variant="body1" gutterBottom>
        第四个是每个州含脏话tweets的hashtag的word cloud：对比：不含脏话tweets的hashtag的word cloud<br />
        相当于每个州两个word clouds （如果数据量不够的话 这个之后还可能会改）
      </Typography>
      <div className={descriptionClasses.seeMore} align="center">
        <Link color="primary" href="#" onClick={preventDefault} >
          See more analysis
        </Link>
      </div>
    </div>
  );
}