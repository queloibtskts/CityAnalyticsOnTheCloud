import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';
import ScenarioPages from '../ScenarioPage';

const Routes = () => (
  <Router>
    <Switch>
      <Route exact path="/scenarios" component={ScenarioPages} />
    </Switch>
  </Router>
)
export default Routes;