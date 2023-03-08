async function getData() {
    try {
      const response = await fetch('https://c792wqnc52.execute-api.eu-north-1.amazonaws.com/prod/proxy?id=2');
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  }


  export default getData