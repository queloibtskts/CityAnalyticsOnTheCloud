import React from "react";

import {
  withScriptjs,
  withGoogleMap,
  GoogleMap,
  Marker
} from "react-google-maps";

const MyMapComponent = withScriptjs(
  withGoogleMap(props => {
    return (
      <GoogleMap
        defaultZoom={5}
        defaultCenter={{ lat: -37.872603996110286, lng: 145.07584419726558 }}
      >
        <Marker position={{ lat: -37.872603996110286, lng: 145.07584419726558 }} />
      </GoogleMap>
    );
  })
);


const Homepage = () => (
  <div>
      <MyMapComponent
        googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyBt7V8flUvWd_DIfVwCcNlBFvCDJc93hgI&v=3.exp&libraries=geometry,drawing,places"
        loadingElement={<div style={{ height: `100%` }} />}
        containerElement={<div style={{ height: `100vh` }} />}
        mapElement={<div style={{ height: `100%` }} />}
      />
  </div>
)


export default Homepage;