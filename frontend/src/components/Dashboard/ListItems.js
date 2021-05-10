import React from 'react';
import {
  Link,
} from 'react-router-dom';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import ListSubheader from '@material-ui/core/ListSubheader';
import DashboardIcon from '@material-ui/icons/Dashboard';
import SaveAltIcon from '@material-ui/icons/SaveAlt';
import SpellcheckIcon from '@material-ui/icons/Spellcheck';
import AccessTimeIcon from '@material-ui/icons/AccessTime';
import EqualizerIcon from '@material-ui/icons/Equalizer';

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
          <SaveAltIcon />
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
          <EqualizerIcon />
        </ListItemIcon>
        <ListItemText primary="Scenario 1" />
      </ListItem>
    </Link>
    <Link to="/scenario2">
      <ListItem button>
        <ListItemIcon>
        <AccessTimeIcon />
        </ListItemIcon>
        <ListItemText primary="Scenario 2" />
      </ListItem>
    </Link>
    <Link to="/scenario3">
    <ListItem button>
      <ListItemIcon>
        <SpellcheckIcon />
      </ListItemIcon>
      <ListItemText primary="Scenario 3" />
    </ListItem>
    </Link>
  </div>
);