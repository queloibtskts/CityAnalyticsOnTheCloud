import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
    margin: theme.spacing(1),
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
    width: 300,
  },
  button: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
    marginTop: theme.spacing(2),
    width: 300,
  },
}));

const TimePickers = () => {
  const timeClasses = useStyles();

  return (
    <div>
      <form className={timeClasses.container} noValidate>
        <TextField
          id="datetime-local"
          label="FROM"
          type="datetime-local"
          defaultValue="2021-05-01T10:30"
          className={timeClasses.textField}
          InputLabelProps={{
            shrink: true,
          }}
        />
        <TextField
          id="datetime-local"
          label="TO"
          type="datetime-local"
          defaultValue="2021-05-03T10:30"
          className={timeClasses.textField}
          InputLabelProps={{
            shrink: true,
          }}
          />
        <Button
          variant="contained"
          color="primary"
          className={timeClasses.button}>
          Submit
        </Button>
        </form>
      </div>
  );
}
export default TimePickers;