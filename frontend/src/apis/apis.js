import axios from 'axios';
const baseUrl = process.env.REACT_APP_CCC_API;

// Start getScenario1//
export const getScenarioOne = ( ) => axios({
  method: 'get',
  url: `${baseUrl}/scenario1`,
});
// Finish getScenario1//

// Start getScenario2//
export const getScenarioTwo = ( ) => axios({
  method: 'get',
  url: `${baseUrl}/scenario2`,
});
// Finish getScenario2//

// Start getScenario3//
export const getScenarioThree = ( ) => axios({
  method: 'get',
  url: `${baseUrl}/scenario3`,
});
// Finish getScenario3//


// Start getScenario3//
export const getScenarioFour = ( ) => axios({
  method: 'get',
  url: `${baseUrl}/scenario4`,
});
// Finish getScenario3//

// Start getSamples//
export const getSamples = ( ) => axios({
  method: 'get',
  url: `${baseUrl}/samples`,
});
// Finish getSamples//