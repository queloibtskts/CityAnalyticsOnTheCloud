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
import InsertChartIcon from '@material-ui/icons/InsertChart';
import AttachMoneyIcon from '@material-ui/icons/AttachMoney';
import MapOutlinedIcon from '@material-ui/icons/MapOutlined';
import CompareArrowsIcon from '@material-ui/icons/CompareArrows';

export const mainListItems = (
  <>
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
  </>
);

export const secondaryListItems = (
  <>
    <ListSubheader inset>Scenarios</ListSubheader>
    <Link to="/scenario1">
      <ListItem button>
        <ListItemIcon>
          <MapOutlinedIcon />
        </ListItemIcon>
        <ListItemText primary="Scenario 1" />
      </ListItem>
    </Link>
    <Link to="/scenario2">
      <ListItem button>
        <ListItemIcon>
        <InsertChartIcon />
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
    <Link to="/scenario4">
    <ListItem button>
      <ListItemIcon>
        <CompareArrowsIcon />
      </ListItemIcon>
      <ListItemText primary="Scenario 4" />
    </ListItem>
    </Link>
    <Link to="/scenario5">
    <ListItem button>
      <ListItemIcon>
        <AttachMoneyIcon />
      </ListItemIcon>
      <ListItemText primary="Scenario 5" />
    </ListItem>
    </Link>
  </>
);