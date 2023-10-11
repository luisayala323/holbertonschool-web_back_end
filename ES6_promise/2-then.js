/* eslint-disable */
export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log('Got a response from the API');
      return { status: 200, body: 'Success' };
    })
    .catch(() => {
      console.error('Got an error from the API');
      return new Error('API request failed');
    })
 
}
