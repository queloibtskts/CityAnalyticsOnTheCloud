
import React from 'react';
import Title from './Title';
import TimePickers from './TimePickers';
import TimeSection from './TimeSection';

const Task = () => {
  return (
    <React.Fragment>
      <Title>Tasks</Title>
      <TimePickers />
      <TimeSection />
    </React.Fragment>
  );
}

export default Task;