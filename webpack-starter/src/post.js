async function invokeLambda() {
    try {
        const newEmployee={
            id:4,
            first_name: "Neel",
            last_name: "Rodrigo",
            email: "udeshi@codingthesmartway.com"
        }
      const response = await fetch('https://c792wqnc52.execute-api.eu-north-1.amazonaws.com/prod/proxy', {
        method: 'POST',
        body: JSON.stringify(newEmployee)
      });
      const data = await response.json();
      console.log(data);
      return data;
    } 
    catch (err) {
      console.error(err);
    }
  }

  export default invokeLambda