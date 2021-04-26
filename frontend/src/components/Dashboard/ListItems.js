import React from 'react';
import {
  Link,
} from 'react-router-dom';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import ListSubheader from '@material-ui/core/ListSubheader';
import DashboardIcon from '@material-ui/icons/Dashboard';
import BarChartIcon from '@material-ui/icons/BarChart';
import FastfoodIcon from '@material-ui/icons/Fastfood';
import LocalHospitalIcon from '@material-ui/icons/LocalHospital';
import SportsHandballIcon from '@material-ui/icons/SportsHandball';

export const mainListItems = (
  <div>
    <Link to="/homepage">
      <ListItem button>
        <ListItemIcon>
          <DashboardIcon />
        </ListItemIcon>
        <ListItemText primary="Homepage" />
      </ListItem>
    </Link>
    <Link to="/report">
      <ListItem button>
        <ListItemIcon>
          <BarChartIcon />
        </ListItemIcon>
        <ListItemText primary="Report" />
      </ListItem>
    </Link>
  </div>
);

export const secondaryListItems = (
  <div>
    <ListSubheader inset>Scenarios</ListSubheader>
    <Link to="/scenario1">
      <ListItem button>
        <ListItemIcon>
          <LocalHospitalIcon />
        </ListItemIcon>
        <ListItemText primary="Scenario 1" />
      </ListItem>
    </Link>
    <Link to="/scenario2">
      <ListItem button>
        <ListItemIcon>
          <SportsHandballIcon />
        </ListItemIcon>
        <ListItemText primary="Scenario 2" />
      </ListItem>
    </Link>
    <Link to="/scenario3">
    <ListItem button>
      <ListItemIcon>
        <FastfoodIcon />
      </ListItemIcon>
      <ListItemText primary="Scenario 3" />
    </ListItem>
    </Link>
  </div>
);