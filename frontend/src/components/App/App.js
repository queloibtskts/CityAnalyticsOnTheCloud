import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Homepage from '../Scenario/Homepage';
import Scenario1 from '../Scenario/Scenario1';
import Scenario2 from '../Scenario/Scenario2';
import Scenario3 from '../Scenario/Scenario3';
import Scenario4 from '../Scenario/Scenario4';
import Scenario5 from '../Scenario/Scenario5';
import Dashboard from '../Dashboard/Dashboard';
import Container from '@material-ui/core/Container';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  appBarSpacer: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    height: '100vh',
    overflow: 'auto',
  },
  container: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(4),
  },
}));

const App = () => {
  const mainClasses = useStyles();
  return (
    <div className={mainClasses.root}>
      <Router>
      <Dashboard />
      <main className={mainClasses.content}>
      <div className={mainClasses.appBarSpacer} />
      <Container maxWidth="lg" className={mainClasses.container}>
        <Switch>
          <Route exact path="/" component={Homepage} />
          <Route exact path="/homepage" component={Homepage} />
          <Route path="/scenario1" component={Scenario1} />
          <Route path="/scenario2" component={Scenario2} />
          <Route path="/scenario3" component={Scenario3} />
          <Route path="/scenario4" component={Scenario4} />
          <Route path="/scenario5" component={Scenario5} />
        </Switch>
      </Container>
      </main>
    </Router>
    </div>
  );
}

export default App;
