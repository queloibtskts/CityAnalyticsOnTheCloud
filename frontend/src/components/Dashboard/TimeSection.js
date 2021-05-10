import React from 'react';
import Timeline from '@material-ui/lab/Timeline';
import TimelineItem from '@material-ui/lab/TimelineItem';
import TimelineSeparator from '@material-ui/lab/TimelineSeparator';
import TimelineConnector from '@material-ui/lab/TimelineConnector';
import TimelineContent from '@material-ui/lab/TimelineContent';
import TimelineDot from '@material-ui/lab/TimelineDot';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(() => ({
  button: {
    fontSize: 9,
  },
  timeline:{
    marginTop: '50px',
  },
})
);
const TimeSection = () => {
  const TimeSectionClass = useStyles();
  return (
    <Timeline className={TimeSectionClass.timeline} align="alternate">
      <TimelineItem>
        <TimelineSeparator>
          <TimelineDot variant="outlined" />
          <TimelineConnector />
        </TimelineSeparator>
        <TimelineContent>
          <Button className={TimeSectionClass.button}>Morning</Button>
        </TimelineContent>
      </TimelineItem>
      <TimelineItem>
        <TimelineSeparator>
          <TimelineDot variant="outlined" color="primary" />
          <TimelineConnector />
        </TimelineSeparator>
        <TimelineContent>
          <Button className={TimeSectionClass.button}>Noon</Button>
        </TimelineContent>
      </TimelineItem>
      <TimelineItem>
        <TimelineSeparator>
          <TimelineDot variant="outlined" color="secondary" />
          <TimelineConnector />
        </TimelineSeparator>
        <TimelineContent>
          <Button className={TimeSectionClass.button}>Afternoon</Button>
        </TimelineContent>
      </TimelineItem>
      <TimelineItem>
        <TimelineSeparator>
          <TimelineDot variant="outlined" />
        </TimelineSeparator>
        <TimelineContent>
          <Button className={TimeSectionClass.button}>Evening</Button>
        </TimelineContent>
      </TimelineItem>
    </Timeline>
  );
}

export default TimeSection;